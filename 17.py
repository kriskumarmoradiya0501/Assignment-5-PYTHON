# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:07:29 2024

@author: ADMIN
"""

def voting_system(candidate_votes, voter_set, voter_name, candidate_name):
    if voter_name in voter_set:
        return "Already voted"
    if candidate_name in candidate_votes:
        candidate_votes[candidate_name] += 1
        voter_set.add(voter_name)
    return candidate_votes, voter_set

candidate_votes = {'party1': 0, 'party2': 0, 'party3': 0}
voter_set = set()

candidate_votes, voter_set = voting_system(candidate_votes, voter_set, 'John', 'party1')
print(candidate_votes)  
print(voter_set) 