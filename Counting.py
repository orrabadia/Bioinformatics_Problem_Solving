

acount = 0
gcount = 0
ccount = 0
tcount = 0
with open ('rosalind_dna.txt') as input:
    for line in input:
        for item in line: 
            if item == 'A' or item == 'a':
                acount += 1
            if item == 'G' or item == 'g':
                gcount += 1
            if item == 'C' or item == 'c':
                ccount += 1
            if item == 'T' or item == 't':
                tcount += 1
    print ("%s %s %s %s" % (acount, ccount, gcount, tcount))
   
            
        
       
        
