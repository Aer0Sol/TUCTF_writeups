from pwn import remote, context
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from icecream import ic

def bytes2bin(msg, length=48):
    return bin(b2l(msg))[2:].zfill(length)

def bin2bytes(msg):
    return l2b(int(msg, 2))

io = remote('chal.tuctf.com', 30004)

def encrypt(pt: bytes, key: bytes):
    io.sendline(b'1')
    io.sendlineafter(b'plaintext: ', pt)
    io.sendlineafter(b'): ', key.hex().upper().encode())
    io.recvuntil(b'is: \n')
    ct = io.recvline().strip().decode()
    ic(ct)
    return bin2bytes(ct)

def decrypt(ct: bytes, key: bytes):
    io.sendline(b'2')
    io.sendlineafter(b'binary: ', bytes2bin(ct).encode())
    io.sendlineafter(b'): ', key.hex().upper().encode())
    io.recvuntil(b'back: \n')
    pt = io.recvline().strip().decode()
    ic(pt)
    return bin2bytes(pt)

pattern = []
for i in range(48):
    payload = ['0'] * 48
    payload[i] = '1'
    payload = ''.join(payload)
    payload = bin2bytes(payload)
    if len(payload) < 6:
        payload = payload.rjust(6, b'\x00')
    ic(payload)
    ct = bytes2bin(encrypt(payload, b'\x00' * 6))
    if ct.count('1') > 1:
        pattern.append(-1)
        continue
    pattern.append(ct.index('1'))
ic(pattern)
ic(pattern.count(-1))