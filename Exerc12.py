# Solicita ao usuário que insira uma letra
letra = input("Digite uma letra: ").lower()

# Verifica se a letra é uma vogal ou consoante
if letra.isalpha() and len(letra) == 1:  # Verifica se é uma letra e tem comprimento 1
    if letra in 'aeiou':
        print("A letra é uma vogal.")
    else:
        print("A letra é uma consoante.")
else:
    print("Entrada inválida. Por favor, digite apenas uma letra.")