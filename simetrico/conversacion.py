from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Alice
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(b"Hola Bob")

# Bob
cipher_bob = AES.new(key, AES.MODE_EAX, nonce=nonce)
msg = cipher_bob.decrypt_and_verify(ciphertext, tag)
print(msg.decode())
