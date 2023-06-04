n1 = int(input("> "))
n2 = int(input("> "))
nfact = []
for i in range(1, n1+1):
    if n1 % i == 0 and n2 % i == 0:
        nfact.append(i)
print(nfact)
