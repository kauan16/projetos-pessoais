while True:
    num_one = input('digite o primeiro valor: ')
    num_two = input('digite o segundo valor: ')
    print('OBS: (*)multiplicação, (/) divisão, (+)soma e (-)subtração. ')
    Operators = input('escolha um dos operadores (*/+-): ')

    valid_num = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(num_one)
        num_2_float = float(num_two)
        valid_num = True
    except:
        valid_num = None

    if valid_num is None:
        print('um ou ambos os números são inavlidos')
        continue
    
    Operators_allowed = '*/+-'

    if Operators not in Operators_allowed:
        print('operador incompativel.')
        continue
    if len(Operators) > 1:
        print('digite apenas um operador.')
        continue
    print('realizando sua conta. confira o resultado: ')
    if Operators == '+':
        print(f'{num_1_float} + {num_2_float}, o resultado é = ', num_1_float + num_2_float)
    
    elif Operators == '-':
        print(f'{num_1_float} - {num_2_float}, o resultado é = ', num_1_float - num_2_float)

    elif Operators == '*':
        print(f'{num_1_float} x {num_2_float}, o resultado é = ', num_1_float * num_2_float)

    elif Operators == '/':
        print(f'{num_1_float} % {num_2_float}, o resultado é = ', num_1_float / num_2_float)

    else:
        print('algo deu errado.')

    sair = input('deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        print('calculadora encerrada.')
        break



        