from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

message = b"Documento importante"
key = RSA.import_key(open("asimetrico/privada.pem").read(), passphrase="clave123")
h = SHA256.new(message)
signature = pkcs1_15.new(key).sign(h)

pub_key = RSA.import_key(open("asimetrico/publica.pem").read())
pkcs1_15.new(pub_key).verify(h, signature)
print("Firma verificada correctamente.")
