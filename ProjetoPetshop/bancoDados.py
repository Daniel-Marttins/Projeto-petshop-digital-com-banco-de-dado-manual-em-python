import os.path
import servicos as s

nomeArquivo = input("Nome >>> ")
juntar = nomeArquivo+".txt"
diretorio = "C:\\Users\\Usuario\\Documents\\Vscode\\"+juntar

if (os.path.exists(diretorio)):
    print("\nSeja bem vindo de volta,", nomeArquivo,", vamos realizar o login!")

else:
    criar_arquivo = open(diretorio, 'w')
    print("\nVocê ainda não possui cadastro, vamos realiza-lo...\n")

def cadastro():
    nome = input("Nome Completo >>> ")
    email = input("Escolha seu melhor email >>> ")
    senha = input("Defina uma senha >>> ")
    salvar = open(diretorio, 'a')
    salvar.writelines(nome+'\n')
    salvar.writelines(email+'\n')
    salvar.writelines(senha+'\n')

def login():
    nome = input("Nome >>> ")
    senha = input("Senha >>> ")
    login = open(diretorio, 'r')
    ler = login.read()
    verificar = ler.split('\n')

    verificar_nome = verificar[0]
    verificar_senha = verificar[2]

    if nome == verificar_nome and senha == verificar_senha:
        s.menu_servicos()

