from ecies import encrypt
import binascii

# Read in from our text file, convert from hex to a byte
with open('public.txt') as f:
    for line in f:
      pk_hex = binascii.unhexlify(''.join(line.split()))

# Test string:
data = b'this is a test'

# Encrypt the test string and then write out to a file as hex
encryptedMessage = encrypt(pk_hex, data)
with open('encrypted.txt', 'wb') as f:
    f.write(binascii.hexlify(encryptedMessage))
  
print("encrypted message!")
