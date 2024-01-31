from flask import Blueprint,render_template,request
from models.forms import LoginForm

login_page = Blueprint('login', __name__)


@login_page.route("/login", methods=['GET','POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
      print(form.username.data)
      print(form.password.data)
   else:
      form.errors
   return render_template('/html/entrar.html', form=form)
