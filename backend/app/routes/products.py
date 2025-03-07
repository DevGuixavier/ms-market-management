from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import Product, db

bp = Blueprint('products', __name__)

@bp.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    new_product = Product(nome=data['nome'], preco=data['preco'], quantidade=data['quantidade'], status=data['status'], imagem=data['imagem'], seller_id=data['seller_id'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created successfully!"}), 201

@bp.route('/products', methods=['GET'])
@jwt_required()
def list_products():
    products = Product.query.all()
    return jsonify([product.as_dict() for product in products]), 200

@bp.route('/products/<int:id>', methods=['PUT'])
@jwt_required()
def update_product(id):
    data = request.get_json()
    product = Product.query.get_or_404(id)
    product.nome = data['nome']
    product.preco = data['preco']
    product.quantidade = data['quantidade']
    product.status = data['status']
    product.imagem = data['imagem']
    db.session.commit()
    return jsonify({"message": "Product updated successfully!"}), 200

@bp.route('/products/<int:id>', methods=['GET'])
@jwt_required()
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.as_dict()), 200

@bp.route('/products/<int:id>/inactivate', methods=['PATCH'])
@jwt_required()
def inactivate_product(id):
    product = Product.query.get_or_404(id)
    product.status = 'Inativo'
    db.session.commit()
    return jsonify({"message": "Product inactivated successfully!"}), 200
