from ecies import decrypt
import binascii

# Read in and un-hex our private key
with open('secret.txt') as f:
    for line in f:
      sk_bytes = binascii.unhexlify(''.join(line.split()))

# Read in and un-hex our message
with open('encrypted.txt') as f:
    for line in f:
      data = binascii.unhexlify(''.join(line.split()))

# Decrypt our message and write it out!
decryptedMessage = decrypt(sk_bytes, data)
print("Decrypted:", decryptedMessage)
