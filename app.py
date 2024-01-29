from flask import Flask ,render_template, request, url_for
from views.login import login_page
from random import randint 

app= Flask(__name__, static_folder="static")


@app.route("/")
def index():
    return render_template("/html/home.html")

@app.route("/login")
def entrar():
    return render_template("/html/entrar.html")

app.register_blueprint(login_page)

@app.route("/Produtos")
def produtos():
    return render_template("/html/produtos.html")


@app.route("/<string:nome>")
def error(nome):
    return render_template("/html/erro.html", name_page=nome)



if __name__=="__main__":
    app.run(debug = True, port=5000)

