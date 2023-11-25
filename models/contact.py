from utils.db import db


class Contacts(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(120))

    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone
