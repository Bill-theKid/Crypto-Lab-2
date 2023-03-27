def encrypt(input: bytes, keyfile):
    b_array = []

    with open(keyfile, 'r') as key:
        n = int(key.readline())
        e = int(key.readline())
    
    for i in range(0, len(input), 2):
        msg_block = int.from_bytes(input[i:i+2], 'big', signed=False)
        cipher_txt = pow(msg_block, e, n)
        out_block = cipher_txt.to_bytes(4, 'big')
        b_array.append(out_block)
    
    return b''.join(b_array)

def decrypt(input: bytes, keyfile):
    b_array = []

    with open(keyfile, 'r') as key:
        n = int(key.readline())
        d = int(key.readline())

    for i in range(0, len(input), 4):
        msg_block = int.from_bytes(input[i:i+4], 'big', signed=False)
        plain_txt = pow(msg_block, d, n)
        out_block = plain_txt.to_bytes(2, 'big')
        b_array.append(out_block)

    return b''.join(b_array)
