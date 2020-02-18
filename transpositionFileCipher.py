# Transposition Cipher Encrypt/Decrypt File

import time,os,sys,transpositionEncrypt as te,transpositionDecrypt as td

def main():
    inputFilename='frankenstein.txt'
    outputFilename='frankenstein.encrypted.txt'
    myKey=10
    myMode='encrypt' # Set to 'encrypt' or 'decrypt'.

    # If the input file does not exist, the program terminates
    if not os.path.exists(inputFilename):
        print('The file %s does not exist.Quitting...'%(inputFilename))

    # If the output file already exists, give user a chance to quit
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?'
              %(outputFilename))
        response=input('>')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file
    fileObj=open(inputFilename)
    content=fileObj.read()
    fileObj.close()

    print('%sing...'%(myMode.title()))

    # Measure how long the encryption/decryption takes
    startTime=time.time()
    if myMode=='encrypt':
        translated=te.encryptMessage(myKey,content)
    elif myMode=='decrypt':
        translated=td.decryptMessage(myKey,content)
    totalTime=round(time.time()-startTime,2)
    print('%sion time: %s seconds'%(myMode.title(),totalTime))

    # Write out the translated message to the output file
    outputFileObj=open(outputFilename,'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).'%(myMode,inputFilename,len(content)))
    print('%sed file is %s.'%(myMode.title(),outputFilename))

# If program is run instead of imported as a module, call main()
if __name__=='__main__':
    main()
    
