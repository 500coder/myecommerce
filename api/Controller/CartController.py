from ..Models import db
from ..Models.CartModel import Cart
from datetime import datetime, timezone
from flask import Blueprint, json, jsonify, request

cart_api = Blueprint('cart', __name__)

@cart_api.route("/cart", methods=['GET'])
@cart_api.route("/cart/<cart_code>", methods=['GET'])
def get(cart_code=None):
    """ List all carts or that one which cart_code is matched """

    if cart_code is not None:
        cart = Cart.query.filter(
            Cart.code == cart_code
        ).one()
    
        return jsonify(cart.serialized)
    
    else:
        carts = Cart.query.all()
        print('carts: ', carts)
        return jsonify({'carts': c.serialized for c in carts})
    
@cart_api.route("/cart/<cart_code>", methods=['PUT'])
def put(cart_code=None):
    """ Update cart from payloaded products list"""
    payload = request.get_json()
    #if(payload):
    return update_cart(payload, cart_code)
    #else:
    #    return jsonify({'message': 'Erro - Payload nulo'}), 402 


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
    