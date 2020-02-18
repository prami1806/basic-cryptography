# Caesar Cipher Hacker

message=input('Enter message:')
SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key
for key in range(len(SYMBOLS)):
    # Clear previous iteration's value for translated
    translated=''

    # Loop through each symbol in message
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex=SYMBOLS.find(symbol)
            translatedIndex=symbolIndex-key

            # Handle wraparound
            if translatedIndex<0:
                translatedIndex=translatedIndex+len(SYMBOLS)

            # Append the decrypted symbol:
            translated=translated+SYMBOLS[translatedIndex]

        else:
            # Append symbol without decrypting
            translated=translated+symbol

    # Display every possible decryption
    print('KEY {}: {}'.format(key,translated))



