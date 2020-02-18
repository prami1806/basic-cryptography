# Affine Cipher Hacker

import pyperclip,affineCipher,detectEnglish,cryptomath

SILENT_MODE=False

def main():
    myMessage=""""5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RNQ"-5!1RQP36ARu"""

    hackedMessage=hackAffine(myMessage)

    if hackedMessage!=None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')

def hackAffine(message):
    print('Hacking...')
    
    # Brute force by looping through every possible key
    for key in range(len(affineCipher.SYMBOLS)**2):
        keyA=affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA,len(affineCipher.SYMBOLS))!=1:
            continue
        decryptedText=affineCipher.decryptMessage(key,message)
        if not SILENT_MODE:
            print('Tried Key %s..(%s)'%(key,decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            # Check with user if the decrypted key has been found
            print()
            print('Possible encryption hack:')
            print('Key: %s'%(key))
            print('Decrypted message: '+decryptedText[:200])
            print()
            print('Enter D for (D)one, or just press Enter to continue hacking:')
            response=input('>')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

# If program is run and not imported as a module run main
if __name__=='__main__':
    main()

