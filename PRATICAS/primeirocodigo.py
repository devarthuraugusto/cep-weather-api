while True:
    cpf = input("Digite seu CPF: ")

    # tratando o cpf
    cpf = cpf.strip()
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")

    if cpf.isdigit() and len(cpf) == 11:
        print(f'Obrigado, seu cpf: {cpf}!')
        break
    else:
        print('CPF inválido. Tente novamente.')
