from flask import Flask, render_template, request

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, estilo, console):
        self.nome = nome
        self.estilo = estilo
        self.console = console


jogo_um = Jogo("havest moon", "fazenda", "PS1")
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
    return render_template("index.html", titulo="Jogos", jogos=lista)


app.run(debug=True)
