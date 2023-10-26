from Cliente.cliente import Cliente
from Tarjeta.debito import Debito
from Cuenta.cajaAhorroPesos import CajaAhorroPesos
from Cuenta.cajaAhorroDolares import CajaAhorroDolares



class Classic(Cliente):
      
      def __init__(self,nombre,apellido,dni,nro_cliente):
            super().__init__(nombre,apellido,dni,nro_cliente)
            self.tipo_cliente = "Classic"
            self.limiteCajero = 10000
            self.retirosDisponibles = 5
            self.cajaDeAhorroDisponiblePesos = 1
            self.cajaDeAhorroDisponibleDolares = 1
            self.tarjetasDeDebitoDisponibles = 1

      def getInfo(self):
            print("Nombre: "+self.nombre+" "+self.apellido+"\n"
                  "DNI: "+str(self.dni)+"\n"
                  "Tipo de cliente: "+self.tipo_cliente)
            
      def altaCajaAhorroPesos(self):
           if self.cajaDeAhorroDisponiblePesos > 0:
                  self.cajaAhorroPesos = CajaAhorroPesos("caja de ahorro",0,"pesos")
                  self.cajaDeAhorroDisponiblePesos -= 1
           else:
                  print("Máximo número de cajas de ahorro alcanzado")

      def altaCajaAhorroDolares(self):
           if self.cajaDeAhorroDisponibleDolares > 0:
                  self.cajaAhorroDolares = CajaAhorroDolares("caja de ahorro",0,"dolares")
                  self.cajaDeAhorroDisponibleDolares -= 1
           else:
                 print("Máximo número de cajas de ahorro alcanzado")

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

      def getSaldoCajaAhorroPesos(self):
            if self.cajaDeAhorroDisponiblePesos < 1:
                  return self.cajaAhorroPesos
            else:
                  return "No se ha dado de alta una caja de ahorro en pesos"

      def getSaldoCajaAhorroDolares(self):
            if self.cajaDeAhorroDisponibleDolares < 1:
                  return str(self.cajaAhorroDolares) +". Costo mensual de mantenimiento: U$D 4"
            else:
                  return "No se ha dado de alta una caja de ahorro en dolares"
      
      def altaTarjetaDebito(self,marcaTarjeta):
            if self.tarjetasDeDebitoDisponibles > 0:
                  if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard"):
                        self.tarjetaDebito = Debito(marcaTarjeta)
                  else:
                        print("El cliente solo tiene acceso a tarjetas Mastercard o Visa")
            else: 
                  print("Máximo número de tarjetas de débito alcanzado")

      def getTarjetaDebito(self):
            if self.tarjetasDeDebitoDisponibles > 0:
                  return self.tarjetaDebito
            else:
                  return "No se ha dado de alta una tarjeta de débito"
      
      def enviarTransferencia(self,montoTransfer,monedaTransfer):
            if self.cajaDeAhorroDisponiblePesos == 0 and monedaTransfer == "pesos" :
                  if  self.cajaAhorroPesos.saldo >= montoTransfer * 1.01:
                        self.cajaAhorroPesos.saldo = self.cajaAhorroPesos.saldo - montoTransfer * 1.01
                        print("Transferencia realizada, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.01)+" "+monedaTransfer+"\n"
                              +"Saldo actual: "+str(self.cajaAhorroPesos.saldo) + " "+monedaTransfer)
                  else:
                        print("Error: verifique la moneda y el monto a transferir ingresados")

            elif self.cajaDeAhorroDisponibleDolares == 0 and monedaTransfer == "dolares" :
                  if  self.cajaAhorroDolares.saldo >= montoTransfer * 1.01:
                        self.cajaAhorroDolares.saldo = self.cajaAhorroDolares.saldo - montoTransfer * 1.01
                        print("Transferencia realizada, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.01)+" "+monedaTransfer+"\n"
                              +"Saldo actual: "+str(self.cajaAhorroDolares.saldo) + " "+monedaTransfer)
                  else:
                        print("Error: verifique la moneda y el monto a transferir ingresados")
            else: 
                  print("Error: debe dar de alta una caja de ahorro en pesos o dolares para enviar transferencias")

      def recibirTransferencia(self,montoTransfer,monedaTransfer):
            if self.cajaDeAhorroDisponiblePesos == 0 and monedaTransfer == "pesos":
                  self.cajaAhorroPesos.saldo = self.cajaAhorroPesos.saldo + (montoTransfer * 0.995)
                  print("Transferencia recibida, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.005)+" "+monedaTransfer+"\n"
                        +"Saldo actual: "+str(self.cajaAhorroPesos.saldo) + " "+monedaTransfer)
                  
            elif self.cajaDeAhorroDisponibleDolares == 0 and  monedaTransfer == "dolares":
                  self.cajaAhorroDolares.saldo = self.cajaAhorroDolares.saldo + (montoTransfer * 0.995)
                  print("Transferencia recibida, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.005)+" "+monedaTransfer+"\n"
                        +"Saldo actual: "+str(self.cajaAhorroDolares.saldo) + " "+monedaTransfer)
            else: 
                  print("Error: debe dar de alta una caja de ahorro en la moneda que quiere recibir la transferencia")

      def retiroPorCaja(self,montoRetiro,monedaRetiro):
            if self.cajaDeAhorroDisponiblePesos ==  0 and monedaRetiro == "pesos":
                  if  montoRetiro <= self.cajaAhorroPesos.saldo:
                        self.cajaAhorroPesos.saldo = self.cajaAhorroPesos.saldo - montoRetiro
                        print("Retiro por caja realizado, monto: "+str(montoRetiro)+". Saldo actual: "+str(self.cajaAhorroPesos.saldo)+" "+monedaRetiro)
                  else:
                        print("Error: verifique la moneda y el monto a retirar ingresados")  

            elif self.cajaDeAhorroDisponibleDolares ==  0 and monedaRetiro == "dolares":
                  if montoRetiro <= self.cajaAhorroDolares.saldo:
                        self.cajaAhorroDolares.saldo = self.cajaAhorroDolares.saldo - montoRetiro
                        print("Retiro por caja realizado, monto: "+str(montoRetiro)+". Saldo actual: "+str(self.cajaAhorroDolares.saldo)+" "+monedaRetiro)
                  else:
                        print("Error: verifique la moneda y el monto a retirar ingresados")
            else: 
                  print("Debe dar de alta una caja de ahorro en la moneda deseada para hacer retiros por caja")
                  
      def retiroCajero(self,montoCajero):
            if self.cajaDeAhorroDisponiblePesos == 0:
                  if montoCajero <= self.limiteCajero and montoCajero <= self.cajaAhorroPesos.saldo and self.retirosDisponibles > 0:
                        self.cajaAhorroPesos.saldo -= montoCajero
                        self.limiteCajero -= montoCajero
                        self.retirosDisponibles -= 1
                        print("Retiro por cajero, monto retirado: "+str(montoCajero)+"\n"+
                              "Saldo disponible: "+str(self.cajaAhorroPesos.saldo)+"\n"+
                              "Limite de retiro por cajero disponible: "+str(self.limiteCajero)+"\n"+
                              "Retiros diarios disponibles: "+str(self.retirosDisponibles))
                  elif montoCajero <= self.limiteCajero and montoCajero > self.cajaAhorroPesos.saldo and self.retirosDisponibles > 0:
                        print("Error: Saldo insuficiente")
                  else: 
                        print("Error: Límite diario de retiro de cajero alcanzado, regrese mañana")
            else:
                  print("Debe dar de alta una caja de ahorro en pesos para retirar por cajero")
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
