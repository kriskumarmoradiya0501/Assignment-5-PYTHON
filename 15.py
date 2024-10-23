# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:07:11 2024

@author: ADMIN
"""

def add_to_cart(cart, products, prod_id, quantity):
    if prod_id in products:
        product = products[prod_id]
        cart[prod_id] = {
            'Name': product['Name'],
            'Price': product['Price'],
            'Quantity': quantity,
            'ItemAmount': product['Price'] * quantity
        }
    return cart

def calculate_total(cart):
    return sum(item['ItemAmount'] for item in cart.values())

products = {'pid1': {'Name': 'Watch', 'Price': 400}, 'pid2': {'Name': 'Wallet', 'Price': 300}}
cart = {}

cart = add_to_cart(cart, products, 'pid1', 2)
print(cart)
total = calculate_total(cart)
print(total) 