alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt():
    encoded = []
    str = input("What message would you like to encrypt?: ").lower()
    shift = int(input("Enter a number to shift by: "))
    for char in str:
        encoded.append(alph[(alph.index(char) + shift)%26])
    print("The coded message is:")
    print(''.join(encoded))

def decrypt():
    decoded = []
    str = input("What message would you like to decrypt?: ").lower()
    shift = int(input("What is the decryption number?: "))
    for char in str:
        decoded.append(alph[(alph.index(char) - shift)%26])
    print("The decoded message is:")
    print(''.join(decoded))

user_choice = input("Would you like to encrypt or decrypt a message?: ")

if user_choice == "encrypt":
    encrypt()
elif user_choice == "decrypt":
    decrypt()
else:
    "Sorry, I don't recognize that command"



