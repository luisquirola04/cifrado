from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA


msg = b"Texto original"
key = RSA.import_key(open("privada.pem").read(), passphrase="clave123")
h = SHA256.new(msg)
signature = pkcs1_15.new(key).sign(h)

# Modificamos mensaje
modificado = b"Texto modificado"
h_mod = SHA256.new(modificado)
try:
    pkcs1_15.new(RSA.import_key(open("publica.pem").read())).verify(h_mod, signature)
    print("Verificación incorrectamente pasada.")
except ValueError:
    print("Verificación fallida, el mensaje fue modificado.")
