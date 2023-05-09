from ecies import encrypt
import binascii

def encryptMessage(data):
    # Read in from our text file, convert from hex to a byte
    with open('textfiles/public.txt') as f:
        for line in f:
            pk_hex = binascii.unhexlify(''.join(line.split()))

    # Encrypt the test string and then write out to a file as hex
    encryptedMessage = encrypt(pk_hex, data.encode("utf8"))
    with open('textfiles/encrypted.txt', 'wb') as f:
        f.write(binascii.hexlify(encryptedMessage))
    
    print("encrypted message!")

if __name__ == "__main__":
  encryptMessage('this is some test data')
