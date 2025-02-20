import struct

def cha_cha_cha(key, iv, position=0):
    if not isinstance(position, int):
        raise TypeError
    if position & ~0xffffffff:
        raise ValueError("Position is not uint32.")

    if not isinstance(key, bytes) or len(key) != 32:
        raise ValueError("Key must be 32 bytes.")
    if not isinstance(iv, bytes) or len(iv) != 8:
        raise ValueError("IV must be 8 bytes.")

    def rotate(v, c):
        return ((v << c) & 0xffffffff) | (v >> (32 - c))

    def quarter_round(x, a, b, c, d):
        x[a] = (x[a] + x[b]) & 0xffffffff
        x[d] = rotate(x[d] ^ x[a], 16)
        x[c] = (x[c] + x[d]) & 0xffffffff
        x[b] = rotate(x[b] ^ x[c], 12)
        x[a] = (x[a] + x[b]) & 0xffffffff
        x[d] = rotate(x[d] ^ x[a], 8)
        x[c] = (x[c] + x[d]) & 0xffffffff
        x[b] = rotate(x[b] ^ x[c], 7)

    ctx = [0] * 16
    ctx[:4] = (0x61707865, 0x3320646e, 0x79622d32, 0x6b206574)  # "expand 32-byte k"
    ctx[4:12] = struct.unpack("<8L", key)
    ctx[12] = position & 0xffffffff
    ctx[13] = (position >> 32) & 0xffffffff
    ctx[14:16] = struct.unpack("<2L", iv)

    while True:
        x = list(ctx)
        for _ in range(10):
            quarter_round(x, 0, 4, 8, 12)
            quarter_round(x, 1, 5, 9, 13)
            quarter_round(x, 2, 6, 10, 14)
            quarter_round(x, 3, 7, 11, 15)
            quarter_round(x, 0, 5, 10, 15)
            quarter_round(x, 1, 6, 11, 12)
            quarter_round(x, 2, 7, 8, 13)
            quarter_round(x, 3, 4, 9, 14)

        for c in struct.pack("<16L", *[(x[i] + ctx[i]) & 0xffffffff for i in range(16)]):
            yield c

        ctx[12] = (ctx[12] + 1) & 0xffffffff
        if ctx[12] == 0:
            ctx[13] = (ctx[13] + 1) & 0xffffffff


def chacha20_decrypt(data, key, iv, position=0):
    if not isinstance(data, bytes):
        raise TypeError("Data must be bytes.")
    return bytes(a ^ b for a, b in zip(data, cha_cha_cha(key, iv, position)))


if __name__ == "__main__":
    # Beispiel-Initialisierung
    key = b'0x61707865+0x3320646e'
    iv = b"8byte_iv"

    encrypted = b"B\xd0\xab\xb2E\xc4\xdbOa\xae\xfc\xce7\xdf;\xcd\xa9\x18%\xcc?\xae\xe5\xda\x170\x10\x93\x8a'"
    decrypted = chacha20_decrypt(encrypted, key, iv)

    print("The Flag for this Challenge is:")
    print(decrypted.decode())
