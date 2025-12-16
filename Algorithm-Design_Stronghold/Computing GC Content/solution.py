#https://rosalind.info/problems/gc/

filename = "Algorithm-Design_Stronghold\\Computing GC Content\\rosalind_gc.txt"

#Simple counter
def GC_count(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    total_length = len(sequence)
    if gc_count == 0:
        return 0.0
    else:
        return (gc_count/total_length) * 100

#Parsing the data to retrieve string ID and String

def data_parse(file):
    data = {} # "ID" : "String"
    current_ID = None
    current_string = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            
            if line.startswith(">Rosalind_"):
                current_ID = line[1:]
                if current_ID:
                    data[current_ID] = "".join(current_string)
                current_string = []
            else:
                current_string.append(line)
                
            if current_ID:
                data[current_ID] = "".join(current_string)
    return data

#Finding the highest GC content
highest_GC = 0
current_GC = 0
highest_ID = ''

dataset = data_parse(filename)

for key in dataset:
    current_GC = GC_count(dataset[key])
    if current_GC > highest_GC:
        highest_GC = current_GC
        highest_ID = key

print(highest_ID, highest_GC)