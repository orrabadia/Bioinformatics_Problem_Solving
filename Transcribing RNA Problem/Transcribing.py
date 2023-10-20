
# with open ('Transcribing RNA Problem/rosalind_rna.txt') as input:
#     for line in input:
#         for item in line: 
#             if item == 'T':
#                 line = line.replace("T", "U")
#         print (line)

import sys
file = open('rosalind_rna.txt')
dna = file.read()
rna = dna.replace("T", "U")
print(rna)
    
    

    
            
        
       
        
