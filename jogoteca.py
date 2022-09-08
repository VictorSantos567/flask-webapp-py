from flask import Flask, render_template, request, redirect

app = Flask(__name__)


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
    return render_template("login.html", titulo="Login")


@app.route(
    "/autenticar",
    methods=[
        "POST",
    ],
)
def autenticar():
    if "alohomora" == request.form["senha"]:
        return redirect("/")
    else:
        return redirect("/login")


app.run(debug=True)
