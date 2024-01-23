from flask import Flask ,render_template, request, url_for
from random import randint 

app= Flask(__name__, static_folder="static")


@app.route("/")
def index():
    return render_template("/html/home.html")


@app.route("/login", methods = ["POST"])
def login():
    user= request.form.get("name")
    keyword = request.form.get("password")                
    if user == "Lucas" and keyword =="Bananas123":            
        return f"<h1>Bem vindo {user} </h1>"
    elif user !="Lucas" and keyword != "Bananas123":
        erro = "VOCÊ DIGITOU A SENHA E O USUÁRIO INCORRETAMENTE"
        return render_template("/html/home.html",erro = erro)
    elif user != "Lucas":
        erro = "VOCÊ DIGITOU O USUÁRIO INCORRETAMENTE"            
        return render_template("/html/home.html",erro = erro)
    else:
        erro = "VOCÊ DIGITOU A SENHA INCORRETAMENTE"            
        return render_template("/html/home.html",erro = erro)

@app.route("/Produtos")
def produtos():
    return render_template("/html/produtos.html")


@app.route("/<string:nome>")
def error(nome):
    return render_template("/html/erro.html", name_page=nome)



if __name__=="__main__":
    app.run(debug = True, port=5000)

