# Solicita ao usuário que insira uma letra para o sexo
sexo = input("Digite F para Feminino ou M para Masculino: ").upper()

# Verifica a letra digitada e exibe a mensagem correspondente
if sexo == "F":
    print("Feminino")
elif sexo == "M":
    print("Masculino")
else:
    print("Sexo Inválido")