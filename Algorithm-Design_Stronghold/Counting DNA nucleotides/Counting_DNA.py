A_count = 0
T_count = 0
G_count = 0
C_count = 0
data_set = str(input("Enter the DNA strand: ")).upper()
for char in data_set:
    if char == 'A':
        A_count += 1
    if char == 'T':
        T_count += 1
    if char == 'C':
        C_count += 1
    if char == 'G':
        G_count += 1

print(f"{A_count} {C_count} {G_count} {T_count}")


