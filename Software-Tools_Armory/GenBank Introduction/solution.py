from Bio import Entrez
Entrez.email = "saltedtangerine@gmail.com"

filename = "Software-Tools_Armory\\GenBank Introduction\\rosalind_gbk.txt"
with open(filename) as f:
    data = f.readlines()
    genus = data[0].strip()
    start_date = data[1].strip()
    end_date = data[2].strip()
    
handle = Entrez.esearch(
    db="nucleotide", 
    term=f"{genus}[Orgn]", 
    mindate=start_date,
    maxdate=end_date,
    datetype="pdat"
    )

record = Entrez.read(handle)
print(record["Count"])

    