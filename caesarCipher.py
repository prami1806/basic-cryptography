# Caesar Cipher

import pyperclip
# The string to be encrypted/decrypted
message=input('Enter message:')

# The encryption/decryption key
key=int(input('Enter key:'))

# Whether the program encrypts or decrypts
mode=input('Enter \'encrypt\' to encrypt, \'decrypt\' to decrypt:')

# Every possible symbol that can be encrypted
SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted/decrypted form of the message
translated=''
for symbol in message:
    # symbol must be in SYMBOLS
    if symbol in SYMBOLS:
        symbolIndex=SYMBOLS.find(symbol)

        # Perform encryption/decryption
        if mode=='encrypt':
            translatedIndex=symbolIndex+key
        elif mode=='decrypt':
            translatedIndex=symbolIndex-key

        # Handle wraparound, if needed
        if translatedIndex>=len(SYMBOLS):
            translatedIndex=translatedIndex-len(SYMBOLS)
        elif translatedIndex<0:
            translatedIndex=translatedIndex+len(SYMBOLS)

        translated=translated+SYMBOLS[translatedIndex]
    else:
        # if not the case, append symbol without encrypting/decrypting
        translated=translated+symbol

# Output translated string
print(translated)
pyperclip.copy(translated)
