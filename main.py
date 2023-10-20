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

cliente1.crearCajaAhorro("Caja de ahorro")
print()
print(cliente1.getCuenta())
print()
cliente1.crearTarjeta("Visa")
print()
print(cliente1.getTarjetaDebito())
print()
cliente2.crearTarjetaCredito("Visa")
print()
print(cliente2.getTarjetaCredito())
cliente3.crearTarjetaCredito("Amex")
print()
print(cliente3.getTarjetaCredito())
