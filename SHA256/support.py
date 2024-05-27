from .constants import *


def Ch(x: int, y: int, z: int) -> int:
    return (x & y) ^ (~x & z)


def Maj(x: int, y: int, z: int) -> int:
    return (x & y) ^ (x & z) ^ (y & z)


def SHR(x: int, n: int) -> int:
    return x >> n


def ROTR(x: int, n: int) -> int:
    return (x >> n) | (x << (w - n)) & 0xFFFFFFFF


def sum0(x: int) -> int:
    return ROTR(x, 2) ^ ROTR(x, 13) ^ ROTR(x, 22)


def sum1(x: int) -> int:
    return ROTR(x, 6) ^ ROTR(x, 11) ^ ROTR(x, 25)


def sigma0(x: int) -> int:
    return ROTR(x, 7) ^ ROTR(x, 18) ^ SHR(x, 3)


def sigma1(x: int) -> int:
    return ROTR(x, 17) ^ ROTR(x, 19) ^ SHR(x, 10)
