# Define a função que recebe três argumentos e retorna a soma
def soma_tres_numeros(a, b, c):
    return a + b + c

# Solicita ao usuário que insira três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Chama a função e armazena o resultado
resultado = soma_tres_numeros(numero1, numero2, numero3)

# Imprime o resultado
print("A soma dos três números é:", resultado)