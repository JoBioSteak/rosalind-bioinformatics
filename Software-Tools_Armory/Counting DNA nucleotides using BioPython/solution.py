#https://rosalind.info/problems/ini/

from Bio.Seq import Seq
filename = "Software-Tools_Armory\\Counting DNA nucleotides using BioPython\\rosalind_ini.txt"
with open(filename) as f:
    my_seq = Seq(f.read())
    print(my_seq.count("A"),my_seq.count("C"),my_seq.count("G"),my_seq.count("T"))