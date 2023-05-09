from ecies.utils import generate_key
import binascii

def makeKeys():
  # Create the key pair, store it into variables
  eth_k = generate_key()
  sk_bytes = eth_k.secret  # hex string
  pk_bytes = eth_k.public_key.format(True)  # hex string

  # Encode the byte to a hex value and write out to different files
  with open('textfiles/secret.txt', 'wb') as f:
    f.write(binascii.hexlify(sk_bytes))
  with open('textfiles/public.txt', 'wb') as f:
    f.write(binascii.hexlify(pk_bytes))

  print("generated keys!")

if __name__ == "__main__":
  makeKeys()
