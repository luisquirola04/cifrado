from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


with open("archivo.txt", "rb") as f:
    data = f.read()

key = RSA.import_key(open("privada.pem").read(), passphrase="clave123")
h = SHA256.new(data)
signature = pkcs1_15.new(key).sign(h)

with open("firma.sig", "wb") as f: f.write(signature)

# Verificación
pub = RSA.import_key(open("publica.pem").read())
h2 = SHA256.new(data)
with open("firma.sig", "rb") as f: sig = f.read()
pkcs1_15.new(pub).verify(h2, sig)
print("Firma de archivo válida.")
