from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(1))
    value = db.Column(db.Numeric(2))
    qty = db.Column(db.Integer())

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    document = db.Column(db.Integer())

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sold_at = db.Column(db.DateTime())
    total = db.Column(db.Numeric(2))
    
    
