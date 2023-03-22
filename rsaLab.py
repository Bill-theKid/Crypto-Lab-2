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
        while data:
            # encrypt