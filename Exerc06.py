# Solicita ao usuário o valor ganho por hora
valor_por_hora = float(input("Digite quanto você ganha por hora: "))

# Solicita ao usuário o número de horas trabalhadas no mês
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário total no mês
salario_mensal = valor_por_hora * horas_trabalhadas

# Imprime o resultado
print("O seu salário total no mês é: R$", salario_mensal)