from Cliente.cliente import Cliente
from Tarjeta.debito import Debito
from Tarjeta.credito import Credito
from Cuenta.cajaAhorroPesos import CajaAhorroPesos
from Cuenta.cajaAhorroDolares import CajaAhorroDolares
from Cuenta.cuentaCorrientePesos import CuentaCorrientePesos
from Cuenta.cuentaCorrienteDolares import CuentaCorrienteDolares
from Cuenta.CuentaInversiones import CuentaInversiones

class Gold(Cliente):

      def __init__(self,nombre,apellido,dni,nro_cliente):
            super().__init__(nombre,apellido,dni,nro_cliente)
            self.tipo_cliente = "Gold"

      def getInfo(self):
            print("Nombre: "+self.nombre+" "+self.apellido+"\n"
                  "DNI: "+str(self.dni)+"\n"
                  "Tipo de cliente: "+self.tipo_cliente)
            
      def altaCajaAhorroPesos(self):
           self.cajaAhorroPesos = CajaAhorroPesos("caja de ahorro",0,"pesos")

      def getSaldoCajaAhorroPesos(self):
            return self.cajaAhorroPesos
      
      def getSaldoCajaAhorroDolares(self):
            return self.cajaAhorroDolares
      
      def altaCajaAhorroDolares(self):
           self.cajaAhorroDolares = CajaAhorroDolares("caja de ahorro",0,"dolares")
            
      def altaTarjetaDebito(self,marcaTarjeta):
            if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard"):
                  self.tarjetaDebito = Debito(marcaTarjeta)
            else:
                  print("El cliente solo tiene acceso a tarjetas Mastercard o Visa") 

      def getTarjetaDebito(self):
            return self.tarjetaDebito
      
      def altaTarjetaCredito(self,marcaTarjeta):
            if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard"):
                  self.tarjetaCredito = Credito(marcaTarjeta,100000,150000)
            else:
                  print("El cliente solo tiene acceso a tarjetas Mastercard o Visa") 

      def getTarjetaCredito(self):
            return self.tarjetaCredito
"""
RESTRICCIONES

- Una tarjeta de débito.
- Hasta 2 cajas de ahorro y una cuenta corriente sin cargos adicionales.
Se aplica un cargo mensual extra por cajas de ahorro en dólares 
adicionales.
- Tarjetas VISA y/o Mastercard con hasta 5 extensiones cada una, con 
límites de $100,000 en un pago y $150,000 en cuotas.
- Máximo de $20,000 en retiros diarios sin comisiones. Retiros 
ilimitados sin costo mensual.
- Acceso a cuentas de inversión.
- Posibilidad de tener una chequera.
- Comisión del 0.5% por transferencias salientes y 0.1% por 
transferencias entrantes.

getOpciones dentro de cada cliente: classic, gold, black

"""