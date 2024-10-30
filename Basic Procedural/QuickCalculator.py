def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2
    
def divide(n1, n2):
    return n1 / n2
    
def calculator(n1, n2, function):
    return function(n1,n2)

result1 = calculator(6, 2, add)
result2 = calculator(6, 2, subtract)
result3 = calculator(6, 2, multiply)
result4 = calculator(6, 2, divide)

print(result1)
print(result2)
print(result3)
print(result4)

