from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

msg = b"Mensaje secreto"
key = RSA.import_key(open("asimetrico/publica.pem").read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(msg)

# Descifrado
priv_key = RSA.import_key(open("asimetrico/privada.pem").read(), passphrase="clave123")
decipher = PKCS1_OAEP.new(priv_key)
plain = decipher.decrypt(ciphertext)
print(plain.decode())
