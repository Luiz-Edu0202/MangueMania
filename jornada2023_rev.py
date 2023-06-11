import os
import time

contc = 0
conte = 0

#CLEAR
def CLEAR():
    return os.system("cls")

#TELA INICIAL
def INICIO():
    print("-" * 76)
    print(" \t \t \t 1- JORNADA CHICO SCIENCE \t \t ")
    print(" \t \t \t 2- JORNADA MANGUE BEAT \t \t ")
    print(" \t \t \t 3- JORNADA NAÇÃO ZUMBI \t \t ")
    print(" \t \t \t 4- SAIR \t \t ")
    print("-" * 76)
    try:
        escolha = int(input("BEM VINDO A SUA JORNADA! EM QUAL CAMINHO VOCE DESEJA COMEÇAR? "))
        print("-" * 76)
        CLEAR()
        if escolha == 1:
            JORNADA1()
        if escolha == 4:
            print("Obrigado por jogar!")
            time.sleep(1.5)
            CLEAR()
            print("FIM DE JOGO")

    except ValueError:
        CLEAR()
        print("Entrada inválida. Por favor, digite um número inteiro.")
        time.sleep(1.5)
        CLEAR()
        INICIO()
    except Exception as e:
        CLEAR()
        print("Ocorreu um erro:", str(e))
        time.sleep(1.5)
        CLEAR()
        INICIO()

def JORNADA1():
    print("ASSISTA AO VÍDEO E DISSERTE SOBRE O MOVIMENTO")
    print("https://www.youtube.com/watch?v=bM0U39sWkZ4&ab_channel=ReiDerso")
    texto = str(input("Insira aqui sua opinião: "))
    CLEAR()

    print("VEJA ESSE TRECHO DE LETRA DE UMA MÚSICA O CHICO SCIENCE E DISSERTE SOBRE ELA:" "\n")
    print(" \t \t \t Andando por entre os becos \t \t ")
    print(" \t \t \t Andando em coletivos \t \t ")
    print(" \t \t \t Ninguém foge ao cheiro sujo \t \t ")
    print(" \t \t \t Da lama da manguetown \t \t ")
    print(" \t \t \t Andando por entre os becos \t \t ")
    print(" \t \t \t Andando em coletivos \t \t ")
    print(" \t \t \t Ninguém foge a vida suja \t \t ")
    print(" \t \t \t Dos dias da manguetown \t \t ")
    texto = str(input("Insira aqui sua opinião: "))
    CLEAR()

    J1_LONGA()

def J1_CURTA():
    global conte
    global contc

    print("-" * 76)
    print("SEJA BEM VINDO A PRIMEIRA ATIVIDADE!")
    print("-" * 76)
    print("PRIMEIRO QUESITO" "\n")
    print("O mangue beat foi um movimento cultural que se destacou por sua fusão de estilos musicais. Quais gêneros musicais influenciaram o mangue beat?")
    print("a) Rock, rap e jazz")
    print("b) Samba, maracatu e frevo")
    print("c) Reggae, forró e funk")
    print("d) Axé, bossa nova e baião")
    resposta = input("resposta: ").lower()
    CLEAR()
    if resposta == "b":
        print("RESPOSTA CERTA! VAMOS PARA PRÓXIMA PERGUNTA")
        time.sleep(1)
        CLEAR()
        contc += 1
    
    else:
        print("RESPOSTA ERRADA! VAMOS PARA PRÓXIMA PERGUNTA")
        time.sleep(1)
        CLEAR()
        conte += 1
    
    print("SEGUNDO QUESITO" "\n")
    print("O estilo de dança característico do mangue beat era conhecido como:")
    print("a) Maracatu beat")
    print("b) Frevo maluco")
    print("c) Axé swing")
    print("d) Ciranda hip-hop")
    resposta = input("resposta: ").lower()
    CLEAR()
    if resposta == "a":
        print("RESPOSTA CERTA, PRIMEIRA ATIVIDADE CONCLUÍDA!")
        time.sleep(1)
        CLEAR()
        contc += 1
        
    else:
        print("RESPOSTA ERRADA, PRIMEIRA ATIVIDADE CONCLUÍDA!")
        time.sleep(1)
        CLEAR()
        conte += 1

    print("TERCEIRO QUESITO" "\n")
    print("Qual foi o nome da banda que se tornou um dos principais expoentes do movimento mangue beat")
    print("a) Nação Zumbi")
    print("b) Mestre Ambrósio")
    print("c) Mundo Livre S/A")
    print("d) Chico Science & Nação Zumbi")
    resposta = input("resposta: ").lower()
    CLEAR()
    if resposta == "a":
        print("RESPOSTA CERTA, PRIMEIRA ATIVIDADE CONCLUÍDA!")
        time.sleep(1)
        CLEAR()
        contc += 1
        
    else:
        print("RESPOSTA ERRADA, PRIMEIRA ATIVIDADE CONCLUÍDA!")
        time.sleep(1)
        CLEAR()
        conte += 1

    
    print("QUARTO QUESITO" "\n")
    print("Infelizmente, Chico Science faleceu prematuramente. Sua morte impactou o mangue beat de que maneira?")
    print("a) O movimento perdeu força e foi extinto")
    print("b) Outras bandas do mangue beat se tornaram ainda mais populares")
    print("c) O movimento passou a ser liderado por artistas estrangeiros")
    print("d) O mangue beat se transformou em um estilo mais melancólico e introspectivo")
    resposta = input("resposta: ").lower()
    CLEAR()
    if resposta == "b":
        print("RESPOSTA CERTA, PRIMEIRA ATIVIDADE CONCLUÍDA!")
        time.sleep(1)
        CLEAR()
        contc += 1
        
    else:
        print("RESPOSTA ERRADA, PRIMEIRA ATIVIDADE CONCLUÍDA!")
        time.sleep(1)
        CLEAR()
        conte += 1
    
    print("QUINTO QUESITO" "\n")
    print("O estilo de dança característico do mangue beat era conhecido como:")
    print("a) Maracatu beat")
    print("b) Frevo maluco")
    print("c) Axé swing")
    print("d) Ciranda hip-hop")
    resposta = input("resposta: ").lower()
    CLEAR()
    if resposta == "a":
        print("RESPOSTA CERTA, PRIMEIRA ATIVIDADE CONCLUÍDA!")
        time.sleep(1)
        CLEAR()
        contc += 1
        
    else:
        print("RESPOSTA ERRADA, PRIMEIRA ATIVIDADE CONCLUÍDA!")
        time.sleep(1)
        CLEAR()
        conte += 1
    print("-" * 76)

def J1_LONGA():
    global conte
    global contc

    print("-" * 76)
    print("SEJA BEM VINDO A PRIMEIRA ATIVIDADE!")
    print("-" * 76)
    print("PRIMEIRO QUESITO" "\n")
    print("Qual foi a principal influência musical de Chico Science no desenvolvimento do mangue beat?")
    print("a) Rock psicodélico")
    print("b) Samba de raiz")
    print("c) Maracatu tradicional")
    print("d) Música eletrônica")
    resposta = input("resposta: ").lower()
    CLEAR()
    if resposta == "d":
        print("RESPOSTA CERTA! VAMOS PARA PRÓXIMA PERGUNTA")
        time.sleep(1)
        CLEAR()
        contc += 1
        
    else:
        print("RESPOSTA ERRADA! VAMOS PARA PRÓXIMA PERGUNTA")
        time.sleep(1)
        CLEAR()
        conte += 1
    
    print("SEGUNDO QUESITO" "\n")
    print("Em que cidade Chico Science nasceu e cresceu, e que teve grande impacto na formação do mangue beat?")
    print("a) Recife")
    print("b) Salvador")
    print("c) São Paulo")
    print("d) Rio de Janeiro")
    resposta = input("resposta: ").lower()
    CLEAR()
    if resposta == "a":
        print("RESPOSTA CERTA, PRIMEIRA CONCLUÍDA!")
        time.sleep(1)
        CLEAR()
        contc += 1
        
    else:
        print("RESPOSTA ERRADA, PRIMEIRA ETAPA CONCLUÍDA!")
        time.sleep(1)
        CLEAR()
        conte += 1

    print("TERCEIRO QUESITO" "\n")
    print("Chico Science foi um dos fundadores de qual banda que se tornou um dos pilares do mangue beat?")
    print("a) Mundo Livre S/A")
    print("b) Nação Zumbi")
    print("c) Mestre Ambrósio")
    print("d) Comadre Fulozinha")
    resposta = input("resposta: ").lower()
    CLEAR()
    if resposta == "b":
        print("RESPOSTA CERTA! VAMOS PARA PRÓXIMA PERGUNTA")
        time.sleep(1)
        CLEAR()
        contc += 1
        
    else:
        print("RESPOSTA ERRADA! VAMOS PARA PRÓXIMA PERGUNTA")
        time.sleep(1)
        CLEAR()
        conte += 1
    
    print("QUARTO QUESITO" "\n")
    print("Qual foi o primeiro álbum lançado pela banda Nação Zumbi, liderada por Chico Science?")
    print("a) Da Lama ao Caos")
    print("b) Afrociberdelia")
    print("c) Carnaval na Obra")
    print("d) Lixo Extraordinário")
    resposta = input("resposta: ").lower()
    CLEAR()
    if resposta == "a":
        print("RESPOSTA CERTA! VAMOS PARA PRÓXIMA PERGUNTA")
        time.sleep(1)
        CLEAR()
        contc += 1
    
    else:
        print("RESPOSTA ERRADA! VAMOS PARA PRÓXIMA PERGUNTA")
        time.sleep(1)
        CLEAR()
        conte += 1

    print("QUINTO QUESITO" "\n")
    print("Além da música, Chico Science também tinha um forte engajamento social. Qual era sua principal mensagem política?")
    print("a) Luta pela preservação do meio ambiente")
    print("b) Combate à desigualdade social")
    print("c) Defesa dos direitos dos animais")
    print("d) Promoção da paz mundial")
    resposta = input("resposta: ").lower()
    CLEAR()
    if resposta == "b":
        print("RESPOSTA CERTA! VAMOS PARA PRÓXIMA PERGUNTA")
        time.sleep(1)
        CLEAR()
        contc += 1
        
    else:
        print("RESPOSTA ERRADA! VAMOS PARA PRÓXIMA PERGUNTA")
        time.sleep(1)
        CLEAR()
        conte += 1

    CONCLUIDO()

#ATIVIDADE CONCLUíDA
def CONCLUIDO():
    global conte
    global contc
    encerrar = False

    print("Parabéns, você concluiu a jornada!")
    time.sleep(1)
    CLEAR()
    
    print("SEU PLACAR É...")
    time.sleep(1)
    CLEAR()
    print(f"ACERTOS: {contc}")
    print(f"ERROS: {conte}")
    encerrar = input("Digite qualquer tecla para encerrar: ")
    encerrar = True

    if True:
        CLEAR()
        INICIO()
    
INICIO()
