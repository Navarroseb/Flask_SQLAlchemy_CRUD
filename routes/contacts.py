from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__)


@contacts.route('/')  # url /
def home():  # función de la url /
    return render_template('index.html')


@contacts.route('/new')
def add_contact():
    return "Agregar contactos"

@contacts.route('/about')  
def about():  
    return render_template('about.html')


@contacts.route('/update')
def update():
    return "Updating a contact"


@contacts.route('/delete')
def delete():
    return "Deleting contact"