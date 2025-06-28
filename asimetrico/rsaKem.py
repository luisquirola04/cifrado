from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

# Alice
session_key = get_random_bytes(16)
rsa_pub = RSA.import_key(open("asimetrico/publica.pem").read())
cipher_rsa = PKCS1_OAEP.new(rsa_pub)
enc_session_key = cipher_rsa.encrypt(session_key)

aes = AES.new(session_key, AES.MODE_EAX)
nonce = aes.nonce
ciphertext, tag = aes.encrypt_and_digest(b"hola bob")

# Bob
rsa_priv = RSA.import_key(open("asimetrico/privada.pem").read(), passphrase="clave123")
dec_rsa = PKCS1_OAEP.new(rsa_priv)
session_key = dec_rsa.decrypt(enc_session_key)

aes_dec = AES.new(session_key, AES.MODE_EAX, nonce=nonce)
msg = aes_dec.decrypt_and_verify(ciphertext, tag)
print(msg.decode())
