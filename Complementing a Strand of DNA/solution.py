file = open("C:\\Users\\derel\\Desktop\\Coding_Projects\\rosalind-bioinformatics\\Complementing a Strand of DNA\\rosalind_revc.txt")
strand = file.read()
c_strand = ""
for char in strand:
    if char == "C":
        c_strand = c_strand + 'G'
    if char == "T":
        c_strand = c_strand + 'A'
    if char == "A":
        c_strand = c_strand + 'T'
    if char == "G":
        c_strand = c_strand + 'C'
print(c_strand[::-1])
