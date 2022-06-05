#Criar um sistema simples de banco de dados 

#Funções 
    #Verifica se arquivo existe, Senão criar o arquivo 
def verificar():
    namefile = input('arquivo:')
    arquivo = namefile + '.txt'
    
    try:
        with open(arquivo) as file:
            file.close()

    except FileNotFoundError:
        print('Arquivo não encontrado!')
        print('Criando arquivo...')

    except Exception as erro:
        print(f'Erro: {erro.__class__}')

    else:
        print('Arquivo já Existe')   

    #Criar o arquivo
    def criar():
        with open(arquivo,'w')as file:
            file.close()
    criar()

    #Mostar os arquivos 
def mostrar():
    import os 

    arquivos = os.listdir()

    for arquivo in arquivos:
        if '.txt' in arquivo:
            print(arquivo)


    #Escrevar os arquivos 

def escrever():
    mostrar()

    print('Escolha o arquivo')
    namefile = input(':')
    arquivo = namefile + '.txt'
    
    import os 
    file = os.listdir()
    if arquivo in file:
        with open(arquivo,'a',encoding='utf-8')as file:
            print('Escreva no arquivo!')
            texto = str(input(':'))
            file.write(f'{texto}\n')
        with open(arquivo,'r',encoding='utf-8') as file:
            print('dentro do arquivo\n')
            print(file.read())
    else:
        print('Não existe nenhum arquivo com esse nome!')
#Loop infinito 

#Mostrar as opções 
while True:

    print('''
    [1] Criar arquivo
    [2] Mostrar arquivos 
    [3] Escrever no arquivo  
    [4] sair\n''')

    opção = int(input('Escolha uma opção:'))

    #Escolher um opção 

    #Estrutura de condição
    try:
        if opção == 1:
            verificar()
            continue
        elif opção == 2:
            mostrar()
            continue
        elif opção == 3:
            escrever()
            continue
        elif opção == 4:
            break
        else:
            pass
    except ValueError:
        print('Erro: Digite um número inteiro')
        continue
    except Exception as erro:
        print(f'Erro: {erro.__class__}')
    else:
        pass






