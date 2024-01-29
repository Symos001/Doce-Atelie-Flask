from flask import Blueprint,render_template,request

login_page = Blueprint('login', __name__)

@login_page.route("/login", methods = ["POST"])
def login():
    user= request.form.get("name")
    keyword = request.form.get("password")                
    if user == "Lucas" and keyword =="Bananas123":            
        return f"<h1>Bem vindo {user} </h1>"
    elif user !="Lucas" and keyword != "Bananas123":
        erro = "VOCÊ DIGITOU A SENHA E O USUÁRIO INCORRETAMENTE"
        return render_template("/html/entrar.html",erro = erro)
    elif user != "Lucas":
        erro = "VOCÊ DIGITOU O USUÁRIO INCORRETAMENTE"            
        return render_template("/html/entrar.html",erro = erro)
    else:
        erro = "VOCÊ DIGITOU A SENHA INCORRETAMENTE"            
        return render_template("/html/entrar.html",erro = erro)