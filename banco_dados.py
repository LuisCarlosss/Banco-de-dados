#Funções 
    #Verifica se arquivo existe, Senão criar o arquivo 
def verificar_se_arquivo_existe():
    namefile = input('arquivo:').capitalize()
    arquivo = namefile + '.txt'
    
    #tratando Erros
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

    
    def criar_arquivo():
        with open(arquivo,'w')as file:
            file.close()
    criar_arquivo()


def exibir_arquivo():
    import os 
    arquivos = os.listdir()

    for arquivo in arquivos:
        if '.txt' in arquivo:
            print(arquivo)

def escrever_no_arquivo():
    exibir_arquivo()

    print('Escolha o arquivo')
    namefile = input(':').capitalize()
    arquivo = namefile + '.txt'

    import os 
    file = os.listdir()

    if arquivo in file:
        with open(arquivo,'a',encoding='utf-8')as file:
            print('\nEscreva no arquivo!')
            texto = str(input(':'))
            file.write(f'{texto}\n')

        with open(arquivo,'r',encoding='utf-8') as file:
            print(f'Escrevendo Dentro do arquivo {arquivo}')
            print('='*12,'\n')
            exibir_dados = file.read()
            print(exibir_dados)
            print('='*12,'\n')
    else:
        print('Não existe nenhum arquivo com esse nome!')
