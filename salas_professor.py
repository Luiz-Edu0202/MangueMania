import os
os.system('cls')

from random import randint

def criar_sala():
    while True:
        nome = input("\nCrie um nome para essa sala: ").strip().upper()
        
        while True:
            tamanho = input("Escolha o tamanho das jornadas [curta/normal]: ").strip().capitalize()

            if tamanho != 'Curta' and tamanho != 'Normal':
                print("Por favor escolha uma opção válida\n")
            else:
                break
        
        caracteres = 'abcdefghijklmnopqrstuvwxyz1234567890'
        codigo = ''

        for _ in range(8):
            codigo += caracteres[randint(0, 35)]

        arquivo.write(f"Nome: {nome} - Tamanho das Jornadas: {tamanho} - Código da Sala: {codigo}\n")

        print("Sala criada com sucesso!\n")
        break


while True:
    with open("Projetos 1\salas_professor.txt", "r+") as arquivo:
        dados = arquivo.readlines()

        if dados == []:
            print("Nenhuma sala encontrada, por favor crie uma seguindo os passos abaixo\n")
            criar_sala()

        else:
            opcoes = ['+']
            print("-=" * 50)
        
            for i in range(len(dados)):
                sala = dados[i].split(' - ')
                nome_sala = sala[0]

                print(f"{i + 1}) {nome_sala}")
                opcoes.append(str(i + 1))
            print()

            while True:
                escolha = input("Digite o número de uma sala para ve-la com mais detalhes ou digite '+' para criar uma nova sala: ").strip()

                if escolha not in opcoes:
                    print("Por favor escolha uma opção válida\n")
                else:
                    if escolha == '+':
                        sair = False
                        criar_sala()
                        break
                    else:
                        sair = True
                        print(f"\n{dados[int(escolha) - 1]}")
                        break

            if sair == True:
                break