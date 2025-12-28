def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')

            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result


def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr(base + (25 - (ord(char) - base)))
            result += new_char
        else:
            result += char
    return result


class CipherDescriptor:

    def __init__(self, cipher_type, shift=3):
        self.cipher_type = cipher_type
        self.shift = shift

    def __set_name__(self, owner, name):

        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        encrypted = getattr(obj, self.private_name, "")

        if self.cipher_type == "caesar":
            return caesar_cipher(encrypted, self.shift, decrypt=True)
        elif self.cipher_type == "atbash":
            return atbash_cipher(encrypted)
        return encrypted

    def __set__(self, obj, value):

        if self.cipher_type == "caesar":
            encrypted = caesar_cipher(value, self.shift, decrypt=False)
        elif self.cipher_type == "atbash":
            encrypted = atbash_cipher(value)
        else:
            encrypted = value
        setattr(obj, self.private_name, encrypted)



class SecretMessage:
    caesar_text = CipherDescriptor("caesar", shift=3)
    atbash_text = CipherDescriptor("atbash")



msg = SecretMessage()

text1 = "Hello World!"
text2 = "Hello World!"

print("Цезарь (расшифровано):", text1)
print("Атбаш (расшифровано):", text2)

print("\nВнутреннее хранилище:")
print("Цезарь (зашифровано):", text1)
print("Атбаш (зашифровано):", text2)