def is_prime(num):
    if num == 1:
        return False
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return False
    return True

def euclid(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

p = int(input('Input value for p: '))
if not is_prime(p):
    print(f'Error: {p} is not a prime number')

q = int(input('Input value for q: '))
if not is_prime(q):
    print(f'Error: {q} is not a prime number')

r = (p-1) * (q-1)

e = int(input('Input value for e: '))
gcd = euclid(e, r)
print(f'e = {e} \n(p-1) * (q-1) = {r} \ngcd = {gcd}')
if gcd != 1:
    print(f'e: {e}, is not relatively prime to (p-1)*(q-1): {r}')
else:
    print(f'e: {e} and (p-1) * (q-1): {r} are relatively prime')
