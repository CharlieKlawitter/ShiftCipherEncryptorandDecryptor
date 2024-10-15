
plaintext = input("What message would you like to encrypt? ")
key = int(input("What key would you like to use to encrypt? "))

#Defining the Shift Cipher Function
def shift(plaintext, key):
    ciphertext = '' #Initialize empty string
    for char in plaintext:
        #Encrypt Uppercase Letters
        if char.isupper():
          ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        #Encrypt Lowercase Letters
        elif char.islower():
          ciphertext += chr((ord(char) + key - 97) % 26 + 97)
        #Leave characters and numbers the way they are
        else:
            ciphertext += char
        #Convert all encrypted text to uppercase
    ciphertext = ciphertext.upper()

    return ciphertext
        #Set ciphertext to equal the function
ciphertext = shift(plaintext, key)

#Output ciphertext
print(f"Your encrypted message is {ciphertext}")

