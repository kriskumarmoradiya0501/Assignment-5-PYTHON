# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:07:47 2024

@author: ADMIN
"""

def update_fitness(fitness_tracker, user_id, name, activity, duration):
    if user_id not in fitness_tracker:
        fitness_tracker[user_id] = {'name': name, 'activities': {}}
    if activity in fitness_tracker[user_id]['activities']:
        fitness_tracker[user_id]['activities'][activity] += duration
    else:
        fitness_tracker[user_id]['activities'][activity] = duration
    return fitness_tracker


fitness_tracker = {1: {'name': 'Eve', 'activities': {'running': 30, 'cycling': 60}}}

fitness_tracker = update_fitness(fitness_tracker, 2, 'Frank', 'swimming', 45)
print(fitness_tracker)