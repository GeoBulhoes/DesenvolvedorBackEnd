# Solicita ao usuário que insira as duas notas parciais
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Verifica a média e exibe a mensagem correspondente
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")