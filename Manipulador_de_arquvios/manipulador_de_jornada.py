import os
import verificacoes as ver
import manipulador_de_salas as salas

zumbi = 'Jornada_Nacao_Zumbi.txt'
chico = 'Jornada_Chico.txt'


def jogar_jornada(sala,index_aluno):
    pontos = 0
    sala = salas.encontrar_sala_por_codigo(sala)
    diretorio = 'Data_Bases/Jornadas/' + jornada
    jornada = leitor_das_perguntas_objetivas_por_jornada(diretorio)
    

def leitor_das_perguntas_objetivas_por_jornada(arq):
    diretorio = 'Data_Bases/Jornadas/' + arq
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


leitor_das_perguntas_objetivas_por_jornada(chico)