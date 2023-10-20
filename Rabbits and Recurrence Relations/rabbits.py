
# Given: Positive integers n≤40
#  and k≤5
# .

# Return: The total number of rabbit pairs that will be present after n
#  months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
#  rabbit pairs (instead of only 1 pair).
def Rec_Relation(n, k):
    # handling input validation
    if (n > 40):
        return "invalid n"
    if (k > 5):
        return "invalid k"
    return 1 + k*(n+1) #we start with 1 pair, they make k pairs (1*k) + 
                    # then each pair in the generation make k pairs for n months (k*n)

    
    
file = open("Rabbits and Recurrence Relations/rosalind_fib.txt")
input = file.read()
inputArr = input.split(" ") #input given as two numbers separated by space
print(Rec_Relation(int(inputArr[0]), int(inputArr[1])))

