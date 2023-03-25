# the following code was used to check values and generate d value

# p = 137 # prime
# q = 577 # prime
# n = p * q
# e = 133 # relatively prime to r
# r = (p-1) * (q-1)
# k = r + 1 # first number equal to 1 mod r
# d = k / e # divide by e and check validity vv

# while((e*d % r) != 1 or (d % 1) != 0): # check if coprime and if d is integer
#     k += r
#     d = k / e
# d = int(d)

# print(f' n = {n}\n r = {r}\n k = {k} \n d = {d}')

bs = int(input('Enter block size (bytes): '))

infile = input('Enter file to encrypt: ')
outfile = input('Enter file to save ciphertext: ')

with open(infile, 'rb') as infile:
    with open(outfile, 'wb') as outfile:
        with open('key.pub', 'r') as pubkey:
            n = int(pubkey.readline())
            e = int(pubkey.readline())
            data = infile.read(bs)
            while data:
                msg_block = int.from_bytes(data, 'big', signed=False)
                cipher_txt = pow(msg_block, e, n)
                out_block = cipher_txt.to_bytes(bs*2, 'big')
                outfile.write(out_block)
                data = infile.read(bs)

infile = input('Enter file to decrypt: ')
outfile = input('Enter file to save plaintext: ')

with open(infile, 'rb') as infile:
    with open(outfile, 'wb') as outfile:
        with open('key.priv', 'r') as privkey:
            n = int(privkey.readline())
            d = int(privkey.readline())
            data = infile.read(bs*2)
            while data:
                msg_block = int.from_bytes(data, 'big', signed=False)
                decrypt_txt = pow(msg_block, d, n)
                out_block = decrypt_txt.to_bytes(bs, 'big')
                outfile.write(out_block)
                data = infile.read(bs*2)
