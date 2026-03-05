meta = 10000
#Calcule o percentuual de vendedores que batram a meta de vendas

array = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcos', 9000],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870]
]
contador = 0
bateu = 0
#quais informações que eu preciso? 
#1: saber o total de vendedores.
for item in array:
    contador += 1
#2: preciso saber quantos bateram a meta
    
    bateu += 1
print(bateu)


#3: preciso converter em porcentagem
