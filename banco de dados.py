#Funções

def li():
    print('='*20)
    
#Função para criar uma ficha

def criar():
    #Criar ficha 
    nome = input('Digite seu nome: ')
    namefile = nome + '.txt'
    with open(namefile,'w') as file:
        file.close()
        print('Arquivo criado!')
      
#Função para Mostra os arquivos

def mostrar():
    import os 

    file = os.listdir()
    for arquivos in file:
        if '.txt' in arquivos:
            print(arquivos)

#Função para Escrever na ficha 

def escrever():
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
    [1] Mostra ficha
    [2] Escrver no seu Ficha
    [3] Sair
    ''')
    li()

    try:
        opção = int(input('Escolha: '))
    except ValueError:
        print('Erro : Digite um dos números das opções! ')
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
            mostrar()
        elif opção == 2:
            escrever()
            continue
        elif opção == 3:
            print('Saindo...')
            break



