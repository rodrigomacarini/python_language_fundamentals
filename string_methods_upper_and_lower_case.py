CURSO = "         pYtHon    "

print(CURSO.upper())

print(CURSO.lower())

print(CURSO.rstrip())

print(CURSO.lstrip(),"\n")

#junções e centralização

nome = "guiLherMe"

print(nome.title(),"\n")

texto = "        Olá mundo!      "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

curso = "Python"

print(curso.center(10, "#"))
print(".".join(curso))
print(curso.center(14))
print(curso.center(14,"#"))

PI = 3.14159

print(f"valor de pi: {PI:.2f}")
print(f"valor de pi: {PI:10.2f}")
