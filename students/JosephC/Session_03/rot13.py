#the string to be encrypted/decrypted
message = "Zntargvp sebz bhgfvqr arne pbeare"

#the encryption/decryption key
key = 13

# tells the program to encrypt or decrypt
mode = 'decrypt' #set to 'encrypt' or 'decrypt'

#every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#stores the encrypted/decrypted form of the message
translated = ''

#capitalize the string in message
message = message.upper()

# run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        #get the encrypted or decrypted number for this symbol
        num = LETTERS.find(symbol) #get the number of the symbol (we need this to slice the message)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
             num = num - key
        #handle the wrap-around if num is larger than the length of LETTERS or less than 0; 
        if num >= len(LETTERS):
            num = num-len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # add encrypted/decrypted number's symbol at the end the translated
        translated = translated + LETTERS[num]

    else:
        # just add the sumbol without encrypting/decrypting
        translated = translated + symbol

#print the encrypted/decrypted string to the screen
print(translated)
