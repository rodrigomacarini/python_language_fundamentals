from datetime import datetime

# Constantes do sistema:
LIMITE_DE_SAQUE = 3  # Limite máximo de saques por dia.
LIMITE_DE_TRANSACOES = 10  # Limite máximo de transações diárias (depósitos + saques).
VALOR_LIMITE = 500
# Menu de opções apresentado ao usuário:
MENU_CONTA = """
============BANCO============
Horario de funcionamento das 07:00 as 17:00 horas
ESCOLHA UMA OPERAÇÃO:
[a] DEPÓSITO
[b] SAQUE
[c] EXTRATO
[d] SAIR
=============================
"""
#Menu de opções para operações gerenciais
MENU_CADASTROS = """
============BANCO============
Horario de funcionamento das 07:00 as 17:00 horas
ESCOLHA UMA OPÇÃO:
[e] CADASTRO DE USUÁRIO
[f] CRIAÇÃO DE CONTA
[g] LISTAR CONTAS
[h] LISTAR USUÁRIOS
[i] LOGIN NA CONTA
[d] SAIR
=============================
"""

# Variáveis do sistema:
mascara_ptr = "%d/%m/%Y %H:%M"  # Formato de data/hora para exibição.
saldo = 0
extrato = [f"Saldo inicial: R$ {saldo:.2f}"]  # Lista que armazena o histórico de transações.
numero_saques = 0  # Contador de saques diários.
transacoes_diarias = 0  # Contador de transações diárias (depósitos e saques).
dia = datetime.today().strftime("%d/%m/%Y")  # Data atual no formato dia/mês/ano.

# Função para realizar depósitos:
def deposito(valor, saldo, extrato, transacoes_diarias, /):
    saldo += valor  # Adiciona o valor ao saldo atual.
    print(f"O valor de R${valor:.2f} foi depositado com sucesso.")
    horario = datetime.now()  # Obtém a data e hora atuais.
    # Adiciona uma entrada ao extrato com o valor depositado e a data/hora da transação:
    extrato.append(f"R$ {valor:.2f} depositados - {horario.strftime(mascara_ptr)}")
    transacoes_diarias += 1  # Incrementa o contador de transações.
    return saldo, extrato, transacoes_diarias  # Retorna os novos valores de saldo, extrato e transações.

# Função para realizar saques:
def saque(*, valor, saldo, numero_saques, extrato, transacoes_diarias):

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
def imprimir_extrato(saldo, /, *, extrato):
    print("\n===== EXTRATO =====")
    for item in extrato:  # Verifica a lista de transações e imprime cada item.
        print(item)
    print(f"Saldo atual: R$ {saldo:.2f}")  # Imprime o saldo atual da conta.
    print("====================\n")

#Função para cadastrar usuário
def cadastro_usuario(cpf):
    usuario = {"cpf": cpf}
    usuario["name"] = str(input("Insira o nome do usuário: "))
    usuario["nascimento"] = datetime.strptime(input("Data de nascimento no formato dd/mm/yyyy: "), "%d/%m/%Y")
    usuario["endereco"] = str(input("Endereço (Logradouro, número - bairro - cidade/SIGLA ESTADO): "))
    lista_usuarios.append(usuario)
    print(f"""
Usuário cadastrado com sucesso.
Nome: {usuario["name"]}
CPF: {usuario["cpf"]}
Data de nascimento: {usuario["nascimento"].strftime("%d/%m/%Y")}
Endereço: {usuario["endereco"]}      
""")

#TODO Função para criar conta (lista)
def cadastro_conta(usuario):
    conta = [usuario]
    numero_conta = len(lista_contas) + 1
    conta.append("0001")
    conta.append(numero_conta)
    conta.append(0)
    conta.append([])  # Extrato (inicializado como lista vazia) extrato = conta[4]
    conta.append(0)  #Inicia a conta com número de saques do dia sendo 0.
    conta.append(0)  #Inicia o contador de transações diárias, começando em 0.
    conta.append(datetime.today().strftime("%d/%m/%Y"))  # Data da última transação
    lista_contas.append(conta)
    print(f"""
Conta criada com sucesso.
Usuário: {conta[0]["name"]}
Agência: {conta[1]}
Número da conta: {conta[2]}
Saldo da conta: R${conta[3]:.2f}
""")

#TODO Função para listar contas
def listar_contas(lista_contas):
    if not lista_contas:
        print("Não há contas cadastradas para mostrar.")
    else:
        print("Lista de contas:")
        for conta in lista_contas:
            print(f"""  
Número da conta: {conta[2]}
Agência: {conta[1]}
Usuário: {conta[0]["name"]}
Saldo da conta: R${conta[3]:.2f}
""")

# Função para apresentar uma lista com todos os usuários do banco. 
def listar_usuarios(lista_usuarios):
    if not lista_usuarios:
        print("Não há usuários cadastrados para mostrar.")
    else:
        print("Lista de usuários:")
        for usuario in lista_usuarios:
            print(f"""  
Nome: {usuario["name"]}
CPF: {usuario["cpf"]}
Data de nascimento: {usuario["nascimento"].strftime("%d/%m/%Y")}
Endereço: {usuario["endereco"]}
""")

#Verifica se o dia da ultima transação foi o dia atual
def ultima_transacao(data_ultima_transacao, transacoes_diarias, numero_saques, conta):
    dia_atual = datetime.today().strftime("%d/%m/%Y")
    if data_ultima_transacao != dia_atual:
        transacoes_diarias = 0  # reseta o número de transações diárias.
        numero_saques = 0  # reseta o número de saques diários.
        conta[6] = transacoes_diarias  # Atualiza a conta com o novo valor de transações diárias.
        conta[5] = numero_saques  # Atualiza a conta com o novo valor de número de saques.
        conta[7] = dia_atual  # Atualiza a data da última transação.
    else:
        None
    return transacoes_diarias, numero_saques, conta

#Função para fazer operações dentro de uma conta específica.
def login_conta(conta, extrato, numero_saques, transacoes_diarias, dia, LIMITE_DE_SAQUE, LIMITE_DE_TRANSACOES, MENU_CONTA):
    
    VALOR_LIMITE = 500.00  # Valor máximo permitido por saque.
    saldo = conta[3]
    numero_saques = conta[5]
    transacoes_diarias = conta[6]
    data_ultima_transacao = conta[7]
    dia_atual = datetime.today().strftime("%d/%m/%Y")

    #Verifica se a fata da última transação foi no dia atual:
    transacoes_diarias, numero_saques, conta = ultima_transacao(data_ultima_transacao, transacoes_diarias, numero_saques, conta)

    #Loop de operações do usuário:
    while True:
        #Verifica se o dia mudou (para resetar os contadores diários):
        opcao = input(MENU_CONTA).lower()  # exibe o menu e recebe a opção do usuário.

        if opcao == "d":
            conta[3] = saldo
            conta[5] = numero_saques
            conta[6] = transacoes_diarias
            print("obrigado por utilizar nossos serviços.")
            return conta
            break  # encerra o processo de LogIn

        elif opcao == "a":  # depósito:
            if transacoes_diarias >= LIMITE_DE_TRANSACOES: # verifica se o limite de transações diárias foi alcançado:
                print("limite de transações diárias alcançado!")
            else:
                valor_deposito = float(input("valor a ser depositado: R$"))
                if valor_deposito > 0:
                    # chama a função de depósito e atualiza as variáveis:
                    saldo, extrato, transacoes_diarias = deposito(valor_deposito, saldo, extrato, transacoes_diarias)
                    conta[7] = dia_atual  # Atualiza a data da última transação
                else:
                    print("Apresente um valor válido.")  # Valida se o valor informado é positivo.

        elif opcao == "b":  # Saque:
            if transacoes_diarias >= LIMITE_DE_TRANSACOES: # verifica se o limite de transações diárias foi alcançado:
                print("limite de transações diárias alcançado!")
            else:
                if numero_saques >= LIMITE_DE_SAQUE:
                    print("Você atingiu o limite de saques diários.")  # Verifica se o limite de saques foi atingido.
                else:

                    valor_saque = float(input("Valor a ser sacado: R$"))
                    if valor_saque > 0:
                        # Chama a função de saque e atualiza as variáveis:
                        saldo, extrato, numero_saques, transacoes_diarias = saque(valor = valor_saque, saldo = saldo, numero_saques = numero_saques, extrato = extrato, transacoes_diarias = transacoes_diarias)
                        conta[7] = dia_atual  # Atualiza a data da última transação                    
                    else:
                        print("Apresente um valor válido.")  # Valida se o valor informado é positivo.

        elif opcao == "c":  # Imprimir extrato:
            # A função extrato deve receber os argumentos por posição e nome (positional only e keyword only)
            # Argumentos posicionais: saldo
            # argumentos nomeados: extrato
            imprimir_extrato(saldo, extrato = conta[4])

        else:
            print("Opção inválida, tente novamente.")  # Mensagem de erro para opções inválidas.

# Variáveis Cadastro e Login:
lista_usuarios = []
lista_contas = []
# Loop de cadastros e Login
while True:
    operacao = input(MENU_CADASTROS).lower()  # Exibe o menu e recebe a operação selecionado.

    #Verifica se o dia mudou (para resetar os contadores diários):
    if dia != datetime.today().strftime("%d/%m/%Y"):
        transacoes_diarias = 0  # reseta o número de transações diárias.
        numero_saques = 0  # reseta o número de saques diários.
        dia = datetime.today().strftime("%d/%m/%Y")  # atualiza a data.

    if operacao == "e": # Cadastro de usuário.
        print("Cadastro de usuário.\n")
        cpf = str(input("Informe o CPF do usuário: "))

        # Verifica se a lista de usuários está vazia e chama o cadastro se estiver:
        if bool(lista_usuarios) == False:
            cadastro_usuario(cpf)

        else:
            # Verifica se o CPF já está cadastrado:
            cpf_ja_cadastrado = False                
            for usuario in lista_usuarios:
                if usuario["cpf"] == cpf:
                    print("CPF já cadastrado em um usuário.")
                    cpf_ja_cadastrado = True
                    break # Se o CPF já está cadastrado em um usuário interrompe o loop.
            # Se o CPF não foi encontrado, faz o cadastro:    
            if cpf_ja_cadastrado == False:
                    cadastro_usuario(cpf)

    elif operacao == "f": # Cadastro de conta.
        print("Cadastro de conta.\n")
        cpf = input("Informe o CPF do usuário: ")
        # As linhas a seguir verificam se o CPF informado pertence a um usuário do banco:
        cpf_ja_cadastrado = False
        for usuario in lista_usuarios:
            if usuario["cpf"] == cpf:
                cpf_ja_cadastrado = True
                cadastro_conta(usuario)
        if not cpf_ja_cadastrado:
            print("Este CPF não possui cadastro de usuário, favor cadastrar.")
    
    elif operacao == "d": # Saida do sistema.
        print("Obrigado por utilizar nossos serviços.")
        break

    elif operacao == "g": # Gera uma lista das contas do banco e seus dados.
        listar_contas(lista_contas)

    elif operacao == "h": # Gera uma lista dos usuários do banco e seus dados.
        listar_usuarios(lista_usuarios)

    elif operacao == "i": #Vai para uma tela de operações na conta especificada.
        numero_conta = int(input("""
LOGIN NA CONTA
Informe o número da conta: 
"""))
        # As linhas a seguir verificam se o número da conta fornecido pertence a uma conta cadastrada no banco.
        conta_cadastrada = False

        for conta in lista_contas:
            if conta[2] == numero_conta:
                conta_cadastrada = True
                conta = login_conta(conta, conta[4], conta[5], conta[6], dia, LIMITE_DE_SAQUE, LIMITE_DE_TRANSACOES, MENU_CONTA)

        if not conta_cadastrada:
            print("Esta conta não existe, favor cadastrar ou entrar com uma existente.")

    else:
        print("Insira um comando válido.") # Caso o usuário entre com um comando não especificado no menu.
