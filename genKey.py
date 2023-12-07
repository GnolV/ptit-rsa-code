import random

e = 65537

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def generate_prime(bits):
    while True:
        candidate = random.getrandbits(bits)
        if is_prime(candidate):
            return candidate

def genKey128():
    num_bits = 35
    p = generate_prime(num_bits)
    q = generate_prime(num_bits)
    while p == q:
        q = generate_prime(num_bits)
    print(p, q)
    n = p*q
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    fo1 = open('public128.txt', 'w')
    fo1.write(str(n)+'\n'+str(e))
    fo2 = open('private128.txt','w')
    fo2.write(str(n)+'\n'+str(d))
    
def genKey1024():
    num_bits = 512
    p = generate_prime(num_bits)
    q = generate_prime(num_bits)
    while p == q:
        q = generate_prime(num_bits)
    n = p*q
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    fo1 = open('public1024.txt', 'w')
    fo1.write(str(n)+'\n'+str(e))
    fo2 = open('private1024.txt','w')
    fo2.write(str(n)+'\n'+str(d))
    
def main():
    genKey128()
    genKey1024()

main()