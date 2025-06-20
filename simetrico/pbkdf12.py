from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

password = b"clave_super_segura"
salt = get_random_bytes(16)
key = PBKDF2(password, salt, dkLen=32, count=1000000, hmac_hash_module=hashlib.sha256)

cipher = AES.new(key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(b"Mensaje protegido")

# Descifrado
cipher_dec = AES.new(key, AES.MODE_GCM, nonce=cipher.nonce)
plaintext = cipher_dec.decrypt_and_verify(ciphertext, tag)
print(plaintext.decode())
