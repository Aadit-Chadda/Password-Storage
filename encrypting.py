import base64


class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256


def encrypt(key, message):
    return bytes(message[i] ^ key.get_key_byte() for i in range(len(message)))


key = KeyStream(10)


def encryption(message):
    message = message.encode()
    cipher = encrypt(key, message)
    cipher = base64.b64encode(cipher)
    return cipher, type(cipher)


def decryption(cipher):
    cipher = cipher.encode()
    cipher = base64.b64decode(cipher)
    message = encrypt(key, cipher)
    message = str(message)
    return message


a = decryption('Gv+Qvzl1H1E=')
print(a)
print('AC-24 Productions')
