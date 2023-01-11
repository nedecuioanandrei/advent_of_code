import hashlib

nr = 0
while True:
    s = b"iwrupvqb"
    if hashlib.md5(s + bytes(str(nr), 'utf-8')).hexdigest().startswith("00000"):
        print(nr)
        exit(0)
    else:
        nr += 1 
