# Transposition Cipher Decryption

import math,pyperclip

def main():
    myMessage='Cenoonommstmme oo snnio. s s c'
    myKey=8

    plaintext=decryptMessage(myKey,myMessage)

    # Print with a | after it in case there are spaces at the
    # end of the decrypted message
    print(plaintext+'|')

    pyperclip.copy(plaintext)

def decryptMessage(key,message):
    # The transposition decrypt function will simulate the 'columns' and
    # 'rows' of the grid that the plaintext is written on by just using a list
    # of strings.

    # The number of 'columns' in our transposition grid
    noOfColumns=int(math.ceil(len(message)/float(key)))
    # The number of 'rows' in our grid
    noOfRows=key
    # Then no of extra spaces in the last 'column' of the grid
    noOfExtra=(noOfColumns*noOfRows)-len(message)

    # Each string in plaintext represent a column in the grid
    plaintext=['']*noOfColumns

    # The column and row variables point to where in the grid the next
    # character in the message will go
    column=0
    row=0

    for symbol in message:
        plaintext[column]+=symbol
        column+=1 # Point to the next column

        # If there are no more columns or we are at a blank space,
        # go back to the first column of the next row
        if (column==noOfColumns) or (column==noOfColumns-1 and
                                     row>=noOfRows-noOfExtra):
            column=0
            row+=1

    return ''.join(plaintext)

# If program is run instead of imported as a module, call main()
if __name__=='__main__':
    main()
