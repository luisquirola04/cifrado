from Crypto.PublicKey import RSA

# Exportación
key = RSA.generate(2048)
pub = key.publickey().export_key(format='PEM')
with open("pub.pem", "wb") as f: f.write(pub)

# Importación
with open("pub.pem", "rb") as f:
    key_imported = RSA.import_key(f.read())
    print(key_imported.export_key())
