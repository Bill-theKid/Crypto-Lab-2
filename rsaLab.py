p = 137 # prime
q = 131 # prime
n = p * q
e = 3 # relatively prime to r
r = (p-1) * (q-1)
k = r + 1 # first number equal to 1 mod r
d = k / e # divide by e and check validity vv

while((e*d % r) != 1 or (d % 1) != 0):
    k = k + r
    d = k / e
d = int(d)

print(f'n = {n}\nr = {r}\nk = {k} \nd = {d}')
