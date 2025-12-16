#https://rosalind.info/problems/cons/

dna = []
current_seq = ''
with open('Algorithm-Design_Stronghold\\Consensus and Profile\\rosalind_cons.txt') as f:
    for line in f:
        line = line.strip()
        if not line.startswith('>'):
            current_seq += line
        else:
            dna.append(current_seq)
            current_seq = ''
    if current_seq:
        dna.append(current_seq)
dna.pop(0)
                


l = len(dna[0])
A = [0] * l
C = [0] * l
G = [0] * l
T = [0] * l


for strand in dna:
    y = 0
    for nucleotide in strand:
        if nucleotide == 'A':
            A[y] += 1
        if nucleotide == 'C':
            C[y] += 1
        if nucleotide == 'G':
            G[y] += 1
        if nucleotide == 'T':
            T[y] += 1
        y += 1

consensus_string = ''
for x in range(0,l):
    values = {'A':A[x],'C':C[x],'G':G[x],'T':T[x]}
    highest_base = max(values,key=values.get)
    consensus_string += highest_base
print(consensus_string)


A_string = ' '.join(str(x) for x in A)
print(f"A: {A_string}")

C_string = ' '.join(str(x) for x in C)
print(f"C: {C_string}")

G_string = ' '.join(str(x) for x in G)
print(f"G: {G_string}")

T_string = ' '.join(str(x) for x in T)
print(f"T: {T_string}")
    
            








