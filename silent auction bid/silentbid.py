from logo import *
import os
print(logo)
print("Welcome to the secret auction program")
dit={}
def highest_bid(**kwargs):
    highest_amount=0
    winner=""
    for key,value in kwargs.items():
        value =dit[key] 
        if value> highest_amount:
            highest_amount = value
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_amount}")

continue_bid=True
while continue_bid==True:
        bid_name =input("What is you name?: ")
        bid_amount=int(input("What's your bid?: $"))
        other_bid=input("Are there any other bidders? Type 'yes' or 'no'.")
        dit[bid_name]=bid_amount
        if other_bid=="yes":
            continue_bid=True
            os.system('cls')
        elif other_bid=="no":
            continue_bid=False
            print(dit)
            highest_bid(**dit)