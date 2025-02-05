class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Marcos", "985720251")
conta = Conta(c1.get_nome(), 1222)

conta.depositar(100)
conta.saque(50)
conta.extrato()