#sao operadores que em conjunto com os operadores de comparação
#retornan um valor booleano
# op_comparação + op_logico + op_comparação... N...
saldo = 1000
saque = 200
limite = 100
print(saldo >= saque and saque <= limite)
print(saldo >= saque or saque <= limite)


print((saldo >= saque and saque <= limite) and (saldo >= saque or saque <= limite))
print((saldo >= saque and saque <= limite) or (saldo >= saque or saque <= limite))

#operador de negação not

print(not 1000 > 1500)
#isso dá True

contatos_emergencia = []
print(not contatos_emergencia)
#isso dá True

print(not "")
#isso dá True

print(not"algo escrito na string")
#isso da False

#logica: na condição and para ser True, tudo tem que ser True
#na condição or para ser True, um dos dois tem que ser True
print("\n")
print(True and True)
print(False and False)
print(True and False)
print(True or False)
print(False or False)
print(True or True)

