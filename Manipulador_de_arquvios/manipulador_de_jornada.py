import os
from enum import Enum
from Manipulador_de_arquvios import verificacoes as ver
from Manipulador_de_arquvios import manipulador_de_salas as salas

zumbi = 'Jornada_Nacao_Zumbi.txt'
chico = 'Jornada_Chico.txt'

class Tamanho(Enum):
    LONGA = 1
    CURTA = 2



def atualizar_pontacao(codigo,index_aluno,pontuacao):
    lista_alunos = []
    for sala in os.scandir('Data_Bases/Salas/'):
        if codigo == sala.name.split('-')[0]:
            nome = sala.name
    path = f'Data_Bases/Salas/{nome}.csv'
    try:
        with open(path,'r', encoding='utf-8',newline='\n') as sala:
            lista_alunos = sala.readlines()
            for aluno in len(1,lista_alunos):
                aluno_info = lista_alunos[aluno].spli(',')
                if index_aluno == aluno_info[0]:
                    pontos = int(aluno_info[5])
                    pontos += pontuacao
                    lista_alunos[aluno] = f'{aluno_info[0]},{aluno_info[1]},{aluno_info[2]},{aluno_info[3]},{aluno_info[4]},{pontos},'

        with open(path,'w', encoding='utf-8',newline='\n') as sala:
            sala.writelines(lista_alunos)
    except EOFError:
        print('\33[31mErro ao carregar arquivo de banco de salas,\nSe o problema persistir reinicie o programa e contate os devs\33[m')


def jogar_jornada(sala,index_aluno):
    pontos = 0
    jornada = salas.encontrar_sala_por_codigo(sala).split('-')[1]
    tamanho = salas.encontrar_sala_por_codigo(sala).split('-')[2]
    diretorio = f'Data_Bases/Jornadas/{jornada}.txt'
    perguntas = leitor_das_perguntas_objetivas_por_jornada(diretorio)

    if tamanho == 'CURTA':
        for i in range(3):
            os.system('cls')
            pergunta = perguntas[i].split('%')[0]
            correto = perguntas[i].split('%')[1]
            reposta = input(pergunta)
            if reposta == correto:
                pontos +=1
                atualizar_pontacao(sala,index_aluno,pontos)
    if tamanho == 'LONGA':
        for i in range(5):
            os.system('cls')
            pergunta = perguntas[i].split('%')[0]
            correto = perguntas[i].split('%')[1]
            reposta = input(pergunta)
            if reposta == correto:
                pontos +=1
                atualizar_pontacao(sala,index_aluno,pontos)
    

def leitor_das_perguntas_objetivas_por_jornada(diretorio):
    sessoes = []
    perguntas = []
    try:
        with open(diretorio, 'r', encoding='utf-8') as arquivo:
            arquivo_str = arquivo.read()
            sessoes = arquivo_str.split('###')
            perguntas = sessoes[0].split('/')
        return perguntas
                
    except:
        print('\33[31mErro ao carregar arquivo de banco de dados da jornada,\nSe o problema persistir reinicie o programa e contate os devs \33[m')


def escolhedor_de_jornadas():
    index = 1
    jornadas_nomes = []
    print('Escolha uma das jornadas disponíveis:')
    for jornada in os.scandir('Data_Bases/Jornadas/'):
        print(index,'-',jornada.name.split('.')[0])
        jornadas_nomes.append(jornada.name.split('.')[0])
        index += 1
    while True:
        escolha = ver.verifica_int('Digite o indice da jornada de sua escolha: ')
        if escolha > index or escolha <= 0:
            print('\033[31mERRO: número fora do intervalo das opções.\033[m')
            print('\033[31mPor favor escolha uma jornada existente.\033[m')
        else:
            print('\033[32mJornada Selecionada!\033[m')
            return jornadas_nomes[escolha-1]
        

def escolhedor_de_tamanho():
    print('Tamanhos disponíveis para a jornada:')
    print(f'1 - {Tamanho.CURTA.name}')
    print(f'2 - {Tamanho.LONGA.name}')
    while True:
        escolha = ver.verifica_int('Digite o indice da sua escolha: ')
        if escolha > 2 or escolha <= 0:
            print('\033[31mERRO: número fora do intervalo das opções.\033[m')
            print('\033[31mPor favor escolha um tamanho existente.\033[m')
        else:
            print('\033[32mJornada Selecionada!\033[m')
            if escolha == 1:
                return str(Tamanho.CURTA.name)
            elif escolha == 2:
                return str(Tamanho.LONGA.name)
            