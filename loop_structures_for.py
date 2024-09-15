frase = str(input("Inserir uma frase: "))
VOGAIS = "AEIOU"
quantidade_vogais = 0
for letra in frase:

    if letra.upper() in VOGAIS:
        print(letra.upper(), end=" ")
        quantidade_vogais += 1
print(f"Essa frase tem {quantidade_vogais} vogais")
