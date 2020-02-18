# Transposition Cipher Test

import random,sys
import transpositionEncrypt as te
import transpositionDecrypt as td

def main():
    random.seed(42) # Set the random 'seed' to a static value

    for i in range(20): # Run, say 20 tests
        # Generate random messages to test

        # The message will have random length
        message='ABCDEFGHIJKLMNOPQRSTUVWXYZ'*random.randint(4,40)

        # Convert message string to a list to shuffle it
        message=list(message)
        random.shuffle(message)
        message=''.join(message) # Convert the list back to a string

        print('TEST {}:"{}..."'.format(i+1,message[:50]))

        # Check all possible keys for each message:
        for key in range(1,int(len(message)/2)):
            encrypted=te.encryptMessage(key,message)
            decrypted=td.decryptMessage(key,encrypted)

            # If decryption doesn't match the original message, display
            # an error message and quit
            if message!=decrypted:
                print('Mismatch with key {} and message {}'.format(key,message))
                print('Decrypted as: '+decrypted)
                sys.exit()

        print('Transposition cipher test passed')

# If program is run instead of imported as a module, call main()
if __name__ == '__main__':
    main()
