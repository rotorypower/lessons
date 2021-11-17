#Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
# которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
# Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.

#Списан ваш код для понимания, это не мое решение !!! 

import base64

inpstr = input("Строка для кодирования: ")
inpkey = input("Ключ: ")

def printable_encrypted_string(string):

     bytes = string.encode("ascii")
     base64_bytes = base64.b64encode(bytes)
     return base64_bytes.decode("ascii")


def get_key_sym(key, index):
    if index > len(key) - 1:
        return key[index % len(key)]
    return key[index]


def xor_cipher(string, key):
    result = []
    for index, symbol in enumerate(string):
        result.append(chr(ord(symbol) ^ ord(get_key_sym(key, index))))
    return "".join(result)

encstring = xor_cipher(inpstr, inpkey)
print("Кодирование: " + printable_encrypted_string(encstring))

decstring = xor_cipher(encstring, inpkey)
print("Строка для кодирования: " + decstring)
