from Cuenta.cuenta import Cuenta
from Cliente.cliente import Cliente
from Tarjeta.debito import Debito

class Classic(Cliente):
      def __init__(self,nombre,apellido,dni,nro_cliente):
            super().__init__(nombre,apellido,dni,nro_cliente)
            self.tipo_cliente = "Classic"

      def getInfo(self):
            print("Nombre: "+self.nombre+" "+self.apellido+"\n"
                  "DNI: "+str(self.dni)+"\n"
                  "Tipo de cliente: "+self.tipo_cliente)
            
      def crearCajaAhorro(self,cajaAhorro):
           self.cuenta = Cuenta(cajaAhorro,0)

      def getCuenta(self):
            return self.cuenta
      
      def crearTarjeta(self,marcaTarjeta):
            if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard"):
                  self.tarjetaDebito = Debito(marcaTarjeta)
            else:
                  print("El cliente solo tiene acceso a tarjetas Mastercard o Visa") 

      def getTarjetaDebito(self):
            return self.tarjetaDebito
            
"""
RESTRICCIONES

- Una tarjeta de débito.
- Caja de ahorro en pesos.
- Opcionalmente, caja de ahorro en dólares con cargo mensual.
- Hasta 5 retiros de dinero en efectivo sin comisiones, luego se aplica 
una tarifa. El límite diario de retiro es de $10,000 por cajero.
- No tienen acceso a tarjetas de crédito.
- Comisión del 1% por transferencias salientes y 0.5% por 
transferencias entrantes.

"""
