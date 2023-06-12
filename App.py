import os
from time import sleep

from Formatacao.formatacao_menu import *
from Manipulador_de_arquvios import cadastro
from Manipulador_de_arquvios import login

os.system("cls")


while True:
    sleep(1)
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
                cadastro.cadastro_professor('cadastros_alunos.csv')
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
                login.login('cadastros_professores.csv',login.ver.Bancos.CADASTRO_PROFESSOR)
            elif resposta == 2:
                login.login('cadastros_alunos.csv',login.ver.Bancos.CADASTRO_ALUNO)
            elif resposta == 4:
                print('\033[32mVoltando...\033[m')
                break
            else:
                print('\033[31mERRO: por favor, digite uma das opções.\033[m')
            sleep(1)
    elif resposta == 3:
        break
    else:
        print('\033[31mERRO: por favor, digite uma das opções.\033[m')