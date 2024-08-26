"""
Author: Aashir Aman Baik
Date: August 26, 2024
Description: This script implements a simple Rock-Paper-Scissors game where the computer randomly chooses a move, and the player competes against it.
"""

import random

print("Welcome to the classic Rock Paper Scissors game!!!!!")
print("To select \nsciccors-(s) \nrock-(r) \npaper(p) ")
user=input("Enter your choice: ")
moves=('r','p','s')
comp_move=random.choice(moves)
if user==comp_move:
    print("You are at draw ")
elif (user=='r' and comp_move=='p') or (user=='p' and comp_move=='s') or (user=='s' and comp_move=='r'):
    print("\nComputer wins.....\nYou lost\nBetter luck next time")
else:
    print("\nComgratulations..\nYou win!!!!!")

print(f"Computer's choice: {comp_move}")
print(f"Your move: {user}")
