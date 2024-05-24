import os
from logo import logo

def operations(x,operator,y):
    if operator== "-":
        return float(x-y)
    elif operator=="+":
        return float(x+y)
    elif operator=="/":
        return float(x/y)
    elif operator=="*":
        return float(x*y)
def cal():
    print(logo)
    num1 =float(input("What's the first number: "))
    operator =input('''+
-
/
*
Pick an operation: ''')
    num2=float(input("What's the second number: "))
    output=operations(num1,operator,num2)
    print(f"{num1} {operator} {num2} = {output}")
    again=input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation:")
    should_continue=True
    while should_continue:
        if again=="y":
            operator=input("Pick an operation: ")
            num3=float(input("What's the next number: "))
            output2=operations(output,operator,num3)
            print(output)
            print(f"{output} {operator} {num3} = {output2}")
            output=output2
            again=input(f"Type 'y' to continue calculating with {output2}, or type 'n' to start a new calculation:")
        else:
            os.system('cls||clear')
            cal()
cal()