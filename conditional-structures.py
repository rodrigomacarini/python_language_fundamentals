#permitem o desvio de fluxo de controle, 
#quando determinadas expressões lógicas são atendidas

#saldo = 2000.0
#saque = float(input("informe o valor do saque: "))
#if saldo >= saque:
#    print("Realizando saque!")
#else:
#    print("Saldo insuficiente!")

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("Informe a sua idade: "))
if (idade >= MAIOR_IDADE):
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas mas não práticas.")
else:
    print("Não está apta para participar ser uma pena")
