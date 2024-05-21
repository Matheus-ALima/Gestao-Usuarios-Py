from flask import Blueprint, render_template

#inicia o blueprint
home_route = Blueprint('home', __name__)

#definindo as rotas
@home_route.route('/')
def home():
    return render_template('index.html')