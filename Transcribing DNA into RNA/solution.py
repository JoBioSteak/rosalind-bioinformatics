file = open("C:\\Users\\derel\\Desktop\\Coding_Projects\\rosalind-bioinformatics\\Transcribing DNA into RNA\\rosalind_rna.txt")
RNA_strand = file.read()
print(RNA_strand.replace('T','U'))

