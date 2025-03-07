from flask import Blueprint, request, jsonify, current_app
from app.models import Seller, db
import bcrypt
from twilio.rest import Client

bp = Blueprint('sellers', __name__)

@bp.route('/sellers', methods=['POST'])
def create_seller():
    data = request.get_json()
    hashed_password = bcrypt.hashpw(data['senha'].encode('utf-8'), bcrypt.gensalt())
    new_seller = Seller(nome=data['nome'], cnpj=data['cnpj'], email=data['email'], celular=data['celular'], senha=hashed_password)
    db.session.add(new_seller)
    db.session.commit()
    
    # Envia o código de ativação via Twilio
    code = '1234'  # Gere um código dinâmico
    client = Client(current_app.config['TWILIO_ACCOUNT_SID'], current_app.config['TWILIO_AUTH_TOKEN'])
    message = client.messages.create(
        body=f"Seu código de ativação é: {code}",
        from_=current_app.config['TWILIO_PHONE_NUMBER'],
        to=new_seller.celular
    )
    
    return jsonify({"message": "Seller created successfully!"}), 201

@bp.route('/sellers/activate', methods=['POST'])
def activate_seller():
    data = request.get_json()
    seller = Seller.query.filter_by(celular=data['celular']).first()
    if seller and data['codigo'] == '1234':  # faz a verificação do código dinâmico
        seller.status = 'Ativo'
        db.session.commit()
        return jsonify({"message": "Seller activated successfully!"}), 200
    return jsonify({"message": "Invalid code or seller"}), 400
