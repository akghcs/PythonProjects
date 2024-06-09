#CHAPTER 6
prgm = int(input("which excercise"))

if prgm == 1:
    sen = str(input("Enter a sentence."))
    length = (len(sen))
    minlen = 0
    print(length)
    index = int(length)
    for i in range(10):
        print(sen)
    print(sen[0:1])
    print(sen[0:2 + 1])
    print(sen[-3:])
    slic = sen[length::-1]
    print(slic)
    if index < 6:
        print("Your string is not long enough for this one")
    if index >= 6 :
        index = sen[6]
        print(index)
        sencomb = sen[1:-1]
        print(sencomb)
    strupper = str.upper(sen)
    print(strupper)
    print(" ".join(sen))
    for a in sen:
        senrep = sen.replace(a, "e")
        print(senrep)
        break

if prgm >= 2:
    msg = input("enter a msg: ")
    part = eval(input("enter encryption: "))
    encrypted = ""
    for chunk in range(part):
        for i in range(chunk, (len(msg)), part):
            encrypted = encrypted + msg[i]
            print(encrypted)

message = input("Enter a message: ")
part = eval(input('how many parts was it split? '))
lengt = len(message)
block = lengt//part
decrypted = ""

for k in range(0, lengt, part):
    for i in range(block):
        for j in range(part):
            section = message[part + i]
            decrypted = decrypted + section

print(decrypted)