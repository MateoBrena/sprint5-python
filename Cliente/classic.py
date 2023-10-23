from Cliente.cliente import Cliente
from Tarjeta.debito import Debito
from Cuenta.cajaAhorroPesos import CajaAhorroPesos
from Cuenta.cajaAhorroDolares import CajaAhorroDolares


class Classic(Cliente):

      def __init__(self,nombre,apellido,dni,nro_cliente):
            super().__init__(nombre,apellido,dni,nro_cliente)
            self.tipo_cliente = "Classic"

      def getInfo(self):
            print("Nombre: "+self.nombre+" "+self.apellido+"\n"
                  "DNI: "+str(self.dni)+"\n"
                  "Tipo de cliente: "+self.tipo_cliente)
            
      def altaCajaAhorroPesos(self):
           self.cajaAhorroPesos = CajaAhorroPesos("caja de ahorro",0,"pesos")
      
      def altaCajaAhorroDolares(self):
           self.cajaAhorroDolares = CajaAhorroDolares("caja de ahorro",0,"dolares")

      def altaCuentaCorrientePesos(self):
            print("El cliente no tiene acceso a cuenta corriente")

      def altaCuentaCorrienteDolares(self):
            print("El cliente no tiene acceso a cuenta corriente")

      def altaCuentaDeInversion(self):
            print("El cliente no tiene acceso a cuenta de inversión")

      def altaTarjetaCredito(self):
            print("El cliente no tiene acceso a tarjeta de crédito")

      def altaChequera(self):
            print("El cliente no tiene acceso a chequera")

      def compraTarjetaCredito(self):
            print("Error: El cliente no posee tarjeta de crédito")

      def compraTarjetaCreditoCuotas(self):
            print("Error: El cliente no posee tarjeta de crédito")

      def getSaldoPesos(self):
            return self.cajaAhorroPesos
      
      def getSaldoDolares(self):
            return str(self.cajaAhorroDolares) +". Costo mensual de mantenimiento: U$D 4"
      
      def altaTarjetaDebito(self,marcaTarjeta):
            if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard"):
                  self.tarjetaDebito = Debito(marcaTarjeta)
            else:
                  print("El cliente solo tiene acceso a tarjetas Mastercard o Visa") 

      def getTarjetaDebito(self):
            return self.tarjetaDebito
      
      def enviarTransferencia(self,montoTransfer,monedaTransfer):
            if monedaTransfer == "pesos" and self.cajaAhorroPesos.saldo >= montoTransfer * 1.01:
                  self.cajaAhorroPesos.saldo = self.cajaAhorroPesos.saldo - montoTransfer * 1.01
                  print("Transferencia realizada, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.01)+" "+monedaTransfer+"\n"
                        +"Saldo actual: "+str(self.cajaAhorroPesos.saldo) + " "+monedaTransfer)
            elif monedaTransfer == "dolares" and self.cajaAhorroDolares.saldo >= montoTransfer * 1.01:
                  self.cajaAhorroDolares.saldo = self.cajaAhorroDolares.saldo - montoTransfer * 1.01
                  print("Transferencia realizada, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.01)+" "+monedaTransfer+"\n"
                        +"Saldo actual: "+str(self.cajaAhorroDolares.saldo) + " "+monedaTransfer)
            else:
                  print("Error: verifique la moneda y el monto a transferir ingresados")

      def recibirTransferencia(self,montoTransfer,monedaTransfer):
            if monedaTransfer == "pesos":
                  self.cajaAhorroPesos.saldo = self.cajaAhorroPesos.saldo + (montoTransfer * 0.995)
                  print("Transferencia recibida, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.005)+" "+monedaTransfer+"\n"
                        +"Saldo actual: "+str(self.cajaAhorroPesos.saldo) + " "+monedaTransfer)
            elif monedaTransfer == "dolares":
                  self.cajaAhorroDolares.saldo = self.cajaAhorroDolares.saldo + (montoTransfer * 0.995)
                  print("Transferencia recibida, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.005)+" "+monedaTransfer+"\n"
                        +"Saldo actual: "+str(self.cajaAhorroDolares.saldo) + " "+monedaTransfer)
            
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
