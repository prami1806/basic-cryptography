# Transposition Cipher Hacker

import pyperclip,detectEnglish,transpositionDecrypt as td

def main():
    myMessage="""AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""
    
    hackedMessage=hackTransposition(myMessage)

    if hackedMessage==None:
        print(' Failed to hack encryption. ')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)

def hackTransposition(message):
    print('Hacking...')

    # Brute-force by looping through every possible key:
    for key in range(1,len(message)):
        print('KEY %s..'%(key))

        decryptedText=td.decryptMessage(key,message)

        if detectEnglish.isEnglish(decryptedText):
            # Ask user if this is the correct decryption
            print()
            print('Possible encryption hack:')
            print('KEY %s: %s'%(key,decryptedText[:100]))
            print()
            print('Enter D if done, any other key to continue hacking:')
            response=input('>')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None

if __name__=='__main__':
    main()
