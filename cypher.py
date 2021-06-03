import random

old = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = input("mode (encrypt/decrypt): ")
b = input("message: ")
if a == "decrypt":
    decrypted = ""
    for c in b:
        random.seed(25)
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
        random.seed(25)
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
