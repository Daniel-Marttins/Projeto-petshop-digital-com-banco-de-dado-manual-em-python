import bancoDados as bd
def menu_inicial():
    while True:
        print("\n--- Alusian PetShop ---\n")
        print('1) - Login')
        print('2) - Cadastro')
        print('3) - Sair')

        op = int(input("Selecione uma opção >>> "))

        if op == 1:
            bd.login()
            print('\n>>> Login <<<\n')

        elif op == 2:
            bd.cadastro()
            print('\n>>> Cadastrar <<<\n')

        elif op == 3:
            print("Obrigado(a) por nos visitar, volte sempre!")

        else:
            print("Opção invalida, tente novamente...")