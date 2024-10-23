# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:05:20 2024

@author: ADMIN
"""

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  
print(is_palindrome("hello"))  