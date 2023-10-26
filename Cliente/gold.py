from Cliente.cliente import Cliente
from Tarjeta.debito import Debito
from Tarjeta.credito import Credito
from Cuenta.cajaAhorroPesos import CajaAhorroPesos
from Cuenta.cajaAhorroDolares import CajaAhorroDolares
from Cuenta.cuentaCorrientePesos import CuentaCorrientePesos
from Cuenta.cuentaCorrienteDolares import CuentaCorrienteDolares
from Cuenta.CuentaInversiones import CuentaInversiones
from Cuenta.chequera import Chequera

class Gold(Cliente):

      def __init__(self,nombre,apellido,dni,nro_cliente):
            super().__init__(nombre,apellido,dni,nro_cliente)
            self.tipo_cliente = "Gold"
            self.limiteCajero = 20000
            self.tarjetasCredito = []
            self.cajaDeAhorroDisponiblePesos = 1
            self.cajaDeAhorroDisponibleDolares = 1
            self.tarjetasDeDebitoDisponibles = 1
            self.cuentaInversionesDisponibles = 1
            self.cantidadChequerasDisponibles = 1
            self.cantidadCuentasCorrientesDisponibles = 1

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

      def altaCuentaInversiones(self):
           if self.cuentaInversionesDisponibles > 0:
                  self.cuentaInversiones = CuentaInversiones("cuenta de inversiones",0,"pesos")
                  self.cuentaInversionesDisponibles -= 1
           else:
                 print("Máximo número de cuentas de inversiones alcanzado")
      
      def altaChequera(self):
           if self.cantidadChequerasDisponibles > 0:
                  self.chequera = Chequera("chequera",50,"pesos")
                  self.cantidadChequerasDisponibles -= 1
           else:
                 print("Máximo número de chequeras alcanzado")

      def altaCuentaCorrientePesos(self):
           if self.cantidadCuentasCorrientesDisponibles > 0:
                  self.cuentaCorrientePesos = CuentaCorrientePesos("cuenta corriente",0,"pesos")
                  self.cantidadCuentasCorrientesDisponibles -= 1
           else:
                 print("Máximo número de cuentas corrientes alcanzado")

      def altaCuentaCorrienteDolares(self):
           if self.cantidadCuentasCorrientesDisponibles > 0:
                  self.cuentaCorrienteDolares = CuentaCorrienteDolares("cuenta corriente",0,"dolares")
                  self.cantidadCuentasCorrientesDisponibles -= 1
           else:
                 print("Máximo número de cuentas corrientes alcanzado")

      def getCuentaCorrientePesos(self):
            if self.cantidadCuentasCorrientesDisponibles < 1:
                  return self.cuentaCorrientePesos
            else:
                  return "No se ha dado de alta una cuenta corriente en pesos"
      
      def getCuentaCorrienteDolares(self):
            if self.cantidadCuentasCorrientesDisponibles < 1:
                  return self.cuentaCorrienteDolares
            else:
                  return "No se ha dado de alta una cuenta corriente en dolares"

      def getChequera(self):
            if self.cantidadChequerasDisponibles < 1:
                  return self.chequera
            else:
                  return "No se ha dado de alta una chequera"

      def getCuentaInversiones(self):
            if self.cuentaInversionesDisponibles < 1:
                  return self.cuentaInversiones
            else:
                  return "No se ha dado de alta una chequera"            

      def getSaldoCajaAhorroPesos(self):
            if self.cajaDeAhorroDisponiblePesos < 1:
                  return self.cajaAhorroPesos
            else:
                  return "No se ha dado de alta una caja de ahorro en pesos"

      def getSaldoCajaAhorroDolares(self):
            if self.cajaDeAhorroDisponibleDolares < 1:
                  return self.cajaAhorroDolares
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
            if self.tarjetasDeDebitoDisponibles < 1:
                  return self.tarjetaDebito
            else:
                  return "No se ha dado de alta una tarjeta de débito"
      
      def altaTarjetaCredito(self,marcaTarjeta):
            if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard"):
                  if len(self.tarjetasCredito) < 2 :
                        if len(self.tarjetasCredito) == 0:
                              self.tarjetasCredito.append(Credito(marcaTarjeta,100000,150000))
                        elif len(self.tarjetasCredito) == 1 and marcaTarjeta != self.tarjetasCredito[0].marca:
                              self.tarjetasCredito.append(Credito(marcaTarjeta,100000,150000))
                        else:
                              print("Error: Solo puede poseer una tarjeta de cada marca")
                  elif len(self.tarjetasCredito) == 2:
                        print("Error: Máxima cantidad de tarjetas de crédito alcanzada")
            else:
                  print("El cliente solo tiene acceso a tarjetas Mastercard o Visa") 
      
      def agregarExtension(self, tarjetaElegida):
            if (len(self.tarjetasCredito) > 0 and tarjetaElegida == self.tarjetasCredito[0].marca) and self.tarjetasCredito[0].extensiones < 5:
                  self.tarjetasCredito[0].extensiones += 1
            elif (len(self.tarjetasCredito) > 0 and tarjetaElegida == self.tarjetasCredito[0].marca) and self.tarjetasCredito[0].extensiones == 5:
                  print("No se pueden agregar más extensiones")
            elif (len(self.tarjetasCredito) > 0 and tarjetaElegida == self.tarjetasCredito[1].marca) and self.tarjetasCredito[1].extensiones < 5:
                  self.tarjetasCredito[1].extensiones += 1
            elif (len(self.tarjetasCredito) > 0 and tarjetaElegida == self.tarjetasCredito[1].marca) and self.tarjetasCredito[1].extensiones == 5:
                  print("No se pueden agregar más extensiones")
            elif len(self.tarjetasCredito) == 0:
                  print("No se posee ninguna tarjeta de crédito, no se pueden agregar extensiones")

      def getTarjetasCredito(self):
            if len(self.tarjetasCredito) < 0:
                  for i in range(len(self.tarjetasCredito)):
                        print(str(self.tarjetasCredito[i])+"\n") 
            else:
                  print("No se ha dado de alta una tarjeta de crédito")

      def enviarTransferencia(self,montoTransfer,monedaTransfer):
            if self.cajaDeAhorroDisponiblePesos == 0 and monedaTransfer == "pesos":
                  
                  if  self.cajaAhorroPesos.saldo >= montoTransfer * 1.005:
                        self.cajaAhorroPesos.saldo = self.cajaAhorroPesos.saldo - montoTransfer * 1.005
                        print("Transferencia realizada, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.005)+" "+monedaTransfer+"\n"
                              +"Saldo actual: "+str(self.cajaAhorroPesos.saldo) + " "+monedaTransfer)
                  else:
                        print("Error: verifique la moneda y el monto a transferir ingresados")

            elif self.cajaDeAhorroDisponibleDolares == 0 and monedaTransfer == "dolares":

                  if  self.cajaAhorroDolares.saldo >= montoTransfer * 1.005:
                        self.cajaAhorroDolares.saldo = self.cajaAhorroDolares.saldo - montoTransfer * 1.005
                        print("Transferencia realizada, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.005)+" "+monedaTransfer+"\n"
                              +"Saldo actual: "+str(self.cajaAhorroDolares.saldo) + " "+monedaTransfer)
                  else:
                        print("Error: verifique la moneda y el monto a transferir ingresados")
            else: 
                  print("Error: debe dar de alta una caja de ahorro en pesos o dolares para enviar transferencias")

      def recibirTransferencia(self,montoTransfer,monedaTransfer):
            if self.cajaDeAhorroDisponiblePesos == 0 and monedaTransfer == "pesos":
                  self.cajaAhorroPesos.saldo = self.cajaAhorroPesos.saldo + (montoTransfer * 0.999)
                  print("Transferencia recibida, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.001)+" "+monedaTransfer+"\n"
                        +"Saldo actual: "+str(self.cajaAhorroPesos.saldo) + " "+monedaTransfer)
                  
            elif self.cajaDeAhorroDisponibleDolares == 0 and  monedaTransfer == "dolares":
                  self.cajaAhorroDolares.saldo = self.cajaAhorroDolares.saldo + (montoTransfer * 0.999)
                  print("Transferencia recibida, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.001)+" "+monedaTransfer+"\n"
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

                  if montoCajero <= self.limiteCajero and montoCajero <= self.cajaAhorroPesos.saldo:
                        self.cajaAhorroPesos.saldo -= montoCajero
                        self.limiteCajero -= montoCajero
                        print("Retiro por cajero, monto retirado: "+str(montoCajero)+"\n"+
                              "Saldo disponible: "+str(self.cajaAhorroPesos.saldo)+"\n"+
                              "Limite de retiro por cajero disponible: "+str(self.limiteCajero))
                        
                  elif montoCajero <= self.limiteCajero and montoCajero > self.cajaAhorroPesos.saldo:
                        print("Error: Saldo insuficiente")

                  else: 
                        print("Error: Límite diario de retiro de cajero alcanzado, regrese mañana")
            else:
                  print("Debe dar de alta una caja de ahorro en pesos para retirar por cajero")
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

"""