from flask import Flask, render_template, request
from pontuacaoTorre import calculate_score


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/torredelondres", methods=['GET', 'POST'])
def processar_teste():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        acertos = request.form['acertos']
        resultado = calculate_score(nome, idade, acertos)
        # Agora você pode passar o 'resultado' para um template ou fazer o que precisar com ele
        return render_template("resultadoTorre.html", resultado=resultado)
    return render_template("torredelondres.html")  # A página com o formulário


if __name__ == "__main__":
    app.run()