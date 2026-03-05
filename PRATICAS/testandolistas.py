produtos = ["arroz", "feijão", "macarrão", "óleo", "açúcar", "pó"]
precos = [25.50, 9.80, 6.40, 7.90, 4.30, 12.00]

# printar valor único da lista por índice
print(f"Na lista tem {produtos[2]}, com o preço de R${precos[2]}.")

# buscar produto na lista
busca = input("O que você quer buscar na lista? ")

if busca in produtos:
    indice = produtos.index(busca)
    print(f"Tem {busca} na lista.")
    print(f"O índice de {busca} é {indice}.")
    print(f"O preço é R${precos[indice]}.")
else:
    print(f"Não tem {busca} na lista.")

# adicionar produto e preço
novo_produto = "batata"
novo_preco = 5.60

produtos.append(novo_produto)
precos.append(novo_preco)

print(f"Adicionamos {novo_produto} com preço R${novo_preco}.")

# remover produto e preço pelo índice
indice_remover = 6

produto_removido = produtos.pop(indice_remover)
preco_removido = precos.pop(indice_remover)

print(f"Removemos o produto {produto_removido} que custava R${preco_removido}.")
