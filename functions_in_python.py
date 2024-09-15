def printa_nome_1():
    #função printando nome
    print("Olá, Rodrigo.")
    return None
    #Desnecessário pois sem colocar return
    #no final o Python ja retorna None

def printa_nome_2(nome):
    #função printando nome
    #se a função for chamada sem dar valor ao parâmetro
    #ocorrerá um erro.
    print(f"Olá, {nome}.")

def printa_nome_3(nome="Sabrina"):
    #função printando nome
    #se a função for chamada sem dar valor ao parâmetro
    #a variável do parâmetro reberá o valor definido aqui
    print(f"Olá, {nome}.")


printa_nome_1()
printa_nome_2("rodrigo")
printa_nome_3()
printa_nome_3("Rodrigo")
