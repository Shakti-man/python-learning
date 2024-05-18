print('''         `>.___    o-.--.-o    ___,<'                                
               /    `.   / ,, \   .'    \                                 
              {       `.; ,__, ;.'       }                                
               `._      }`.__.'{      _.'                                 
                  `,=."'        `".=,'                                    
                 .'   /`-.____.-'_   `,                                   
                 \_.';`-.______.-':`._/                                   
                     `+-.______.-''                                       
                       `-.____.-'                                         
                        /  ||  \                                         
                       ;   ;;   ;                                        
                       `-./  \.-'       ''')
print("welcome to treasure island. \n your mission is to find the treasure.")
chose1=input('''you are at cross road, where you want to go? type "left" or "right"\n ''')
if(chose1.lower()=="right"):
    print("fall into a hole. \nGame over.")
elif(chose1.lower()=="left"):
    chose2=input ('''you came to a lake. there is an island in the middle of the lake. type "wait" to wait for a boat. type "swim" to swim across.\n''')
    if(chose2.lower()=="swim"):
        print(''' you were attacked by trout. \n GAME OVER.\n''')
    elif(chose2.lower()=="wait"):
        chose3=input ('''you arrive at island unharmed. there is a house with 3doors. one red, one yellow and one blue.  which colour do you choose?\n''')
        if(chose3.lower()=="red"):
            print("burned by fire. \nGAME OVER.")
        elif(chose3.lower()=="blue"):
            print("eaten by beats. \nGAME OVER.")
        else:
            print("you win!")
else:
    print("Wrong input")