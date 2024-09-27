from flask import Blueprint, render_template
from models.model import Pessoa

blueprintrota = Blueprint('blueprintrota', __name__)

JoaoV = Pessoa('Joao Vitor Santos',10)

@blueprintrota.route('/')
def index():
    return render_template('index.html', JoaoV=JoaoV)