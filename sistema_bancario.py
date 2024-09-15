from datetime import datetime
#Variáveis do sistema:
LIMITE_DE_SAQUE = 3
numero_saques = 0
valor_limite = 500.00
saldo = 0
extrato = [f"Saldo inicial: {saldo}"]
menu = """
============BANCO============
EsCOLHA UMA OPERAÇÃO:
[a] DEPÓSITO
[b] SAQUE
[c] EXTRATO
[d] SAIR
=============================
"""
#Funções:
def deposito(valor):
    global saldo
    saldo += valor
    print(f"O valor de R${valor:.2f} foi depositado com sucesso.")
    extrato.append(f"R$ {valor:.2f} foram depositados")
    return saldo, extrato

def saque(valor):
    global saldo, numero_saques, valor_limite
    if numero_saques >= LIMITE_DE_SAQUE:
        print("Você atingiu o limite de saques diários.")
    elif valor > saldo:
        print("Saldo insuficiente para o saque.")
    elif valor > valor_limite:
        print("Valor informado é maior que o valor limite para saques.")
    else:
        saldo -= valor
        numero_saques += 1
        print(f"Retire o valor de R${valor:.2f} da máquina.")
        extrato.append(f"-R$ {valor:.2f} foram sacados")
    return saldo, extrato

def imprimir_extrato():
    global extrato
    print("\n===== EXTRATO =====")
    print(datetime.today().strftime("%d/%m/%Y"))
    for item in extrato:
        print(item)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("====================\n")

#Sistema:
while True:
    opcao = input(menu)
    if opcao == "d":
        print("Obrigado por utilizar nossos serviços.")
        break
    elif opcao == "a":
        valor_deposito = float(input("Valor a ser depositado: R$"))
        if valor_deposito > 0.0:
            saldo, extrato = deposito(valor_deposito)
        else:
            print("Apresente um valor válido.")
    elif opcao == "b":
        valor_saque = float(input("Valor a ser sacado: R$"))
        if valor_saque > 0.0:
            saldo, extrato = saque(valor_saque)
        else:
            print("Apresente um valor válido.")
    elif opcao == "c":
        if len(extrato) <= 1:
            print("Não há movimentações para exibir")
        else:
            imprimir_extrato()
    else:
        print("Opção inválida, tente novamente.")
