def validar_email(email):
    while not (email.__contains__("@") and email.__contains__(".")):
        email = input("Digite um e-mail válido: ")

def validar_preco(preco):
    if preco < 2000:
        print("Infelizmente o seguro só cobre bicicletas acima de R$2000,00 ")
    else:
        print("Bicicleta cadastrada com sucesso!")


print("Bem-vindo ao Bike Lock")


opcao = 0
status_login = 0
cpf = ""
email = ""
confirmacao_senha = ""

while opcao < 5:
    opcao = int(input(
        "Escolha uma opção abaixo: "
        "\n 1-Realizar cadastro "
        "\n 2-Realizar login"
        "\n 3-Cadastrar bicicleta"
        "\n 4-Escolher um tipo de seguro "
        "\n 5-Terminar atendimento \n"))

    match opcao:
        case 1:
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            cpf = input("CPF: ")
            email = input("E-mail: ")
            validar_email(email)
            telefone = input("Telefone: ")
            senha = input("Crie uma senha: ")
            confirmacao_senha = input("Confirme sua senha: ")

            if senha == confirmacao_senha:
                print("Cadastro efetuado com sucesso!")
            else:
                print("As senhas não coincidem, tente novamente.")

        case 2:
            login = input("CPF ou e-mail: ")
            senha_login = input("Senha: ")

            if cpf == "" and email == "":
                print("Você ainda não possui um usuário cadastrado. Selecione a opção 1 e realize um cadastro.")
            else:
                while (cpf != login or email != login) and (senha_login != confirmacao_senha):
                    print("Login ou senha incorretos!")
                    login = input("CPF ou e-mail: ")
                    senha_login = input("Senha: ")

                status_login = 1
                print("Login efetuado com sucesso!")
                print("Bem-vindo,", nome,". Como posso ajudar?")

        case 3:
            if status_login == 1:
                marca = input("Digite a marca da sua bicicleta: ")
                modelo = input("Digite o modelo da sua bicicleta: ")
                ano = int(input("Digite o ano de fabricação da bicicleta: "))
                numero_serie = input("Digite o número de série da bicicleta: ")
                preco = float(input("Digite o valor da sua bicicleta: "))

                validar_preco(preco)
            else:
                print("Por favor selecione a opção 2 e realize o login para continuar.")
        case 4:
            if status_login == 1:
                tipo_seguro = int(
                    input("Escolha o tipo de seguro: "
                          "\n 1- Plano básico "
                          "\n 2- Plano médio "
                          "\n 3- Plano premium "
                          "\n"))

                match tipo_seguro:
                    case 1:
                        seguro = "Plano básico"
                    case 2:
                        seguro = "Plano médio"
                    case 3:
                        seguro = "Plano premium"
                    case _:
                        print("Opção inválida")

                print(seguro, "selecionado com sucesso!")
            else:
                print("Por favor selecione a opção 2 e realize o login para continuar.")

print("Obrigado pela preferência, volte sempre!")










'''
░░░░░░░▄▄▄█████▄▄▄░░░░░░░
░░░░░██░░░░░░░░░░░██░░░░░
░░░██░░░░░░░░░░░░░░░██░░░
░░█░░░░░░░░░░░░░░░░░░░█░░
░█░▄▀▀▀▄░░░░░░▄▀▀▀▄░░░░█░
░█▐  ▄██▌░░░░▐  ▄██▌░░░░█
█░▐▄▄███▌░░░░▐▄▄███▌░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░█
█░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░█
█░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░█
░█░░█▒▒hahahaha▒▒▒▒█░░░░█
░░█░░█▒▒▒▒▒░░░░░░▒█░░░░█░
░░░█░░█▒▒▒░░░░░░░█░░░██░░
░░░░██░▀▀▀▀▀▀▀▀▀▀░░░█░░░░
░░░░░░▀▀▀▀██████▀▀▀▀░░░░░
█████████████████████████
'''