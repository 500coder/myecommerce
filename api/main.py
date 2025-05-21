from flask import request, jsonify, json
from flask_cors import CORS
from Models.ProductsModel import Product
from Models.CartModel import Cart
from Controller.ResetMigrations import reset_migrations
from Controller.ProductController import run_products
from Controller.CartController import run_initial_cart, update_cart
from Controller.OrdersController import total_sum, create_from

from app import app

CORS(app)

@app.route("/")
def index():
    reset_migrations(app)
    run_products(app)
    run_initial_cart(app)
    return 'migrations done'
    

@app.route("/products", methods=['GET']) # requested by Product List with or without search params (query)
@app.route("/product/<id>", methods=['GET']) # requested by product detail page (id)
def get_products(id=None):
    args = request.args.to_dict()
    query = args.get("query")

    if(args.get("pageSize") and args.get("currentPage")):
        page_size = int(args.get("pageSize"))
        current_page = int(args.get("currentPage"))

    
    if(query is None and id is not None): # return product base on id, 
        
        product = Product.query.filter(Product.id==id).first()
        return jsonify(product.serialized) if product else jsonify({'error': 'Produto não encontrado'}), 404

    elif(query is None and id is None): # return all products
        
        all_products = Product.query

    elif(query is not None and id is None): # return products base on search params
        
        all_products = Product.query.filter(
            Product.title.ilike(f'%{query}%'))
    
    pagination = all_products.paginate(page=current_page, per_page=page_size, error_out=False)

    return jsonify({
        'query': query, 
        'pageSize': page_size, 
        'currentPage': current_page, 
        'totalItems': pagination.total, 
        'totalPages': pagination.pages, 
        'results': [p.serialized for p in pagination.items]
        })
    
   
@app.route("/cart", methods=['GET'])
@app.route("/cart/<cart_code>", methods=['GET'])
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
    
@app.route("/cart/<cart_code>", methods=['PUT'])
def put(cart_code=None):
    """ Update cart from payloaded products list"""
    payload = request.get_json()
    #if(payload):
    return update_cart(payload, cart_code)
    #else:
    #    return jsonify({'message': 'Erro - Payload nulo'}), 402 


@app.route("/order/", methods=['POST'])
def order():
    payload = request.get_json()
    cart_code = payload['cart_code']
    print("@app.route('/order/', methods=['POST'])", cart_code)
    order = create_from(cart_code)

    return jsonify(order.serialized)


@app.route("/order/<cart_code>", methods=['GET'])
def get_order():
    return
