# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:07:37 2024

@author: ADMIN
"""

def add_order(order_book, menu, table_id, food_item, quantity):
    if food_item in menu and menu[food_item]['available']:
        if table_id not in order_book:
            order_book[table_id] = []
        order_book[table_id].append({'fooditem': food_item, 'quantity': quantity})
    return order_book

def calculate_total_bill(order_book, menu):
    total_bill = 0
    for orders in order_book.values():
        for order in orders:
            total_bill += menu[order['fooditem']]['price'] * order['quantity']
    return total_bill

menu = {'burger': {'price': 50, 'available': True}, 'pizza': {'price': 150, 'available': False}, 'pasta': {'price': 100, 'available': True}}
order_book = {}

order_book = add_order(order_book, menu, 1, 'burger', 2)
order_book = add_order(order_book, menu, 1, 'pasta', 1)
print(order_book)  
total_bill = calculate_total_bill(order_book, menu)
print(total_bill)  