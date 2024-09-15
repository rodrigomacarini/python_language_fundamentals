nome = "Rodrigo"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.486

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}" .format(nome, idade))
print(f"Nome: {nome} Idade: {idade}")

print("Idade: {1} profissão: {2} Nome: {0}" .format(nome, idade, profissao))
print(f"Saldo: {saldo}")
print(f"Saldo: {saldo:.2f}")
print(f"Saldo: {saldo:10.2f}")
