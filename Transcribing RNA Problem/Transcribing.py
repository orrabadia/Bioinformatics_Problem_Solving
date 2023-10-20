
with open ('Transcribing RNA Problem/rosalind_rna.txt') as input:
    for line in input:
        for item in line: 
            if item == 'T':
                line = line.replace("T", "U")
        print (line)
    
    
    # this isn't as fast it could be: this is my initial solution, however I could have used import
    # sys to open/read the file, then just use .count(nt) for A, G, C, and T.
    # I also printed inefficiently, I could have just done print(acount,ccount,gcount,tcount)
    
            
        
       
        
