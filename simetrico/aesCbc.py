from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
iv = get_random_bytes(16)
#cifrado
with open("archivo.txt", "rb") as f:
    data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
ciphered = cipher.encrypt(pad(data, AES.block_size))

with open("archivo_cifrado.bin", "wb") as f:
    f.write(iv + ciphered)

# Descifrado
with open("archivo_cifrado.bin", "rb") as f:
    iv = f.read(16)
    ciphertext = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
original = unpad(cipher.decrypt(ciphertext), AES.block_size)
print(original.decode())
