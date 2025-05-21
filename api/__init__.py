from flask import Flask
from flask_cors import CORS
from .Models import db, DATABASE_URL

from .Controller.ProductController import product_api, run_products
from .Controller.CartController import cart_api, run_initial_cart
from .Controller.OrdersController import order_api
from .Controller.ResetMigrations import reset_migrations


def create_app(config_file):
    
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    db.init_app(app)

    app.register_blueprint(product_api)
    app.register_blueprint(cart_api)
    app.register_blueprint(order_api)

    reset_migrations(app)
    run_products(app)
    run_initial_cart(app)
    
    CORS(app)

    return app