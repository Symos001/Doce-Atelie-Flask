from flask import Flask ,render_template, request, url_for
from views.login import login_page
from views.Produtos import products_page
from views.home import home_page
from views.error import error_page
from flask_sqlalchemy import SQLAlchemy

#
app= Flask(__name__, static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///storage.db'
db=SQLAlchemy(app)
app.config['SECRET_KEY'] = 'secret'
#Apps
app.register_blueprint(home_page)
app.register_blueprint(login_page)
app.register_blueprint(products_page)
app.register_blueprint(error_page)


if __name__=="__main__":
    app.run(debug = True, port=5000)

