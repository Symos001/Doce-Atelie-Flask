from flask import Flask ,render_template, request
from random import randint 

app= Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    variavel= "Game: adivinhe o número de 0 a 2 00:"
    
    if request.method=="GET":
        return render_template("/html/home.html", variavel=variavel)
    else:  
        comp = 0
        comp= randint(1,200) 
        user = int(request.form.get("name"))
        
        if user==comp :
            return "<h1>Você acertou!!</h1>"
        else:
            return "<h2>Você errou tente novamente</h2>"



    
@app.route("/<string:nome>")
def error(nome):
    return render_template("/html/erro.html", name_page=nome)


if __name__=="__main__":
    app.run(debug = True)

