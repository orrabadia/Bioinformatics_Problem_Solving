import sys
file = open("Complementing DNA/rosalind_revc.txt")
dna = file.read()
dnareverse = dna[::-1]

for letter in dnareverse:
    if letter == "A":
        dnareverse = dnareverse.replace("A", "t", 1)
    elif letter == "G":
        dnareverse = dnareverse.replace("G", "c", 1)
        continue
    elif letter == "C":
        dnareverse = dnareverse.replace("C", "g", 1)
        continue
    elif letter == "T":
        dnareverse = dnareverse.replace("T", "a", 1)
        continue

print(dnareverse.upper())

# some issues I ran into: I first didn't know how to keep track of the letters I changed
# I then thought to replace everything with lower case letters, and then uppercase it later
# I also drew it out on paper to know when to reverse the string
        
