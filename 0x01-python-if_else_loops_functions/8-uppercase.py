#!?usr/bin/python3
def uppercase(str):
    new_str = ""
    for a in range(len(str)):
        if (ord(str[a]) >= 97 and ord(str[a]) <= 122):
            new_str += chr(ord(str[a]) - 32)
            continue
        new_str += str[a]

    print('{0}'.format(new_str))
