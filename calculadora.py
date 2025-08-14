def calculadora():
    while True:
        print('----CALCULADORA----')
        print('1. Somar')
        print('2. Subtrair')
        print('3. Multiplicar')
        print('4. Dividir')
        print('5. Sair')

        escolha = input('Escolha uma operação (1/2/3/4/5): ')

        if escolha == '5':
            print('Saindo da calculadora...')
            break

        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        if escolha == '1':
            print(f'{num1} + {num2} = {num1 + num2}')
        elif escolha == '2':
            print(f'{num1} - {num2} = {num1 - num2}')
        elif escolha == '3':
            print(f'{num1} * {num2} = {num1 * num2}')
        elif escolha == '4':
            if num2 != 0:
                print(f'{num1} / {num2} = {num1 / num2}')
            else:
                print('ERRO! Não é possível dividir por zero.')
        else:
            print('Essa opção não existe. Tente novamente.')

calculadora()
