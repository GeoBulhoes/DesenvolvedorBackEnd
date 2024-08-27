nome = 0
senha = 0
while nome == senha:
    nome = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
    if nome == senha:
        print("Nome e senha devem ser diferentes!")