with open("prot.txt") as file:
    p = ''
    s = file.readline()
    for i in xrange(0,len(s),3):
        codon = s[i:i+3]
        if codon == "UUU" or codon == "UUC":
            p = p + 'F'
        elif codon == "UUA" or codon == "UUG" or codon == "CUU" or codon == "CUC" or codon == "CUA" or codon == "CUG":
            p = p + 'L'
        elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG" or codon == "AGC" or codon == "AGU":
            p = p + 'S'
        elif codon == "UAU" or codon == "UAC":
            p = p + 'Y'
        elif codon == "UGU" or codon == "UGC":
            p = p + 'C'
        elif codon == "UGG":
            p = p + 'W'
        elif codon == "CCU" or codon == "CCC" or codon == "CCA" or codon == "CCG":
            p = p + 'P'
        elif codon == "CAU" or codon == "CAC":
            p = p + 'H'
        elif codon == "CAA" or codon == "CAG":
            p = p + 'Q'
        elif codon == "CGU" or codon == "CGC":
            p = p + 'R'
        elif codon == "AUU" or codon == "AUC" or codon == "AUA":
            p = p + 'I'
        elif codon == "AUG":
            p = p + 'M'
        elif codon == "ACU" or codon == "ACC" or codon == "ACA" or codon == "ACG":
            p = p + 'T'
        elif codon == "AAC" or codon == "AAU":
            p = p + 'N'
        elif codon == "AAG" or codon == "AAA":
            p = p + 'K'
        elif codon == "CGG" or codon == "AGG" or codon == "AGA" or codon == "CGA":
            p = p + 'R'
        elif codon == "GUU" or codon == "GUC" or codon == "GUA" or codon == "GUG":
            p = p + 'V'
        elif codon == "GCU" or codon == "GCC" or codon == "GCA" or codon == "GCG":
            p = p + 'A'
        elif codon == "GAC" or codon == "GAU" :
            p = p + 'D'
        elif codon == "GAA" or codon == "GAG":
            p = p + 'E'
        elif codon == "GGA" or codon == "GGC" or codon == "GGU" or codon == "GGG":
            p = p + 'G'
        elif codon == "UAA" or codon == "UAG" or codon == "UGA":
            break
    print p
