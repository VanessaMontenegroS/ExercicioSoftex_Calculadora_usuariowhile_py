#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código
# deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará
# a seguinte lista de operações:
#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair

#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve
# mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.
#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois
# precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema
# irá parar.
#É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.



def adicao(a, b):
    return (n1 + n2)


def subtracao(a, b):
    return (n1 - n2)


def multiplicacao(a, b):
    return (n1 * n2)


def divisao(a, b):
    return (n1 / n2)


def cabecalho():
    print('-' * 20)
    print('    CALCULADORA    ')
    print('-' * 20)
    print('''    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão
    0. Sair''')
    print('-' * 20)


x = 1
while x != 0:
    print(' ')
    cabecalho()
    x = int(input('\nDigite o número para a operação correspondente: '))
    if x == 1:
       print('\nOpção escolhida: SOMA ')
    elif x == 2:
        print(' ')
        print('\nOpção escolhida: SUBTRAÇÃO ')
    elif x == 3:
        print(' ')
        print('\nOpção escolhida: MULTIPLICAÇÃO ')
    elif x == 4:
        print(' ')
        print('\nOpção escolhida: DIVISÃO ')
    elif x > 4:
        print(' ')
        print('\nEsta opção não existe. ')
        print(' ')
        cabecalho()
        x = int(input('\nDigite o número para a operação correspondente: '))
    else:
        x == 0
        print('\nProcesso encerrado. \n')
        exit(0)

    n1 = float(input('\nDigite o primeiro número: \n'))
    n2 = float(input('\nDigite o segundo número: \n'))

    if x == 1:
        print(' \n=> Resultado da soma entre ',  n1, 'e', n2,  'é', float(adicao(n1, n2)))
    if x == 2:
        print(' \n=> Resultado da subtração entre ',  n1, 'e', n2,  'é', float(subtracao(n1, n2)))
    if x == 3:
        print(' \n=> Resultado da multiplicação entre ',  n1, 'e', n2,  'é', float(multiplicacao(n1, n2)))
    if x == 4 and n2 == 0:
        print(' \n=> Não se pode dividir por zero!')
    elif x == 4:
        print(' \n=> Resultado da divisão entre ', n1, 'e', n2, 'é', float(divisao(n1, n2)))



