from SHA256 import sha256
from typing import List
from math import log2
from time import time
from support import *


def merkle_root(transactions: List[bytes]) -> bytes:
    """Функция реализующая подсчет корня дерева Меркла

    Args:
        transactions (List[bytes]): транзакции по которым строится дерево

    Returns:
        bytes: корень дерева(хэш всех транзакций)
    """
    hashs = [sha256(i) for i in transactions]
    
    while log2(len(hashs)) % 1 != 0:
        hashs.append(hashs[-1])
    
    while len(hashs) > 1:
        new_hashs = []
        for i in range(0, len(hashs), 2):
            new_hashs.append(sha256(hashs[i] + hashs[i + 1]))
        hashs = new_hashs
    
    return hashs[0]


def mine(size: bytes, previous: bytes, merkle_root: bytes, time: bytes) -> int:
    """Функция реализующая поиск nonce при котором хэш начинается с 4 нулей(выполняет Proff of Work)

    Args:
        size (bytes): размер блока
        previous (bytes): хэш заголовка предыдущего блока
        merkle_root (bytes): корень Меракла транзакций нашего блока
        time (bytes): время создания блока

    Returns:
        int: nonce при котором хэш начинается с 4 нулей
    """
    nonce = 0
    base_header = size + previous + merkle_root + time
    
    hash = sha256(base_header + nonce.to_bytes(4, byteorder='big'))

    
    while bin(hash[0])[2:].zfill(8)[:4] != '0000':
        nonce += 1
        hash = sha256(base_header + nonce.to_bytes(4, byteorder='big'))
        # print(nonce, bin(hash[0])[2:].zfill(8)[:4], hash)
        
    return nonce.to_bytes(4, byteorder='big')


if __name__ == '__main__':
    path = input("Input path to file with transactions(data/transactions by default) or input 'g' if want generate random transactions: ")
    if path == 'g':
        n = input("How many transactions you want to generate(4 by default): ")
        if n == '':
            generate_random_transactions(4)
        else:
            generate_random_transactions(int(n))
        transactions = load_transactions()
    elif path == '':
        transactions = load_transactions()
    else:
        transactions = load_transactions(path)

    path_to_hash = input("Input path to file with previous transaction hash(data/previous by default): ")
    if path_to_hash == '':
        previous_hash = load_previous_hash()
    else:
        previous_hash = load_previous_hash(path_to_hash)


    transactions_hash = merkle_root(transactions)
    block_size = (80 + len(transactions) * 226).to_bytes(4, byteorder='big')
    start_time = int(time()).to_bytes(4, byteorder='big')
    nonce = mine(block_size, previous_hash, transactions_hash, start_time)


    block = {'size': block_size,
             'previous': previous_hash,
             'merkle_root': transactions_hash,
             'time': start_time,
             'nonce': nonce
             }
    
    print('Block:', {i: v.hex() for i, v in block.items()})
    save_block(block)
    print('Block is saved in data/block.json')
    