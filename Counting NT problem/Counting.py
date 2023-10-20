

acount = 0
gcount = 0
ccount = 0
tcount = 0
with open ('Counting NT problem/rosalind_dna.txt') as input:
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
    print(acount,ccount,gcount,tcount)
    
    # this isn't as fast it could be: this is my initial solution, however I could have used import
    # sys to open/read the file, then just use .count(nt) for A, G, C, and T.
    # I also printed inefficiently, I could have just done print(acount,ccount,gcount,tcount)
    
            
        
       
        
