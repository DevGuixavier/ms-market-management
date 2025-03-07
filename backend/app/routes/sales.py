from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import Sale, Product, db

bp = Blueprint('sales', __name__)

@bp.route('/sales', methods=['POST'])
@jwt_required()
def create_sale():
    data = request.get_json()
    product = Product.query.get_or_404(data['produto_id'])
    if product.quantidade < data['quantidade']:
        return jsonify({"message": "Quantidade insuficiente em estoque"}), 400

    sale = Sale(produto_id=data['produto_id'], quantidade=data['quantidade'], preco=product.preco)
    product.quantidade -= data['quantidade']
    db.session.add(sale)
    db.session.commit()
    return jsonify({"message": "Sale created successfully!"}), 201
