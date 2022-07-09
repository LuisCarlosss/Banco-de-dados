import banco_dados as banco

while True:
    print('''
    [1] Criar arquivo um arquivo de texto
    [2] Exibir arquivos de texto criados
    [3] Escrever dentro do arquivo de texto  
    [4] sair do sistema\n''')

    opção = int(input('Escolha uma opção:'))

    try:
        if opção == 1:
            banco.verificar_se_arquivo_existe()
            
        elif opção == 2:
            banco.exibir_arquivo()
            
        elif opção == 3:
            banco.escrever_no_arquivo()

        elif opção == 4:
            print('Você saiu do sistema!')
            break

    #Verificar se digitou um numero inteiro
    except ValueError:
        print('Erro: Digite um número inteiro')
        continue
    except Exception as erro:
        print(f'Erro: {erro.__class__}')
        continue






