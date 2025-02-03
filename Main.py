class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Marcos", "985720251")
conta = Conta(c1.nome, 6565, 0)

print(conta.titular, " Numero: ", conta.numero, "Seu Saldo:", conta.saldo)