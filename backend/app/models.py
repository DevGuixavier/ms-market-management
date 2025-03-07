from . import db
from datetime import datetime

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    cnpj = db.Column(db.String(18), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    celular = db.Column(db.String(15), nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    status = db.Column(db.String(10), default='Inativo')

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    imagem = db.Column(db.String(256), nullable=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'), nullable=False)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)
