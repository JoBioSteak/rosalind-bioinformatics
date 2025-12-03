filename = "Algorithm-Design_Stronghold\\Mendel's First Law\\rosalind_iprb.txt"
with open(filename) as f:
    k, m, n = [int(x) for x in next(f).split()]
    
population = k + m + n
total_pairs = (population * (population - 1)) / 2


#probability * unique offspring pairs
mm = 0.25 * (m*(m-1)/2)  
nn = 1.0 * (n*(n-1)/2)    
mn = 0.5 * (m*n)          

#calculation
P_reccessive = (mm + nn + mn) / total_pairs
P_dominant = 1 - P_reccessive 

print(round(P_dominant,5))