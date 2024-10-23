# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:07:00 2024

@author: ADMIN
"""

def banking_operations(accounts, transaction_dict, acc_id, operation, amount):
    if operation == 'deposit':
        accounts[acc_id]['current_balance'] += amount
        transaction_dict[acc_id].append([amount, 'd', accounts[acc_id]['current_balance']])
    elif operation == 'withdraw':
        if accounts[acc_id]['current_balance'] >= amount:
            accounts[acc_id]['current_balance'] -= amount
            transaction_dict[acc_id].append([amount, 'w', accounts[acc_id]['current_balance']])
    return accounts, transaction_dict

accounts = {902: {'name': 'Suresh', 'current_balance': 5000}, 904: {'name': 'Jayesh', 'current_balance': 15000}}
transaction_dict = {902: [[3000, 'd', 8000], [5000, 'w', 2000]]}

accounts, transaction_dict = banking_operations(accounts, transaction_dict, 902, 'deposit', 2000)
print(accounts)  
accounts, transaction_dict = banking_operations(accounts, transaction_dict, 902, 'withdraw', 1000)
print(transaction_dict)