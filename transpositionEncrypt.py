# Transposition Cipher Encryption

import pyperclip

def main():
    myMessage='Common sense is not so common.'
    myKey=8

    ciphertext=encryptMessage(myKey,myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted messages
    print(ciphertext+'|')

    # Copy the encrypted string in ciphertext to the clipboard
    pyperclip.copy(ciphertext)


def encryptMessage(key,message):
    # Each string in ciphertext represents a column in the grid
    ciphertext=['']*key
    # Loop through each column in ciphertext
    for column in range(key):
        currentIndex=column

        # Keep looping until currentIndex goes past the message length
        while currentIndex<len(message):
            # Place the character at currentIndex in the message at the
            # end of the current column in the ciphertext list:
            ciphertext[column]+=message[currentIndex]

            # Move currentIndex over
            currentIndex+=key

    # Convert the ciphertext list into a single string value and return it
    return ''.join(ciphertext)

# If program is run instead of imported as a module call main()
if __name__=='__main__':
    main()
