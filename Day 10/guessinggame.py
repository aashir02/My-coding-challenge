import random
count=0

real_num=random.randint(1,100)
print("Welcome to the number guessing game!!!")
print("The number you have to guess is between 1 and 100")
while True:
    guess=int(input("Enter your guess: "))
    if guess==real_num:
        print("Hurray!!!!.You have found the number ")
        print(f"You found the real number in {count} guesses")
        exit()
    elif guess<real_num:
        print("wrong answer.\nReal number is greater than your guess.Try again")
        count+=1
    elif guess>real_num:
        print("wrong answer.\nReal number is smaller than your guess.Try again")
        count+=1