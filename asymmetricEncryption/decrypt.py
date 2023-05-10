from ecies import decrypt
import binascii

def decryptMessage():
  # Read in and un-hex our private key
  with open('textfiles/secret.txt') as f:
    for line in f:
      sk_bytes = binascii.unhexlify(''.join(line.split()))

  # Read in and un-hex our message
  with open('textfiles/encrypted.txt') as f:
    for line in f:
      data = binascii.unhexlify(''.join(line.split()))

  # Decrypt our message and write it out!
  decryptedMessage = decrypt(sk_bytes, data)
  print("Decrypted:", decryptedMessage.decode("utf8")) #The decode is to remove a b'text here' formatting

if __name__ == "__main__":
  decryptMessage()
