from datetime import datetime  # Importa a biblioteca datetime para manipulação de datas e horas.

# Constantes do sistema (valores que não mudam durante a execução):
LIMITE_DE_SAQUE = 3  # Limite máximo de saques por dia.
VALOR_LIMITE = 500.00  # Valor máximo permitido por saque.
LIMITE_DE_TRANSACOES = 10  # Limite máximo de transações diárias (depósitos + saques).

# Menu de opções apresentado ao usuário:
MENU = """
============BANCO============
ESCOLHA UMA OPERAÇÃO:
[a] DEPÓSITO
[b] SAQUE
[c] EXTRATO
[d] SAIR
=============================
"""

# Variáveis do sistema (valores que podem mudar durante a execução):
mascara_ptr = "%d/%m/%Y %H:%M"  # Formato de data/hora para exibição.
saldo = 0  # Saldo inicial da conta.
extrato = [f"Saldo inicial: R$ {saldo:.2f}"]  # Lista que armazena o histórico de transações.
numero_saques = 0  # Contador de saques diários.
transacoes_diarias = 0  # Contador de transações diárias (depósitos e saques).
dia = datetime.today().strftime("%d/%m/%Y")  # Data atual no formato dia/mês/ano.

# Função para realizar depósitos:
def deposito(valor, saldo, extrato, transacoes_diarias):
    saldo += valor  # Adiciona o valor ao saldo atual.
    print(f"O valor de R${valor:.2f} foi depositado com sucesso.")
    horario = datetime.now()  # Obtém a data e hora atuais.
    # Adiciona uma entrada ao extrato com o valor depositado e a data/hora da transação:
    extrato.append(f"R$ {valor:.2f} depositados - {horario.strftime(mascara_ptr)}")
    transacoes_diarias += 1  # Incrementa o contador de transações.
    return saldo, extrato, transacoes_diarias  # Retorna os novos valores de saldo, extrato e transações.

# Função para realizar saques:
def saque(valor, saldo, numero_saques, extrato, transacoes_diarias):

    if valor > saldo:
        print("Saldo insuficiente para o saque.")  # Verifica se o saldo é suficiente.
    elif valor > VALOR_LIMITE:
        print(f"Valor informado é maior que o limite de R${VALOR_LIMITE:.2f} para saques.")  # Verifica se o valor está acima do permitido.
    else:
        saldo -= valor  # Subtrai o valor do saldo.
        numero_saques += 1  # Incrementa o contador de saques.
        print(f"Retire o valor de R${valor:.2f} da máquina.")
        horario = datetime.now()  # Obtém a data e hora atuais.
        # Adiciona uma entrada ao extrato com o valor sacado e a data/hora da transação:
        extrato.append(f"-R$ {valor:.2f} sacados - {horario.strftime(mascara_ptr)}")
        transacoes_diarias += 1  # Incrementa o contador de transações.
    return saldo, extrato, numero_saques, transacoes_diarias  # Retorna os novos valores.

# Função para imprimir o extrato:
def imprimir_extrato(extrato, saldo):
    print("\n===== EXTRATO =====")
    for item in extrato:  # Percorre a lista de transações e imprime cada item.
        print(item)
    print(f"Saldo atual: R$ {saldo:.2f}")  # Imprime o saldo atual da conta.
    print("====================\n")


# Loop principal do programa (exibe o menu e processa as opções do usuário):
while True:
    # Verifica se o dia mudou (para resetar os contadores diários):
    if dia != datetime.today().strftime("%d/%m/%Y"):
        transacoes_diarias = 0  # Reseta o número de transações diárias.
        numero_saques = 0  # Reseta o número de saques diários.
        dia = datetime.today().strftime("%d/%m/%Y")  # Atualiza a data.

    # Verifica se o limite de transações diárias foi alcançado:
    if transacoes_diarias >= LIMITE_DE_TRANSACOES:
        print("Limite de transações diárias alcançado!")
        imprimir_extrato(extrato, saldo)  # Imprime o extrato e finaliza o programa.
        break

    opcao = input(MENU).lower()  # Exibe o menu e recebe a opção do usuário.

    if opcao == "d":
        print("Obrigado por utilizar nossos serviços.")
        break  # Encerra o programa.

    elif opcao == "a":  # Depósito:
        valor_deposito = float(input("Valor a ser depositado: R$"))
        if valor_deposito > 0:
            # Chama a função de depósito e atualiza as variáveis:
            saldo, extrato, transacoes_diarias = deposito(valor_deposito, saldo, extrato, transacoes_diarias)
        else:
            print("Apresente um valor válido.")  # Valida se o valor informado é positivo.

    elif opcao == "b":  # Saque:

        if numero_saques >= LIMITE_DE_SAQUE:
            print("Você atingiu o limite de saques diários.")  # Verifica se o limite de saques foi atingido.
        else:

            valor_saque = float(input("Valor a ser sacado: R$"))
            if valor_saque > 0:
                # Chama a função de saque e atualiza as variáveis:
                saldo, extrato, numero_saques, transacoes_diarias = saque(valor_saque, saldo, numero_saques, extrato, transacoes_diarias)
            else:
                print("Apresente um valor válido.")  # Valida se o valor informado é positivo.

    elif opcao == "c":  # Imprimir extrato:
        imprimir_extrato(extrato, saldo)

    else:
        print("Opção inválida, tente novamente.")  # Mensagem de erro para opções inválidas.
        
