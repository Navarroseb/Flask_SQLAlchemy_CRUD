from flask import Blueprint

contacts = Blueprint('contacts', __name__)

@contacts.route('/')  # url /
def home():  # función de la url /
    return "Listado de contactos"
@contacts.route('/new')
def add_contact():
    return "Agregar contactos"