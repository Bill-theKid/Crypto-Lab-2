import sys

p = 137 # prime
q = 131 # prime
n = p * q
e = 3 # relatively prime to r
r = (p-1) * (q-1)
k = r + 1 # first number equal to 1 mod r
d = k / e # divide by e and check validity vv

while((e*d % r) != 1 or (d % 1) != 0): # check if coprime and if d is integer
    k = k + r
    d = k / e
d = int(d)

print(f' n = {n}\n r = {r}\n k = {k} \n d = {d}')

with open('message.txt', 'rb') as infile:
    with open('cipher.txt', 'wb') as outfile:
        data = infile.read(2)
        print('encrypting...')
        while data:
            print(data)
            # encrypt
            msg_block = int.from_bytes(data, sys.byteorder)
            cipher_txt = (msg_block ** e) % n
            print(cipher_txt)
            out_block = cipher_txt.to_bytes(2, sys.byteorder)
            outfile.write(out_block)
            data = infile.read(2)

with open('cipher.txt', 'rb') as infile:
    with open('decrypted.txt', 'wb') as outfile:
        data = infile.read(2)
        print('decrypting...')
        while data:
            # decrypt
            msg_block = int.from_bytes(data, sys.byteorder)
            for x in range(d - 1):
                msg_block = msg_block * msg_block % n
            decrypt_txt = msg_block
            print(decrypt_txt)
            out_block = decrypt_txt.to_bytes(2, sys.byteorder)
            print(out_block)
            outfile.write(out_block)
            data = infile.read(2)

