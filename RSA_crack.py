import math

N = 636759522636283862603
e = 65537

#Put your code here
def calculate_PQ():
    n = int(math.sqrt(N))
    if n%2==0: n += 1
    for i in range(n, 3, -2):
        if N%i==0:
            p = i
            break
    q = int(N/p)
    return p, q

def RSA(cipher):
    p, q = calculate_PQ()
    phi = (p-1)*(q-1)
    d = modinv(e, phi)
    decrypt_c = pow(cipher,d,N)
    return num_to_char(str(decrypt_c))

#Convert number to character
def num_to_char(text):
    text_lst = [''.join(c) for c in text]
    decrypt_lst = []
    while(len(text_lst)!=0):
        tmp = text_lst.pop(0)
        if tmp == '1':
            tmp += text_lst.pop(0)
            tmp += text_lst.pop(0)
        else:
            tmp += text_lst.pop(0)
        decrypt_lst.append(int(tmp))
        tmp = ''
    clear_text = ''.join(chr(c) for c in decrypt_lst)
    return clear_text

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modulo inverses do not exist')
    else:
        return x % m

def rot47(text):
    result = ""
    for char in text:
        if char.isprintable():
            if '!' <= char <= '~':
                result += chr(((ord(char) - 33 + 47) % 94) + 33)
            else:
                result += char
        else:
            result += char
    return result

#Print your results here
cipher_text = int(input('Enter cipher text: '))
res = rot47(RSA(cipher_text))
print('Result: ' + res)