# pip install stegano wheel steganocryptopy
from stegano import lsb

# записать текст в изображение
secret = lsb.hide("img/1.png", "Your password: qwerty")
secret.save("img/1_secret.png")
# считать текст
result = lsb.reveal("img/1_secret.png")
print(result)

# from steganocryptopy.steganography import Steganography

# Steganography.generate_key("")
# secret = Steganography.encrypt("key.key", "img/1.png", "secret_message.txt")
# secret.save("img/1_secret.png")

# result = Steganography.decrypt("key.key", "img/1_secret.png")
# print(result)