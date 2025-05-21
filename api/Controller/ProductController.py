from database import db
from Models.ProductsModel import Product

def run_products(app):

    with app.app_context():
      
        if Product.query.count() == 0:
            product1 = Product(
                title="Caneca Azul", 
                amount=123.45, 
                installments=3, 
                installments_fee=False)
            product2 = Product(
                title="Caneca Vermelha", 
                amount=100.23, 
                installments=4, 
                installments_fee=True)
            product3 = Product(
                title="Caneca Amarela", 
                amount=145.20, 
                installments=6, 
                installments_fee=True,)
            product4 = Product(
                title="Caneca Arco-Íris", 
                amount=80.34, 
                installments=3, 
                installments_fee=False)
            product5 = Product(
                title="Caneca Roxa", 
                amount=90.12, 
                installments=4, 
                installments_fee=True)
            product6 = Product(
                title="Caneca Preta", 
                amount=74.78, 
                installments=6, 
                installments_fee=True)

            db.session.add_all([product1, product2, product3, product4, product5, product6])
            db.session.commit()
