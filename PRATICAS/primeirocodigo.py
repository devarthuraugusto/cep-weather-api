'''n = int(input(''))

soma = 0

for i in range(1, n+1):
    if n % i == 0:
        soma += i
    print(i)

print(soma)'''


n = int(input(''))

soma = n

for i in range(1, (n//2) +1):
    if n % i == 0:
        soma += i

print(soma)