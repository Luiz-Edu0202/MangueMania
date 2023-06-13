import os


arquivos_cadastro_nome = ['cadastros_alunos.csv','cadastros_professores.csv']

diretorio_cadastros = 'Data_Bases/Cadastros/'
diretorio_jornadas = 'Data_Bases/Jornadas/'
diretorio_salas = 'Data_Bases/Salas/'

def inicializador_de_data_bases():
    
    if not(os.path.exists(diretorio_cadastros+arquivos_cadastro_nome[0])):
        with open(diretorio_cadastros+arquivos_cadastro_nome[0],'x',encoding='utf-8') as arquivo:
            arquivo.write('index,nome,email,senha,sala,\n')
    
    if not(os.path.exists(diretorio_cadastros+arquivos_cadastro_nome[1])):
        with open(diretorio_cadastros+arquivos_cadastro_nome[1],'x',encoding='utf-8') as arquivo:
            arquivo.write('index,nome,email,senha,numero de salas,\n')
    
