from SHA256 import sha256


def test_one_block_message():
    inpt = b'abc'
    res = sha256(inpt)
    assert isinstance(res, bytes)
    assert len(res) == 32
    assert res.hex() == 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'


def test_multi_block_message():
    inpt = b'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq'
    res = sha256(inpt)
    assert isinstance(res, bytes)
    assert len(res) == 32
    assert res.hex() == '248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1'



def test_long_message():
    inpt = b'a'*1000000
    res = sha256(inpt)
    assert isinstance(res, bytes)
    assert len(res) == 32
    assert res.hex() == 'cdc76e5c9914fb9281a1c7e284d73e67f1809a48a497200e046d39ccc7112cd0'