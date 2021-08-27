"""
author:sachin
date:14/8/20201
Purpose: Practise
"""
import random
def user_guess_is_int():
    while True:
        try:
            user=int(input("enter a number\n"))
        except:
            print("please enter a number ")
        else:
            return user
def guess(a,b):
    random_number=random.randint(a,b)
    user=input("Enter your name \n")
    print("Random number is genrated")
    user_guess=None
    user_count=0
    while user_guess!=random_number:
        user_guess=user_guess_is_int()
        user_count +=1
        if user_guess<a or user_guess>b:
            print("nuber enter is out of range ")
            continue
        if user_guess>random_number:
            print(f"enter a smaller number than {user_guess} ")
        elif user_guess<random_number:
            print(f"Enter a larger nuber than{user_guess} ")
        else:
            print(f"Congraltulation {user} you guessed it correctly it was {random_number} in {user_count} guesses")
            return [user,user_count]

try:

    n1=int(input("Enter the number 1 of the range "))
    n2=int(input("Enter the number 2 of the range "))
except:
    print("Enter a number and number must not contain alphabet ")
    exit()
if n1<0 or n2<0:
    print("number must be positive")
    exit()
player1=guess(n1,n2)
player2=guess(n1,n2)

if player1[1]<player2[1]:
    print(f"{player1[0]} is the winner because he guess the number in {player1[1]} guess whereas {player2[0]} take{player2[1]} guess")
elif player1[1]>player2[1]:
    print(f"{player2[0]} is the winner because he guess the number in {player2[1]} guess whereas {player1[0]} take{player1[1]} guess")
else:
    print(f"{player1[0]} and {player2[0]} tie the match with {player1[1]} guess")