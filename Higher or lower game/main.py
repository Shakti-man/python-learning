from data import *
from logo import *
import random
import os
should_continue=True
shuffled_list = sorted(data, key=lambda x : random.random())
while should_continue==True:
    print(logo)
    count_score=0
    for i in range(0,len(shuffled_list)):
        print(f"Compare A: {shuffled_list[i]['name']},{data[i]['description']},{shuffled_list[i]['country']}")
        print(vs)
        print(f"Against B: {shuffled_list[i+1]['name']},{shuffled_list[i+1]['description']},{shuffled_list[i+1]['country']}")
        more=input("Who has more followers? Type 'A' or 'B': ")
        if more=="A":
            if shuffled_list[i]['follower_count']>shuffled_list[i+1]['follower_count']:
                count_score+=1
            else:
                os.system('cls||clear')
                print(logo)
                print(f"Sorry, that's wrong. Final score {count_score}")
                should_continue=False
                break
            os.system('cls||clear')
            print(logo)
            print(f"You're Right! Current score: {count_score}")
        elif more=="B":
            if shuffled_list[i]['follower_count']<shuffled_list[i+1]['follower_count']:
                count_score+=1
            else:
                os.system('cls||clear')
                print(logo)
                print(f"Sorry, that's wrong. Final score {count_score}")
                should_continue=False
                break
            os.system('cls||clear')
            print(logo)
            print(f"You're Right! Current score: {count_score}")
