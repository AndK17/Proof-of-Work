import json
from random import randint
from typing import List


def generate_bytes(n: int) -> bytes:
    """Генерирует строку случайных байт размером n

    Args:
        n (int): количество генерируемых байт

    Returns:
        bytes: сгенерированные байты
    """
    return bytes([randint(0, 2**8 - 1) for i in range(n)])


def load_previous_hash(path: str = 'data/previous.txt') -> bytes:
    """Загружает хэш предыдущего блока из файла

    Args:
        path (str, optional): путь к файлу. Defaults to 'data/previous.txt'.

    Returns:
        List[bytes]: хэш предыдущего блока
    """
    with open(path, 'r') as f:
        hex_data_array_read = [bytes.fromhex(line.strip()) for line in f]

    return hex_data_array_read[0]


def load_transactions(path: str = 'data/transactions.txt') -> List[bytes]:
    """Загружает транзакции из файла

    Args:
        path (str, optional): путь к файлу. Defaults to 'data/transactions.txt'.

    Returns:
        List[bytes]: список транзакций преобразованных в байты
    """
    with open(path, 'r') as f:
        return [bytes.fromhex(line.strip()) for line in f]


def generate_random_transactions(n: int, path: str = 'data/transactions.txt') -> None:
    """Генерирует заданное количество транзакций

    Args:
        n (int): необходимое количество транзакций
        path (str, optional): путь к файлу для сохранения. Defaults to 'data/transactions.txt'.
    """
    with open(path, 'w') as f:
        for _ in range(n):
            f.write(generate_bytes(226).hex() + '\n')


def save_block(block: dict, path: str = 'data/block.json') -> None:
    """Сохраняет блок в json файл

    Args:
        block (dict): Блок
        path (str, optional): путь к файлу. Defaults to 'data/block.json'.
    """
    with open(path, 'w') as f:
        json.dump({i: v.hex() for i, v in block.items()}, f)
