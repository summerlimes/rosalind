a=0
t=0
c=0
g=0
with open("dna.txt") as file:
    while True:
        s = file.read(1)
        if s == 'A':
            a += 1
        elif s == 'T':
            t += 1
        elif s == 'C':
            c += 1
        elif s == 'G':
            g += 1
        elif not s:
            break
    print (a,c,g,t)
