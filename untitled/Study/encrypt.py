import simplecrypt

with open("encrypted.bin", "rb") as inp:
    with open('passwords.txt', "rb") as inp1:
        encrypted = inp.read()
        passwords = inp1.read().splitlines()
        for password in passwords:
            try:
                info = simplecrypt.decrypt(password, encrypted)
                print(info.decode("utf-8"))
                break
            except:
                print('Wrong password')
