import random
import string

def getPublicKey(file):
    fr = open(file,'r')
    n = int(fr.readline().rstrip('\n'))
    e = int(fr.readline())
    fr.close()
    return n, e

def RSA_encrypt(C, N, e):
    msg_ord = [ord(c) for c in C]
    M = int(''.join(str(i) for i in msg_ord))
    encrypt_m = pow(M,e,N)
    return str(encrypt_m)

def main():
    passwd = 'AcddH_C5dd9=c3bE9:D:DA2DDH@C57@CCD2=23'
    file128 = input('Enter public key 128bit direction: ')
    N128, e128 = getPublicKey(file128)
    file1024 = input('Enter public key 1024bit direction: ')
    N1024, e1024 = getPublicKey(file1024)
    # pos = random.randint(8,16)
    pos = 8
    file1 = open('pass1.txt', 'w')
    file1.write(RSA_encrypt(passwd[:pos], N128, e128))
    file2 = open('pass2.txt', 'w')
    file2.write(RSA_encrypt(passwd[pos:], N1024, e1024))
    # file3 = open('pass3.txt', 'w')
    # letters = string.ascii_lowercase
    # ran_str = ''.join(random.choice(letters) for i in range(16))
    # file3.write(RSA_encrypt(ran_str, N128, e128))

main()
