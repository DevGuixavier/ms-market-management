from flask import Blueprint

# Importa os blueprints das rotas
from .sellers import bp as sellers_bp
from .products import bp as products_bp
from .sales import bp as sales_bp

# Registra os blueprints
def register_blueprints(app):
    app.register_blueprint(sellers_bp, url_prefix='/sellers')
    app.register_blueprint(products_bp, url_prefix='/products')
    app.register_blueprint(sales_bp, url_prefix='/sales')
