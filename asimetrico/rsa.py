from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key(passphrase="clave123", pkcs=8, protection="scryptAndAES128-CBC")
public_key = key.publickey().export_key()

with open("asimetrico/privada.pem", "wb") as f: f.write(private_key)
with open("asimetrico/publica.pem", "wb") as f: f.write(public_key)
