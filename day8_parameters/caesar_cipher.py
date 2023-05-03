alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt():
    encoded = []
    str = input("What message would you like to encrypt?: ").lower()
    shift = int(input("Enter a number to shift by: "))
    for char in str:
        encoded.append(alph[(alph.index(char) + shift)%26])
    print(''.join(encoded))


encrypt()