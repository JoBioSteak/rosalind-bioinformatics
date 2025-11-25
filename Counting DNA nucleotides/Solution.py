file = open("C:\\Users\\derel\\Desktop\\Coding_Projects\\Rosalind\\Counting DNA nucleotides\\rosalind_dna.txt")
dna_str = file.read() 

A = dna_str.count("A")
C = dna_str.count("C")
G = dna_str.count("G")
T = dna_str.count("T")

print(A, C, G, T)