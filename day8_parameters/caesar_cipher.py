alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encoded = []
def encrypt(str, shift):
    str = str.lower()
    for char in str:
        encoded.append((alph.index(char) + shift)%26)

shift = int(input("Enter a number to shift by: "))
encrypt('z',shift)
print(encoded)