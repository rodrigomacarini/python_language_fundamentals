frase = str(input("Inserir uma frase: "))
VOGAIS = "AEIOU"
quantidade_vogais = 0
for letra in frase:

    if letra.upper() in VOGAIS:
        if letra.upper() == "I":
            break
        print(letra.upper(), end=" ")
        quantidade_vogais += 1
print(f"\nEssa frase tem {quantidade_vogais} vogais")
