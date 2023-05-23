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

def calculate(int1, int2, operation):
    return operations[operation](int1, int2)

continue_loop = True


user_int1 = int(input("What's the 1st number?: "))
user_operation = input("Pick an operation: (+ - * / ^) ")
user_int2 = int(input("What's the 2nd number?: "))
answer = calculate(user_int1, user_int2, user_operation)
print(answer)

while continue_loop:
    print(f"Type 'y' to continue calculating with {answer} or type 'n' to exit.")
    continue_calculate = input()
    if continue_calculate == 'y':
        user_operation = input("Pick an operation: (+ - * / ^) ")
        user_int2 = int(input("What's the 2nd number?: "))
        answer = calculate(answer, user_int2, user_operation)
        print(answer)
    else:
        calculate = False
        break