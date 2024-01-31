from flask import Blueprint , render_template

error_page= Blueprint('erro', __name__)

@error_page.route("/<string:nome>")
def error(nome):
    return render_template("/html/erro.html", name_page=nome)
