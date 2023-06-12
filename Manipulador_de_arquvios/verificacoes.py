import os
import csv
from enum import Enum
from time import sleep

from zxcvbn import zxcvbn as verificador_senha
from validate_email_address import validate_email


class Bancos(Enum):
    CADASTRO_ALUNO = 1
    CADASTRO_PROFESSOR = 2
    SALA = 3
    jORNADA = 4


def verificador_de_banco_de_dados(arq,Banco:Bancos):
    diretorio = ''
    if (Banco == Bancos.CADASTRO_ALUNO) and (os.path.exists('Data_Bases/Cadastros/'+ arq)):
        diretorio = 'Data_Bases/Cadastros/'+ arq
    elif (Banco == Bancos.CADASTRO_PROFESSOR) and (os.path.exists('Data_Bases/Cadastros/'+ arq)):
        diretorio = 'Data_Bases/Cadastros/'+ arq
    elif (Banco == Bancos.jORNADA) and(os.path.exists('Data_Bases/Jornadas/'+ arq)):
        diretorio = 'Data_Bases/Jornadas/'+ arq
    elif (Banco == Bancos.SALA) and (os.path.exists('Data_Bases/Salas/'+ arq)):
        diretorio = 'Data_Bases/Salas/'+ arq
    return diretorio


def verifica_int(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return num


def verifica_email(msg):
    while True:
        try:
            email = input(msg).lower()
            valido = validate_email(email)
            if valido:
                print('\033[32mEmail válido.\033[m')
                sleep(2)
                os.system('cls')
                return email
            else:
                print('\033[31mERRO: Email Inválido, por favor digite um email válido.\033[m')
                sleep(2)
                os.system('cls')
        except (KeyboardInterrupt):
            print('\n\033[31mpor favor digite um email para cadastro.\033[m')
            sleep(2)
            os.system('cls')
        except:
            print('\033[31mERRO: Email Inválido, por favor digite um email válido.\033[m')
            sleep(2)
            os.system('cls')

        
def verificador_de_nome_valido(msg):
    valor = input(msg)
    if valor.find(',') == -1:
        return valor
    else:
        print('\33[31mValor Inválido indentificado: virgula(,)\33[m')
        sleep(0.5)
        print('\33[32mSubstituindo virgula(,) por hífen(-)\33[m')
        sleep(2)
        return valor.replace(',','-')


def ler_ultimo_index(path):
    memoria_csv = []
    with open(path,'r',encoding='utf-8', newline='\n') as file:
        csvreader = csv.reader(file)
        for linha in csvreader:
            memoria_csv.append(linha)
    if len(memoria_csv) > 2:
        ultima_linha = memoria_csv[len(memoria_csv)-1]
        return (int(ultima_linha[0]))
    else:
        return(0)


def verificador_de_senha_valida(msg):
    while True:
        try:
            senha = input(msg)
            resultado = verificador_senha(senha)['score']
            feedback = verificador_senha(senha)['feedback']['suggestions']
            if resultado >= 2:
                print('\n\033[32msenha válida!\033[m')
                sleep(2)
                os.system('cls')
                return senha
            else:
                print('\n\033[31mpor favor digite uma senha mais forte.\033[m')
                for output in feedback:
                    print(f'\n\033[31m{output}\033[m')
                sleep(2)
        except (KeyboardInterrupt):
            print('\n\033[31mpor favor digite uma senha para cadastro.\033[m')
            sleep(2)
            os.system('cls')
        except:
            print('\033[31mERRO: senha Inválida, por favor digite uma senha válida.\033[m')
            sleep(2)
            os.system('cls')



def verificador_de_sala(msg):
    while True:
        sala_codigo = input(msg)
        for codigo in os.scandir('Data_Bases/Salas/'):
            if sala_codigo == codigo.name.split('-')[0]:
                print('\n\033[32mSala Encontrada!\033[m')
                return sala_codigo
        else:
            print('\n\033[31mpor favor verifique novamente o código.\033[m')

    
