import os
from time import sleep

from Manipulador_de_arquvios import manipulador_de_DB
from Manipulador_de_arquvios import manipulador_de_jornada
from Manipulador_de_arquvios import manipulador_de_salas
from Manipulador_de_arquvios import cadastro
from Manipulador_de_arquvios import login
from Formatacao.formatacao_menu import *

os.system("cls")


while True:
    manipulador_de_DB.inicializador_de_data_bases()
    os.system('cls')
    cabeçalho('MENU')
    resposta = menu(['Cadatro','Login','Encerrar'])
    
    if resposta == 1:
        while True:
            os.system('cls')
            print(linha())
            resposta2 = menu(['Professor', 'Aluno', 'Voltar'])
            if resposta2 == 1:
                cadastro.cadastro_professor('cadastros_professores.csv')
                sleep(1)
            elif resposta2 == 2:
                cadastro.cadastro_aluno('cadastros_alunos.csv')
                sleep(1)
            elif resposta2 == 3:
                break
            sleep(1)
    elif resposta == 2:
        while True:
            os.system("cls")
            print(linha())
            resposta = menu(['Professor', 'Aluno', 'Voltar'])
            if resposta == 1:
                perfil = login.login('cadastros_professores.csv',login.ver.Bancos.CADASTRO_PROFESSOR)
                while True:
                    os.system("cls")
                    resposta = menu(['Criar Sala', 'Lista das Suas Salas', 'Voltar'])
                    if resposta == 1:
                        jornada = manipulador_de_jornada.escolhedor_de_jornadas()
                        tamanho = manipulador_de_jornada.escolhedor_de_tamanho()
                        manipulador_de_salas.criacao_de_sala(perfil[0],jornada,tamanho)

                    elif resposta == 2:
                        pass
                    elif resposta == 3:
                        print('\033[32mVoltando...\033[m')
                        break
                    else:
                        print('\033[31mERRO: por favor, digite uma das opções.\033[m')
                        sleep(1)

            elif resposta == 2:
                perfil = login.login('cadastros_alunos.csv',login.ver.Bancos.CADASTRO_ALUNO)
                index_aluno = perfil[0]
                sala = perfil[4]
                manipulador_de_jornada.jogar_jornada(sala=sala,index_aluno=index_aluno)
            elif resposta == 3:
                print('\033[32mVoltando...\033[m')
                break
            else:
                print('\033[31mERRO: por favor, digite uma das opções.\033[m')
            sleep(1)
    elif resposta == 3:
        break
    else:
        print('\033[31mERRO: por favor, digite uma das opções.\033[m')