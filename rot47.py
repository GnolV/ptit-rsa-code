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

print(rot47('p455w0rd55hl4b3thisispasswordforrsalab'))
print('Result: p455w0rd55hl4b3thisispasswordforrsalab')