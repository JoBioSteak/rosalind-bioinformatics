#https://rosalind.info/problems/hamm/

filename = "Algorithm-Design_Stronghold\\Counting Point Mutations\\rosalind_hamm.txt"

#Saving each strand as a separate array
strand_1 = ""
strand_2 = ""
with open(filename, 'r') as f:
    lines = f.readlines()
    strand_1 = lines[0].strip()
    strand_2 = lines[1].strip()
    
#Comparing each character
mutations = 0
n = len(strand_1)
for x in range(0,n):
    if strand_1[x] != strand_2[x]:
        mutations += 1
    
print(mutations)
        
            