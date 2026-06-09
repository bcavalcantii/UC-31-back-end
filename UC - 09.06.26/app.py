from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route("/")
def inicio():
    nome = request.cookies.get("nome_visitante", "")
    tema = request.cookies.get("tema", "claro")
    return render_template("inicio.html", nome=nome, tema=tema)


@app.route("/salvar-nome", methods=["POST"])
def salvar_nome():
    nome = request.form.get("nome", "").strip()
    resposta = make_response(redirect(url_for("inicio")))
    if nome:
        # Cookie dura 30 dias (em segundos)
        resposta.set_cookie("nome_visitante", nome, max_age=30 * 24 * 60 * 60)
    return resposta


@app.route("/alterar-tema/<tema>")
def alterar_tema(tema):
    if tema not in ("claro", "escuro"):
        tema = "claro"
    resposta = make_response(redirect(url_for("inicio")))
    resposta.set_cookie("tema", tema, max_age=30 * 24 * 60 * 60)
    return resposta


@app.route("/limpar")
def limpar():
    """Remove todos os cookies e volta à página inicial."""
    resposta = make_response(redirect(url_for("inicio")))
    resposta.delete_cookie("nome_visitante")
    resposta.delete_cookie("tema")
    return resposta


if __name__ == "__main__":
    app.run(debug=True)