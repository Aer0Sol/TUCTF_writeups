from itertools import cycle

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, cycle(b)))

key = b'Emoji Moring Sta'

with open('table_encryption.xml.enc', 'rb') as f:
    data = f.read()

encrypted = xor(data, key)

with open('xored.xml', 'wb') as output:
    output.write(encrypted)
