import sys
import operator
import re

def addition(a, b):
    return float(a)+float(b) 

def substraction(a, b): 
    return float(a)-float(b)

def multiplication(a, b):
    return float(a)*float(b)

def divison(a, b):
    if b!=0:
        return float(a)/float(b)
    else:
        return "Cannot divide by zero"

def powerRaise(a, b):
    return float(a)**float(b)

def sqrtRoot(a):
    if a<0:
        return "Invalid Input"
    else:
        return a**0.5



def read_input(history):
    symbols=['+', '-', '*', '/', '^', "sqrt"]
    input1=input()
    expression=input1.split()
    if expression[0] in symbols:
        nr1=history[-1]
        operator1=expression[0]
        if operator1=="sqrt":
            nr2=0 
        else:
            nr2= float(expression[-1])
    else:
        nr1 = float(expression[0])
        operator1=expression[1]
        nr2= float(expression[-1])
    return nr1, operator1, nr2


def calculator():
    history=[] 
    while True:
        nr1, operator1, nr2=read_input(history)
        
        if operator1=="+":
            ans=addition(nr1, nr2)
        elif operator1=="-":
            ans=substraction(nr1, nr2)
        elif operator1=="*":
            ans=multiplication(nr1, nr2)
        elif operator1=="/":
            ans=divison(nr1, nr2)
        elif operator1=="^":
            ans=powerRaise(nr1, nr2)
        elif operator1=="sqrt":
            ans=sqrtRoot(nr1)
        history.append(ans)
        print("= "+str(ans))
    
if __name__ == "__main__":
    calculator()