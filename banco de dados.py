
#Funções 






from codecs import utf_16_be_encode


def li():
    print('='*20)

def criar():
    #Criar ficha
    nome = input('Digite seu nome: ')
    namefile = nome + '.txt'
    with open(namefile,'w') as file:
        file.close()
        print('Arquivo criado!')

def mostra_escrever():
    
    import os 

    
    file = os.listdir()

    for arquivos in file:
        if '.txt' in arquivos:
            print(arquivos)
    try:
        escolha = input('Digite nome do arquivo: ')
        txt = escolha + '.txt'
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    except Exception as erro:
        print(f'Erro : {erro.__class__}')
    else:
        print('Digite o texto')
        texto = input('Texto: ')
        with open(txt,'a',encoding="utf-8") as file:
            file.write(f'{texto} \n')
        with open(txt,'r') as file:
            print(file.read())
    



#Mostrar as opções 
while True:
    print('Banco de dados')
    li()
    print('''
    [0] Criar novo Ficha
    [1] Mostra e Escrver no seu Ficha
    [2] Sair 
    ''')
    li()

    try:
        opção = int(input('Escolha: '))
    except ValueError:
        print('Digite um dos números das opções! ')
        print('Tente novamente!')
        continue
    except Exception as erro:
        print(f'{erro.__class__}')
        break
    else:
        if opção == 0:
            criar()
            continue
        elif opção == 1:
            mostra_escrever()
            continue
        elif opção == 2:
            print('Saindo...')
            break

