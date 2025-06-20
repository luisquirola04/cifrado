from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
#cifrado
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_GCM)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(b"Hola mundo")

# Descifrado
cipher_dec = AES.new(key, AES.MODE_GCM, nonce=nonce)
plaintext = cipher_dec.decrypt_and_verify(ciphertext, tag)
print(plaintext.decode())
