from flask import Blueprint , render_template

home_page = Blueprint('home',__name__)


@home_page.route("/")
def index():
    return render_template("/html/home.html")
