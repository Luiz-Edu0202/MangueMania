import os
os.system('cls')

def ler_dados():
    read = open('Projetos Pessoais\Original\dados.txt', 'r')
    d = read.readlines()
    read.close()
    return d

def atualizar_dados(apagar=False):
        if apagar == False:
            write = open('Projetos Pessoais\Original\dados.txt', 'w')
            write.writelines(f'True\n{usuario}\n{senha}')
            write.close()
            print("Cadastro atualizado com sucesso!\n")

        elif apagar == True:
            write = open('Projetos Pessoais\Original\dados.txt', 'w')
            write.writelines('False')
            write.close()
            print("Cadastro apagado do sistema!\n")

def verificar_dados():
    usuario = input("\nDigite seu nome de usuário: ")
    senha = input("Digite a sua senha: ")
    return usuario == dados[1].strip() and senha == dados[2].strip()

def pegar_dados():
    usuario = input("Digite um nome de usuário para cadastrar: ")
    senha = input("Digite uma senha para fazer o cadastro: ")
    return usuario, senha

while True:
    dados = ler_dados()

    if dados[0] == 'False':
        print("Nenhum cadastro encontrado, por favor siga os passas a seguir...")
        usuario, senha = pegar_dados()
        atualizar_dados()

    elif dados[0].strip() == 'True':
        print("Cadastro encontrado, por favor siga as instruções abaixo...")
        escolha = input("""[1] Acessar a página
[2] Atualizar cadastro
[3] Apagar cadastro
Digite o número da sua escolha: """)

        if escolha == '1':
            if verificar_dados() == True:
                print("\nParabéns, você tem acesso a página!\n")
                break
            else:
                print("\nUsuário ou senha errada, por favor tente de novo.\n")

        elif escolha == '2':
            if verificar_dados() == True:
                print()
                usuario, senha = pegar_dados()
                atualizar_dados()
                break
            else:
                print("\nUsuário ou senha errada, por favor tente de novo.\n")

        elif escolha == '3':
            if verificar_dados() == True:
                conf = input("\nTem certeza que deseja apagar seu cadastro? [S/N]: ").lower()

                if conf == 's':
                    atualizar_dados(apagar=True)
                    break
                elif conf == 'n':
                    print()
                else:
                    print("Escolha inválida! Por favor tente de novo.\n")