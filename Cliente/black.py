from Cliente.cliente import Cliente
from Tarjeta.debito import Debito
from Tarjeta.credito import Credito
from Cuenta.cajaAhorroPesos import CajaAhorroPesos
from Cuenta.cajaAhorroDolares import CajaAhorroDolares
from Cuenta.cuentaCorrientePesos import CuentaCorrientePesos
from Cuenta.cuentaCorrienteDolares import CuentaCorrienteDolares
from Cuenta.CuentaInversiones import CuentaInversiones

class Black(Cliente):
      
      def __init__(self,nombre,apellido,dni,nro_cliente):
            super().__init__(nombre,apellido,dni,nro_cliente)
            self.tipo_cliente = "Black"

      def getInfo(self):
            print("Nombre: "+self.nombre+" "+self.apellido+"\n"
                  "DNI: "+str(self.dni)+"\n"
                  "Tipo de cliente: "+self.tipo_cliente)
            
      def altaCajaAhorroPesos(self):
           self.cajaAhorroPesos = CajaAhorroPesos("caja de ahorro",0,"pesos")

      def getSaldoCajaAhorroPesos(self):
            return self.cajaAhorroPesos
      
      def altaCajaAhorroDolares(self):
           self.cajaAhorroDolares = CajaAhorroDolares("caja de ahorro",0,"dolares")

      def getSaldoCajaAhorroDolares(self):
            return self.cajaAhorroDolares
      
      def altaTarjetaDebito(self,marcaTarjeta):
            if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard" or marcaTarjeta == "Amex"):
                  self.tarjetaDebito = Debito(marcaTarjeta)
            else:
                  print("El cliente solo tiene acceso a tarjetas Mastercard, Visa o Amex") 

      def getTarjetaDebito(self):
            return self.tarjetaDebito
      
      def altaTarjetaCredito(self,marcaTarjeta):
            if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard" or marcaTarjeta == "Amex"):
                  self.tarjetaCredito = Credito(marcaTarjeta,500000,600000)
            else:
                  print("El cliente solo tiene acceso a tarjetas Mastercard, Visa o Amex") 

      def getTarjetaCredito(self):
            return self.tarjetaCredito
            
"""
RESTRICCIONES

- Hasta 5 tarjetas de débito. (Hay que hacer lista de tarjetas de débito)
- Hasta 5 cajas de ahorro en pesos y dólares sin cargos adicionales,
luego se aplica un cargo extra.(Hay que hacer lista de cajas de ahorro)
- Hasta 3 cuentas corrientes sin cargos adicionales. (Hay que hacer lista de cuentas corrientes)
- Tarjetas   VISA,   Mastercard   y/o   American   Express   con   hasta   10
extensiones cada una, con límites de $500,000 en un pago y $600,000 en
cuotas.
- Retiro   máximo   de   $100,000   por   día   sin   comisiones,   con   retiros
ilimitados al mes sin costo adicional.
- Acceso a cuentas de inversión.
- Posibilidad de tener hasta dos chequeras.
- No se aplican comisiones a las transferencias

"""