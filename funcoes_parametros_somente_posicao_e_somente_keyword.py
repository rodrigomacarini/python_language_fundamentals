#TODOS PARÂMENTRO QUE VEM ANTES DA BARRA É SOMENTE POR POSIÇÃO, E TODOS OS PARÂMETROS DEPOIS DO * SÃO SOMENTE POR KEYWORD.
#TODOS OS PARÂMETROS NO MEIO DELES SÃO HÍBRIDOS, COMO SE NÃO TIVESSE MARCADO NADA.

#SOMENTE POR POSIÇÃO:
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#--------------------------------------------------------------------------------------------------------------------------

criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", combustivel = "Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

#SOMENTE POR NOME:
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

#--------------------------------------------------------------------------------------------------------------------------

def criar_carro(modelo, ano, placa, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#--------------------------------------------------------------------------------------------------------------------------
