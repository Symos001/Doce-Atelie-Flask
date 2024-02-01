import click
from flask import Flask ,render_template, request, url_for
from app.views.login import login_page
from app.views.Produtos import products_page
from app.views.home import home_page
from flask.cli import FlaskGroup
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#Configs
app= Flask(__name__, static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///storage.db'
db=SQLAlchemy(app)
app.config['SECRET_KEY'] = 'secret'

cli =FlaskGroup(app)
migrate = Migrate(app,db)
migrate.init_app(app,db)


#Apps
app.register_blueprint(home_page)
app.register_blueprint(login_page)
app.register_blueprint(products_page)
