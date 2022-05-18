import bd_pedidos as bp
def consulta():
    tipos_consultas = ['1) - Checkup geral', '2) - Ultrassongrafia', '3) - Exame de sangue', '4) - Exame de fezes', '5) - Exame de urina', '6) - Exame oftalmológico', '7) - Exame odontológico', '8) - Temeperatura corporal', '9) - Endoscopia']

    print('°---------------------------°')
    for item in tipos_consultas:
        print('|', item)
    print('°---------------------------°')

def tosa():
    turnos = ['1) - Manhã','2) - Tarde']
    horarios_manha = ['6:00', '8:00', '10:00']
    horarios_tarde = ['13:00', '15:00', '17:00']
    VALOR = '50.00'
    print(turnos[0])
    print(turnos[1])

    op = int(input("Selecione o turno >>> "))
    
    if op == 1:
        print(turnos[0])
        for h in horarios_manha:
            print('\n',h, 'Horas')
        print("Valor da Tosa: R$50.00")
        escolha = input('Confirmar Tosa [S]- Sim / [N] - Não >>> ')
        if escolha == 'S' or 's':
            dia = input("Diga-nos o dia que deseja (seg a sex)>>> ")
            horario = input("Informe o  horario >>> ")
            bp.pedido_tosa(dia, horario, VALOR)

    elif op == 2:
        print(turnos[1])
        for h in horarios_tarde:
            print(h, 'Horas\n')
        print("Valor da Tosa: R$50.00\n")
        escolha = input("Confirmar Tosa [S]- Sim / [N] - Não")
        if escolha == 'S' or 's':
            dia = input("Diga-nos o dia que deseja (seg a sex)>>> ")
            horario = input("Informe o  horario >>> ")
            bp.pedido_tosa(dia, horario, VALOR)

def banho ():
    horarios_manha = ["1) - 8:00", "2) - 10:00", "3) - 12:00"]
    horarios_tarde = ["1) - 14:00", "2) - 16:00", "3) - 18:00"]
    print('''\nTurnos:
    1) - Manhã
    2) - Tarde\n''')

    turno = int(input('Selecione um turno >>> '))

    if (turno == 1):
        print("\n____________\n")
        for hora in horarios_manha:
            print("|", hora)
        print("\n____________\n")


    elif (turno == 2):
        print("\n____________\n")
        for hora in horarios_tarde:
            print("|", hora)
        print("\n____________\n")