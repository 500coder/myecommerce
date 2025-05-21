from database import db
from Models.OrdersModel import Orders
from Controller.CartController import get_by_code
from datetime import datetime, timezone
from decimal import *

def create_from(cart_code):

    with db.session.begin():
        cart = get_by_code(cart_code)
        now = datetime.now(timezone.utc)
        order = Orders(products=cart.content, amount=sum_total(cart), created_at=now, updated_at=now, status='DONE')
    
        db.session.add(order)
        db.session.commit()

        return order


def sum_total(cart):
    total = 0
    for p in cart.serialized['products']:
        total = total + (Decimal(p['unitPrice']) * int(p['quantity']))
    return total