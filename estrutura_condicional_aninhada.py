conta_normal = True
conta_universitaria = False
saldo = 2000.0
saque = 2300.0
cheque_especial = 450.0

if conta_normal:

    if saldo >= saque:
        print("Realizando saque!")
    elif saque <= (saldo + cheque_especial):
        print("Realizando saque com cheque especial")
    else:
        print("Saldo insuficiente :C")
        
elif conta_universitaria:

    if saldo >= saque:
        print("Realizando Saque!")
    else:
        print("Saldo insuficiente :C")

else:
    print("O sistema não reconheceu seu tipo de conta, entre em contato com seu gerente.")