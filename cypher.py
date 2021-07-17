import random
import string

old = list(string.printable)
new = list(string.printable)

key = input("key: ")

a = input("mode (encrypt/decrypt): ")
b = input("message: ")
if a == "decrypt":
    decrypted = ""
    for c in b:
        random.seed(key)
        random.shuffle(new)
        index = 0
        if c in new:
            for c2 in new:
                if c == c2:
                    decrypted += old[index]
                    break
                index += 1
        else:
            decrypted += c
    print(decrypted)
else:
    encrypted = ""
    for c in b:
        random.seed(key)
        random.shuffle(new)
        index = 0
        if c in old:
            for c2 in old:
                if c == c2:
                    encrypted += new[index]
                    break
                index += 1
        else:
            encrypted += c
    print(encrypted)
