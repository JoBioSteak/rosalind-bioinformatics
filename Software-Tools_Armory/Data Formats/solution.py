#https://rosalind.info/problems/frmt/

from Bio import Entrez
from Bio import SeqIO
Entrez.email = "saltedtangerine@gmail.com"

filename = "Software-Tools_Armory\\Data Formats\\rosalind_frmt.txt"
id_list = []
with open(filename) as f:
    data = f.read().split()
    for id in data:
        id_list.append(id.strip())

shortest_len = float('inf')
shortest_record = None

handle = Entrez.efetch(db="nucleotide",id=id_list,rettype="fasta")

for seq_record in SeqIO.parse(handle,"fasta"):
    if len(seq_record.seq) < shortest_len:
        shortest_record = seq_record
        shortest_len = len(shortest_record.seq)

print(shortest_record.description)
print(shortest_record.seq)