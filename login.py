import os
os.system("cls")

#---------------------------------------- Login/Cadastro ----------------------------------------
with open("Projetos 1\login.txt", "r+") as arquivo:
    dados = arquivo.read()

    # Caso não haja dados salvos no banco de dados, começar o cadastro
    if dados.strip() == '':
        print("CADASTRO")
        
        while True:
            # Pergunta se é aluno ou professor
            ocupacao = input("\nEscreva sua escolha - Eu sou [Aluno/Professor]: ").strip().capitalize()

            # Se a resposta não for aluno nem professor, perguntar novamente
            if ocupacao != 'Aluno' and ocupacao != 'Professor':
                print("Por favor escreva uma opção válida")
            else:
                break
        
        # Pede o nome completo
        nome = input("\nDigite o seu nome completo: ").strip().title()

        while True:
            # Pede o email
            email = input("\nDigite um email para o cadastro: ").strip()

            # Verifica se tem @
            if '@' in email:
                break
            else:
                print("Por favor digite um email válido")

        while True:
            # Pede pra criar uma senha e confirmar
            senha = input("\nDigite uma senha para o cadastro: ").strip()
            confirmacao = input("Confirme sua senha: ").strip()

            # Verifica se a senha e a confirmação estão iguais
            if senha == confirmacao:
                break
            else:
                print("Senha diferente da confirmação, por favor tente novamente")

        # Escreve as informações para o arquivo/banco de dados
        arquivo.write(f"{ocupacao}, {nome}, {email}, {senha}")
        print("\nCadastro realizado com sucesso!")


    else:
        print("LOGIN")

        # Cria uma lista com formato [ocupação, nome completo, email, senha]
        dados = dados.split(', ')
        email_salvo = dados[2]
        senha_salva = dados[3]

        while True:
            # Pede para digitar email e senha
            email = input("\nDigite seu email: ")
            senha = input("Digite sua senha: ")

            # Verifica se ambos estão corretos
            if email == email_salvo and senha == senha_salva:
                print("\nAcesso à plataforma liberado!")
                break
            else:
                print("Email ou senha incorretos, por favor tente novamente")
#------------------------------------------------------------------------------------------------