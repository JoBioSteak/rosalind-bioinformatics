#https://rosalind.info/problems/subs/

filename = "Algorithm-Design_Stronghold\\Finding a Motif in DNA\\rosalind_subs.txt"
with open(filename) as f:
    lines = f.read().split()

string = lines[0]
substring = lines[1]

index = 0
indices = []
while index < len(string):
    index = string.find(substring,index)
    if index == -1:
        break
    indices.append(str(index+1))
    index += 1

print(" ".join(indices))