n = int(input())
#n = 11
nb = bin(n); nb = nb[2:]
m = 0
for i in range(len(nb)):
    nb = nb[1:] + nb[0]
    n = int(nb, 2)
    if m < n: 
        m = n
print(m)
