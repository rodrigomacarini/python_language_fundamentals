def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("valor sacado: ", valor)
        saldo -= valor
        print("Saldo atual: ", saldo)
    else:
        print("saldo insuficiente")
    print("Obrigado por utilizar nossos serviços.")
sacar(600)
sacar(450)

def depositar(valor):
    saldo = 500
    saldo += valor
    print("Valor depositado.\nSaldo: ", saldo)
depositar(800)
