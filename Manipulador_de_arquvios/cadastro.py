import os
from Manipulador_de_arquvios import verificacoes as ver
from Manipulador_de_arquvios import manipulador_de_salas


def cadastro_aluno(arq):
    os.system('cls')
    arq = ver.verificador_de_banco_de_dados(arq,ver.Bancos.CADASTRO_ALUNO)
    index = ver.ler_ultimo_index(arq)
    nome = ver.verificador_de_nome_valido('Digite o nome para cadastro: ')
    email = ver.verifica_email('Digite o email para cadastro: ')
    senha = ver.verificador_de_senha_valida('Digite uma senha: ')
    sala = ver.verificador_de_sala('Digite o código da sua sala: ')
    with open(arq,'a',encoding='utf-8', newline='\n') as arquivo:
        arquivo.write(f"{index +1},{nome},{email},{senha},{sala},\n")
    manipulador_de_salas.adicionar_aluno(index=index,nome=nome,email=email,codigo=sala)


def cadastro_professor(arq):
    os.system('cls')
    arq = ver.verificador_de_banco_de_dados(arq,ver.Bancos.CADASTRO_PROFESSOR)
    index = ver.ler_ultimo_index(arq)
    nome = ver.verificador_de_nome_valido('Digite o nome para cadastro: ')
    email = ver.verifica_email('Digite o email para cadastro: ')
    senha = ver.verificador_de_senha_valida('Digite uma senha: ')

    with open(arq,'a',encoding='utf-8', newline='\n') as arquivo:
        arquivo.write(f"{index +1},{nome},{email},{senha},0,\n")


#cadastro_aluno('cadastros_alunos.csv')
#cadastro_professor('cadastros_professores.csv')