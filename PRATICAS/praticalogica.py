loop = int(input(""))
for numero in range(loop +1):
    if numero % 2 == 0:
        if numero == 0:
            continue
        print(f"{numero}^2 = {numero * numero}")
