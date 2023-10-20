
# Given: Positive integers n≤40
#  and k≤5
# .

# Return: The total number of rabbit pairs that will be present after n
#  months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
#  rabbit pairs (instead of only 1 pair).
def Rec_Relation(n, k):
    if (n > 40): #handle validation
        return "invalid n"
    if (k > 5): #handle validation
        return "invalid k"
    if (n == 1): #base case
        return 1
    elif (n == 2): #second month, 1st pair just matured and
        return k
    if (n <= 4): #can be predicted using numbers from 1 and 2 gens previous
        return Rec_Relation(n-1, k) + Rec_Relation(n-2, k) #Fib
    return Rec_Relation(n-1, k) + (Rec_Relation(n-2, k) * k) #pattern identification
    

    
    
file = open("rosalind_fib.txt")
input = file.read()
inputArr = input.split(" ") #input given as two numbers separated by space
print(Rec_Relation(int(inputArr[0]), int(inputArr[1])))

