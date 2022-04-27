
contador = 0
vezes = int(input('Bem-vinde ao conversor de moedas, você quer converter quantos valores?.'))
moeda = input('Por favor, escolha qual moeda você quer converter: \nDólar[1];\nYenes[2];\nLibra esterlina[3].')

if moeda == '1':
    print('Bem vinde ao conversor de Real para Dólar!')
    while contador < vezes:
        contador = contador + 1
        Real = int(input(f'Qual o {contador}º valor em R$?'))
        Conversao = 5 * Real
        print(f'Esse valor fica {Conversao} dólares.')
    print('Obrigade por utilizar o Conversor de Moedas! \nAté mais!')

if moeda == '2':
    print('Bem vinde ao conversor de Real para Yene!')
    while contador < vezes:
        contador = contador + 1
        Real = int(input(f'Qual o {contador}º valor em R$?'))
        Conversao = 25.62 * Real
        print(f'Esse valor fica {Conversao} yenes.')
    print('Obrigade por utilizar o Conversor de Moedas! \nAté mais!')

if moeda == '3':
    print('Bem vinde ao conversor de Real para Libras Esterlinas!')
    while contador < vezes:
        contador = contador + 1
        Real = int(input(f'Qual o {contador}º valor em R$?'))
        Conversao = 6 * Real
        print(f'Esse valor fica {Conversao} libras esterlinas.')
    print('Obrigade por utilizar o Conversor de Moedas! \nAté mais!')