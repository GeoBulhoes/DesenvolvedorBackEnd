# Validação do Nome
nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("Erro: O nome deve ter mais de 3 caracteres.")
    nome = input("Digite seu nome: ")

# Validação da Idade
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Erro: A idade deve estar entre 0 e 150.")
    idade = int(input("Digite sua idade: "))

# Validação do Salário
salario = float(input("Digite seu salário: "))
while salario <= 0:
    print("Erro: O salário deve ser maior que zero.")
    salario = float(input("Digite seu salário: "))

# Validação do Sexo
sexo = input("Digite seu sexo (f para feminino ou m para masculino): ").lower()
while sexo not in ['f', 'm']:
    print("Erro: O sexo deve ser 'f' para feminino ou 'm' para masculino.")
    sexo = input("Digite seu sexo (f para feminino ou m para masculino): ").lower()

# Validação do Estado Civil
estado_civil = input("Digite seu estado civil (s, c, v, d): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']:
    print("Erro: O estado civil deve ser 's' (solteiro), 'c' (casado), 'v' (viúvo) ou 'd' (divorciado).")
    estado_civil = input("Digite seu estado civil (s, c, v, d): ").lower()

# Exibe as informações validadas
print("\nInformações validadas com sucesso:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
print(f"Estado Civil: {'Solteiro' if estado_civil == 's' else 'Casado' if estado_civil == 'c' else 'Viúvo' if estado_civil == 'v' else 'Divorciado'}")