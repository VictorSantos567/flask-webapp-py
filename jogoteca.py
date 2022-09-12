from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = "alura"


class Jogo:
    def __init__(self, nome, estilo, console):
        self.nome = nome
        self.estilo = estilo
        self.console = console


jogo_um = Jogo("havest moon", "simulação", "PS1")
jogo_dois = Jogo("LOL", "MOBA", "PC")
lista = [jogo_um, jogo_dois]


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


usuario_um = Usuario("Victor", "victao", "alohomora")
usuario_dois = Usuario("João", "batista", "voz_deserto")
usuario_tres = Usuario("Mina", "cobra", "python")

usuarios = {
    usuario_um.nickname: usuario_um,
    usuario_dois.nickname: usuario_dois,
    usuario_tres.nickname: usuario_tres,
}  # nickname chave para levar ao proprio usuario


@app.route("/")
def index():
    return render_template("index.html", titulo="Jogos", jogos=lista)


@app.route("/novo")
def novo():
    if "usuario_logado" not in session or session["usuario_logado"] == None:
        return redirect(url_for("login", proxima=url_for("novo")))

    return render_template("novo.html", titulo="Novo Jogo")


@app.route(
    "/criar",
    methods=[
        "POST",
    ],
)
def criar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for("index"))


@app.route("/login")
def login():
    proxima = request.args.get("proxima")
    return render_template("login.html", proxima=proxima)


@app.route(
    "/autenticar",
    methods=[
        "POST",
    ],
)
def autenticar():
    if request.form["login"] in usuarios:
        usuario = usuarios[request.form["login"]]
        if request.form["senha"] == usuario.senha:
            session["usuario_logado"] = usuario.nickname
            flash(usuario.nickname + " está logado corretamente.")
            proxima_pagina = request.form["proxima"]
            return redirect(proxima_pagina)
    else:
        flash("Usuário digitou nome ou senha incorretamente")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session["usuario_logado"] = None
    flash("Logout efetuado")
    return redirect(url_for("index"))


app.run(debug=True)
