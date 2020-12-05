with open("subs.txt") as file:
    s = file.readline()
    t = file.readline().strip()
    t_len = len(t)
    for i in range(len(s)):
        if s[i] == t[0]:
            if t == s[i:i+len(t)]:
                print (i+1," ",end="")
