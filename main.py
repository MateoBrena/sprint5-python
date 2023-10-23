from Cliente.classic import Classic
from Cliente.gold import Gold
from Cliente.black import Black

cliente1 = Classic("Cliente","Classic",12345678,1)
cliente2 = Gold("Cliente2","Gold",12345679,2)
cliente3 = Black("Cliente3","Black",12345670,3)

cliente1.getInfo()
print()
cliente2.getInfo()
print()
cliente3.getInfo()

cliente1.altaCajaAhorroPesos()
print()
print(cliente1.getSaldoPesos())
print()
cliente1.altaCajaAhorroDolares()
print()
print(cliente1.getSaldoDolares())
print()
cliente1.altaTarjetaDebito("Visa")
cliente1.altaTarjetaCredito()
print()
print(cliente1.getTarjetaDebito())
print()
cliente2.altaTarjetaCredito("Visa")
print()
print(cliente2.getTarjetaCredito())
cliente3.altaTarjetaCredito("Amex")
print()
print(cliente3.getTarjetaCredito())
print()
