import os

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

def getPrivateKey(file):
    fr = open(file,'r')
    N = int(fr.readline().rstrip('\n'))
    d = int(fr.readline())
    fr.close()
    return N, d

def RSA(file, N, d):
    fo = open(file, 'r')
    C = int(fo.readline())
    decrypt_c = pow(C,d,N)
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

def main():
    file128 = input('Enter private key 128bit direction: ')
    N128, d128 = getPrivateKey(file128)
    file1024 = input('Enter private key 1024bit direction: ')
    N1024, d1024 = getPrivateKey(file1024)
    pass1 = RSA('pass1.txt', N128, d128)
    pass2 = RSA('pass2.txt', N1024, d1024)
    passwd = rot47(pass1) + rot47(pass2)
    # os.system("sshpass -p %s ssh -o StrictHostKeyChecking=no ubuntu@10.10.0.2" % passwd)
    print(passwd)

main()