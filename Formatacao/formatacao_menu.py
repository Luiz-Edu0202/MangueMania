def linha(tamanho = 42):
    return "-" * tamanho


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return num


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def topicos(topicos):
    print()
    for topico in topicos:
        print(topico.ljust(42))
    print(linha())


def menu(sessoes):
    opcao = 1
    for item in sessoes:
        print(f'\033[34m{opcao}\033[m - \033[34m{item}\033[m')
        opcao +=1
    print(linha())
    escolha = leiaInt('\033[32mSua Opção: \033[m')
    return escolha

