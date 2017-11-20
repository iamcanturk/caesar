import argparse
desc="""
|     title      |          Caesar.py           |
|----------------|------------------------------|
| author         | Yusuf Can TÜRK               |
| mail           | rekcahesrever@protonmail.com |
| version        | 1.0                          |
| python_version | 3.6.3                        |
| licence        | MIT                          |

"""
print (desc)

lwrCase = "abcçdefghıijklmnoöprsştuüvyz"
uprCase = "ABCÇDEFGHIİJKLMNOÖPRSŞTUÜVYZ"
number   = "0123456789"
symbol  = "!'^+%&/()=?_>£#$½{[]}\|/*-.:,;~¨<|€@"
blank  = chr(32)


def caesarEncrypt(text,inc):
    csrText=text
    csrInc=inc
    encrypt=''
    for c in csrText:
        if c in lwrCase:
            encrypt+=lwrCase[(lwrCase.index(c) + csrInc) % (len(lwrCase))]
        elif c in number:
            encrypt+=number[(number.index(c) + csrInc) % (len(number))]
        elif c in uprCase:
            encrypt+=uprCase[(uprCase.index(c) + csrInc) % (len(uprCase))]
        elif c in symbol:
            encrypt+=symbol[(symbol.index(c) + csrInc) % (len(symbol))]
        elif c in blank:
            encrypt+=blank
    return encrypt

def caesarDecrypt(text):
    csrText=text
    decrypt=''
    for csrInc in range(0, int(len(lwrCase))):
        for c in csrText:
            if c in lwrCase:
                decrypt += lwrCase[(lwrCase.index(c) + csrInc) % (len(lwrCase))]
            elif c in number:
                decrypt += number[(number.index(c) + csrInc) % (len(number))]
            elif c in uprCase:
                decrypt += uprCase[(uprCase.index(c) + csrInc) % (len(uprCase))]
            elif c in symbol:
                decrypt += symbol[(symbol.index(c) + csrInc) % (len(symbol))]
            elif c in blank:
                decrypt += blank
        decrypt+='\n'

    print(decrypt)


choice = input ("Encrypt = 1 - Decrypt = 2: ")
if(choice=="1"):
    text   = input("Please enter the text to be encrypted: ")
    inc = int(input("Please enter the increment amount: "))
    print("Encrypted Text: ",caesarEncrypt(text,inc))
elif(choice=="2"):
    text = input("Please enter the text to be decrypted: ")
    print("Decrpted Text:\n ", caesarDecrypt(text))
else:
    print ("Keystroke Error")



