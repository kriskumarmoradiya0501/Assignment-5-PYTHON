# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:07:56 2024

@author: ADMIN
"""

def rent_vehicle(vehicles, user, user_id, vehicle_id, hours):
    if vehicles[vehicle_id]['available']:
        vehicles[vehicle_id]['available'] = False
        if user_id not in user:
            user[user_id] = []
        user[user_id].append({'vehicleid': vehicle_id, 'Status': 'Rent', 'hour': hours})
    return vehicles, user

def return_vehicle(vehicles, user, user_id, vehicle_id):
    for record in user[user_id]:
        if record['vehicleid'] == vehicle_id and record['Status'] == 'Rent':
            vehicles[vehicle_id]['available'] = True
            record['Status'] = 'Return'
    return vehicles, user

def calculate_bill(user, user_id, vehicles):
    return sum(record['hour'] * vehicles[record['vehicleid']]['rate'] for record in user[user_id])

vehicles = {101: {'type': 'Car', 'available': True, 'rate': 50}, 102: {'type': 'Bike', 'available': False, 'rate': 15}}
user = {}

vehicles, user = rent_vehicle(vehicles, user, 1, 101, 5)
print(user) 
vehicles, user = return_vehicle(vehicles, user, 1, 101)
print(vehicles[101]['available'])  
bill = calculate_bill(user, 1, vehicles)
print(bill) 