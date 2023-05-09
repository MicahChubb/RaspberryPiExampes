import generateKeys, decrypt, encrypt

while True:
    print('\nChoose what you want to do:\n1: Generate new keys\n2: Encrypt a message\n3: Decrypt the message\n4: Exit')
    command = input()
    if(command == '1'):
        generateKeys.makeKeys()
    elif(command == '2'):
        print('Type what you want to encrypt:')
        message = input()
        if(message == ''):
            message = 'You should have chosen a message!!'
        encrypt.encryptMessage(message)
    elif(command == '3'):
        decrypt.decryptMessage()
    elif(command == '4'):
        break
    else:
        print('Not an expected input, try again!')
