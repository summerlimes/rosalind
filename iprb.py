with open("iprb.txt") as file:
    d = int(file.read(2).split()[0])
    h = int(file.read(2).split()[0])
    r = int(file.read(2).split()[0])
    pop = float(d+h+r)
    prob = (d/pop)
    prob = prob + (r*h/(pop*pop-pop))
    prob = prob + ((d*(r+h))/(pop*(pop-1)))
    prob = prob + (3*h*(h-1)/(4*pop*(pop-1)))
    print prob
