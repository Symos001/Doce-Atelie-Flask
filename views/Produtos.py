from flask import Blueprint , render_template

products_page= Blueprint('products',__name__)


@products_page.route("/Produtos")
def produtos():
    return render_template("/html/produtos.html")