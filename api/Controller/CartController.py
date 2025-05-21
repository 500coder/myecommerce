from database import db
from Models.CartModel import Cart
from datetime import datetime, timezone
from flask import json, jsonify

def run_initial_cart(app):
    with app.app_context():
        now = datetime.now(timezone.utc)
        cart_products = "[]"
        # cart_products = """
        # [
        #  {
        #         "unitPrice": "123.45",
        #         "id": 1,
        #         "quantity": 1,
        #         "title": "Caneca de Ceramica",
        #         "thumbnailUrl": "https://placehold.co/100"
        #     },
        #     {
        #         "unitPrice": "123.45",
        #         "id": 2,
        #         "quantity": 1,
        #         "title": "Caneca Aluminio",
        #         "thumbnailUrl": "https://placehold.co/100"
        #     },
        #     {
        #         "unitPrice": "123.45",
        #         "id": 3,
        #         "quantity": 1,
        #         "title": "Caneca Barro",
        #         "thumbnailUrl": "https://placehold.co/100"
        #     }           
        # ]    
        # """

        cart = Cart(code="fixed-cart-code", content=cart_products, created_at=now, updated_at=now)

        db.session.add(cart)
        db.session.commit()

def update_cart(payload, cart_code):
    Cart.query.filter(Cart.code ==cart_code).update({
        Cart.content: json.dumps(payload), Cart.updated_at: datetime.now(timezone.utc)}, synchronize_session=False
    )
    db.session.commit()

    return jsonify(Cart.query.filter(Cart.code ==cart_code).one().serialized)

def get_by_code(cart_code):
    return Cart.query.filter(Cart.code ==cart_code).one()
    