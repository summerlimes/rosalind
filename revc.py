s1 = ''
with open("revc.txt") as file:
    while True:
        c = file.read(1)
        if c == 'A':
            s1 = 'T' + s1
        elif c == 'T':
            s1 = 'A' + s1
        elif c == 'C':
            s1 = 'G' + s1
        elif c == 'G':
            s1 = 'C' + s1
        elif not c:
            break
    print (s1)
