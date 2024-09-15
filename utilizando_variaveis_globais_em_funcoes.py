salario = 2000


def salario_bonus(bonus):
    #salario += bonus #(não funciona sem declarar variavel global)
    global salario
    salario += bonus
    return salario


print("O salário com bonus é:", salario_bonus(500)) #2500
