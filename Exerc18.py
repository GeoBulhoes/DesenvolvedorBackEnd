# Solicita ao usuário que insira os dois números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Verifica qual número é o menor e qual é o maior
if numero1 < numero2:
    menor = numero1
    maior = numero2
else:
    menor = numero2
    maior = numero1

# Gera e imprime os números inteiros que estão no intervalo
print(f"Os números inteiros entre {menor} e {maior} são:")
for numero in range(menor + 1, maior):
    print(numero)