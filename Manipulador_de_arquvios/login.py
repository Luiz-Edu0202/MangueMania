from Manipulador_de_arquvios import verificacoes as ver
from time import sleep
import os
import csv


def login(arq,Banco:ver.Bancos):
    cadastros = []
    arq = ver.verificador_de_banco_de_dados(arq,Banco)
    with open(arq,'r',encoding='utf-8', newline='\n') as arquivo:
        arquivo_csv = csv.reader(arquivo)
        for cadastro in arquivo_csv:
            cadastros.append(cadastro)
    while True:
        email = ver.verifica_email('Digite o email para cadastro: ')
        senha = ver.verificador_de_nome_valido('Digite uma senha: ')
        for cadastro in cadastros:
            if cadastro[2] == email.lower() and cadastro[3] == senha:
                print('\n\033[32mLogin feito com sucesso!\033[m')
                return cadastro[0]
        else:
            print('\n\033[31mLogin ou senha Inválidos.\033[m')
            print(cadastro)
            sleep(2)
            os.system('cls')

#print(login('cadastros_alunos.csv',ver.Bancos.CADASTRO_ALUNO))