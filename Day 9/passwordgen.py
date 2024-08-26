"""
Author: Aashir Aman Baik
Description: This script implements a simple password generator.
"""

import string
import random

req=[]
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
special_char=string.punctuation

print("Welcome to THE PASSWORD GENERATOR!!!")
len=int(input("Enter the length for the passsword: "))

low=input("Include lowercase letters? (y/n): ").lower()=='y'
upp=input("Include uppercase letters? (y/n): ").lower()=='y'
dig=input("Include digits? (y/n): ").lower()=='y'
spl_chr=input("Include special characters? (y/n): ").lower()=='y'

char_pool=""
if low:
    char_pool+=lower
if upp:
    char_pool+=upper
if dig:
    char_pool+=digits
if spl_chr:
    char_pool+=special_char

if not char_pool:
    print("Select atleast one character set!")
    exit()

password=''.join(random.choices(char_pool,k=len))
print(f"Generated password: {password}")