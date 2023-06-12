import os
import random
import array


def encontrar_sala_por_codigo(codigo):
    for sala in os.scandir('Data_Bases/Salas/'):
        if codigo == sala.name.split('-')[0]:
            nome = sala.name
    path = f'Data_Bases/Salas/{nome}'
    try:
        with open(path,'r', encoding='utf-8',newline='\n') as sala:
            return sala.readlines()
    except EOFError:
        print('\33[31mErro ao carregar arquivo de banco de salas,\nSe o problema persistir reinicie o programa e contate os devs\33[m')


def criacao_de_sala(index_professor,jornada):
    codigo = criador_de_chave_da_sala()
    nome = f'{codigo}-{jornada}-Prof-{index_professor}.csv'
    diretorio = f'Data_Bases/Salas/{nome}'
    try:
        with open(diretorio,'x', encoding='utf-8') as sala:
            sala.write('index,nome,email,ultima pergunta,pontuação,')
        print('\33[32mSala Criada com Sucesso!\33[m')
        print(f'\33[32mCódigo da sala:{codigo}\33[m')
        input('Digite algo para continuar!')
        os.system('cls')
        
    except EOFError:
        print('\33[31mErro ao carregar arquivo de banco de salas,\nSe o problema persistir reinicie o programa e contate os devs\33[m')



def criador_de_chave_da_sala():
    MAX_LEN = 6
    DIGITOS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LETRAS_MINUSCULAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r',
                         's','t', 'u', 'v', 'w', 'x', 'y','z']
    LETRAS_MAIUSCULAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R',
                        'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    
    LISTA_COMBINADA = DIGITOS + LETRAS_MINUSCULAS + LETRAS_MAIUSCULAS
    rand_digit = random.choice(DIGITOS)
    rand_upper = random.choice(LETRAS_MINUSCULAS)
    rand_lower = random.choice(LETRAS_MAIUSCULAS)
    temp_code= rand_digit + rand_upper + rand_lower
    for x in range(MAX_LEN - 4):
        temp_code= temp_code+ random.choice(LISTA_COMBINADA)
        temp_pass_list = array.array('u', temp_code)
        random.shuffle(temp_pass_list)
    codigo = ""
    for x in temp_pass_list:
        codigo = codigo + x

    return codigo
    


def adicionar_aluno(index,nome,email,codigo):
    for sala in os.scandir('Data_Bases/Salas/'):
        if codigo == sala.name.split('-')[0]:
            nome = sala.name
    path = f'Data_Bases/Salas/{nome}'
    try:
        with open(path,'a', encoding='utf-8',newline='\n') as sala:
            sala.write(f'{index},{nome},{email},0,0,')
    except EOFError:
        print('\33[31mErro ao carregar arquivo de banco de salas,\nSe o problema persistir reinicie o programa e contate os devs\33[m')


#criacao_de_sala(index_professor=2,jornada='Jornada_Chico.txt')    