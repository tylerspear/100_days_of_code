user_int1 = int(input("What's the 1st number?: "))
user_operation = input("Pick an operation: (+ - * / ^) ")
user_int2 = int(input("What's the 2nd number?: "))



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def power(n1, n2):
    return n1**n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power
}

print(operations[user_operation](user_int1, user_int2))
