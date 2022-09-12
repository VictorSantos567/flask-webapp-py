from flask import Flask, render_template, request, redirect, session, flash

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


@app.route("/")
def index():
    return render_template("index.html", titulo="Jogos", jogos=lista)


@app.route("/novo")
def novo():
    if "usuario_logado" not in session or session["usuario_logado"] == None:
        return redirect("/login?proxima=novo")

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
    return redirect("/")


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
    if "alohomora" == request.form["senha"]:
        session["usuario_logado"] = request.form["login"]
        flash(session["usuario_logado"] + " está logado corretamente.")
        proxima_pagina = request.form["proxima"]
        return redirect("/{}".format(proxima_pagina))
    else:
        flash("Usuário digitou nome ou senha incorretamente")
        return redirect("/login")


@app.route("/logout")
def logout():
    session["usuario_logado"] = None
    flash("Logout efetuado")
    return redirect("/")


app.run(debug=True)
