entrada_do_cliente = int(input("Escolha uma opção (1,2 ou 3): "))

while entrada_do_cliente != 3:

    if entrada_do_cliente == 1:
        print("sacando seu dinheiro!")
        break
    elif entrada_do_cliente == 2:
        print("Imprimindo extrato bancário:")
        break
    else:
        print("Escolha uma opção válida.")
        break

else:
    print("Obrigado por utilizar nossos sistemas!")
