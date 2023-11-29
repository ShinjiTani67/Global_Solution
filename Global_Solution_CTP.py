def menu():
    print("opção de dicas de saúde (1)")
    print("opção de calendario de vacinas(2)")
    print("opção de nutrição(3)")
    print("opção de calculo de IMC(4)")

def login():
    nome_usuario = "nando"
    senha = 123
    nome_login = input("digite o seu nome de usuario: ")
    senha_login = input("digite a senha do login: ")
    if nome_login == nome_usuario and senha_login == senha:
        print("Bem Vindo")
    else:
        print("senha ou nome de usuario invalidados")
        print("caso não possua um login, ir para a página de cadastro")

def calculoIMC():
    peso = float(input("Por favor digite o seu peso: "))
    altura = float(input("Por favor digite a sua altura: "))
    IMC = peso / (altura ** 2)
    if IMC <= 18.5:
        print("abaixo do peso ideal")
    elif IMC >= 18.6 or IMC <= 24.9:
        print("peso ideal")
    elif IMC >= 25 or IMC <= 29.9:
        print("Sobre peso")
    elif IMC >= 30 or IMC <= 34.9:
        print("Obesidade nivel 1")
    elif IMC >= 35 or IMC <= 39.9:
        print("Obesidade nivel 2")
    else:
        print("Obesidade nivel 3")

#===============================================================================================================

login()
menu()
opcao = int(input("Por favor digite a sua opção desejada: "))
while opcao != 0:
    if opcao == 1:
        print("O menu de dicas abre opções de dicas sobre oque fazer em diversas situações como uma dor de cabeça por exemplo")
        pass
    elif opcao == 2:
        print("O menu de caledário de vacinas deve dar a opção do usuário ver as vacinas que ele ja tomou")
        pass
    elif opcao == 3:
        print("O menu de nutrição abre diverdsas dicas de como suplementar ")
        pass
    elif opcao == 4:
        calculoIMC()
        pass
    else:
        print("opcao não é valida")
        pass
    opcao = int(input("Por favor digite a sua opção desejada: "))
