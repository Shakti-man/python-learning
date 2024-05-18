import random
print("what to do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors")
x=int(input())
y = random.randint(0,2)
if x>2 or x<0:
    print("\ninvalid input \n")
elif x==0:
    print('''    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''                 )
elif x==1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

elif x==2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
if y==0:
    print("computer choose \n\n")
    print('''    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''                 )
elif y==1:
    print("computer choose \n\n")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

else:
    print("computer choose \n\n")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
if x==y:
    print("its a draw")
elif x==0 and y==2:
    print ("you won")
elif x==1 and y==0:
    print("you won")
elif x==2 and y==1:
    print("you won")
else:
    print("You lost")
