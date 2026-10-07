import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
# print(chars)
chars = list(chars)
key = chars.copy()
random.shuffle(key)
# print(f"chars: {chars}")
# print(f"key: {key}")

#ENCRYPT

plain_text = input("Enter a massage to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original massage  : {plain_text}")
print(f"encrypted massage : {cipher_text}")

#DECRYPT

cipher_text = input("Enter a massage to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted massage : {cipher_text}")
print(f"original massage  : {plain_text}")