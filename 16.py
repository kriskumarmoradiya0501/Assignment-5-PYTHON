# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:07:22 2024

@author: ADMIN
"""

def update_salary(employee_dict):
    for emp_id, details in employee_dict.items():
        increment = 0.10 if details['expe'] <= 2 else 0.15
        employee_dict[emp_id]['salary'] += employee_dict[emp_id]['salary'] * increment
    return employee_dict

employee_dict = {'emp1': {'name': 'Ramesh', 'salary': 15000, 'expe': 2}, 'emp2': {'name': 'Suresh', 'salary': 22000, 'expe': 3}}
employee_dict = update_salary(employee_dict)
print(employee_dict)