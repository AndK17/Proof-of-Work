from typing import List
from .support import *
from .constants import *


def preprocessing(message: bytes) -> List[bytes]:
    l = len(message) * 8
    padding = (448 - l - 1) % 512
    message += b'\x80'
    padding -= 7
    message += b'\x00' * (padding // 8)
    message += l.to_bytes(8, byteorder='big')
    return [message[i:i+64] for i in range(0, len(message), 64)]


def sha256(message: bytes) -> bytes:
    H = [[0x6a09e667], 
    [0xbb67ae85],
    [0x3c6ef372], 
    [0xa54ff53a], 
    [0x510e527f], 
    [0x9b05688c], 
    [0x1f83d9ab], 
    [0x5be0cd19]]
    
    M = preprocessing(message)
    N = len(M)
    for i in range(1, N + 1):
        m = M[i - 1]
        W = [int.from_bytes(m[j:j+4], byteorder='big') for j in range(0, len(m), 4)]
        for t in range(16, 64):
            W.append((sigma1(W[t - 2]) + W[t - 7] + sigma0(W[t - 15]) + W[t - 16]) % 2**32)
        
        a = H[0][i - 1]
        b = H[1][i - 1]
        c = H[2][i - 1]
        d = H[3][i - 1]
        e = H[4][i - 1]
        f = H[5][i - 1]
        g = H[6][i - 1]
        h = H[7][i - 1]
        
        for t in range(64):
            T1 = (h + sum1(e) + Ch(e, f, g) + K[t] + W[t]) % 2**32
            T2 = (sum0(a) + Maj(a, b, c)) % 2**32
            h = g
            g = f
            f = e
            e = (d + T1) % 2**32
            d = c
            c = b
            b = a
            a = (T1 + T2) % 2**32
            # print(t, list(map(lambda x: hex(x)[2:], [a, b, c, d, e, f, g, h])))
        
        H[0].append((a + H[0][i - 1]) % 2**32)
        H[1].append((b + H[1][i - 1]) % 2**32)
        H[2].append((c + H[2][i - 1]) % 2**32)
        H[3].append((d + H[3][i - 1]) % 2**32)
        H[4].append((e + H[4][i - 1]) % 2**32)
        H[5].append((f + H[5][i - 1]) % 2**32)
        H[6].append((g + H[6][i - 1]) % 2**32)
        H[7].append((h + H[7][i - 1]) % 2**32)
    # print(''.join([hex(i[N])[2:] for i in H]))
    # print(b''.join([i[N].to_bytes(4, byteorder='big') for i in H]))
    return b''.join([i[N].to_bytes(4, byteorder='big') for i in H])