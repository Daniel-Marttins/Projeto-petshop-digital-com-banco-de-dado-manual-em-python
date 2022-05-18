import sistema_servicos as ss
def menu_servicos():
    while True:
        print("\n --- PetShop dos Deuses --- \n")
        servicos = ['1) - Consulta', '2) - Tosa', '2) - Banho', '3) - Acessórios', '4) - Meus pedidos', '5) - Voltar']
        print('°--------------°')
        for item in servicos:
            print("|",  item)
        print('°--------------°\n')

        op = int(input("Selecione uma opção: "))

        if op == 1:
            print('\n',servicos[0],'\n')
            ss.consulta() 
        elif op == 2:
            ss.tosa()

