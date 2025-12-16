#https://rosalind.info/problems/fib/

def litter_finder(n,k):
    if n <= 1:
        return n
    return (litter_finder(n-1,k) + k * litter_finder(n-2,k))

print(litter_finder(35,2))
