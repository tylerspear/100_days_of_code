def checker(num):
    is_prime = True
    for i in range(2, num):
        if num%i == 0:
            is_prime = False
            return is_prime
    return is_prime
n = int(input("Input a number: "))
print(checker(n))