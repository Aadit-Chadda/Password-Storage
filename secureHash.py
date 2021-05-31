import hashlib


def hashing(message):
    msg = message.encode()
    sha = hashlib.sha256()
    sha.update(msg)
    digester = sha.digest()
    return digester


master_key = b'H~\xf9A\xd9\xde\xab\x95~\xc0\xd1TG\xc0\xcd\xe6\x00\xbd\x92\x9f\xee\xa79\x07\x95R&\x14\xafed\xac'

print()
print('AC-24 productions')
