from Crypto.Hash import SHA512
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA

message = b"Mensaje con SHA-512"
key = RSA.import_key(open("asimetrico/privada.pem").read(), passphrase="clave123")
h = SHA512.new(message)
signature = pkcs1_15.new(key).sign(h)

# Verificar
pub = RSA.import_key(open("asimetrico/publica.pem").read())
pkcs1_15.new(pub).verify(h, signature)
print("Verificado con SHA-512")
