# Online Python - IDE, Editor, Compiler, Interpreter
Math = True
#Functions for add, subtract, multiply and divide
def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2
    
def divide(n1, n2):
    return n1 / n2
    
#Four functions in a dictionary as the values with the keys 
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    Math = True
    num1 = float(input("What is the first number? "))
    
    while Math == True:
        for symbol in operations:
            print(symbol)
        op = input("Pick an operaion: ")
        num2 = float(input("What is the second number? "))
        answer = operations[op](num1,num2)
        print(f"{num1} {op} {num2} = {answer}")
        
        choice = input(f"Continue calculating {answer}? Y or N: ")
        
        if choice == "y":
            num1 = answer
        else:
            print (f"The answer is {answer}")
            Math = False
            print("\n" * 20)
            calculator()

calculator()
