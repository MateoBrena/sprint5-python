from Cliente.cliente import Cliente
from Tarjeta.debito import Debito
from Tarjeta.credito import Credito
from Cuenta.cajaAhorroPesos import CajaAhorroPesos
from Cuenta.cajaAhorroDolares import CajaAhorroDolares
from Cuenta.cuentaCorrientePesos import CuentaCorrientePesos
from Cuenta.cuentaCorrienteDolares import CuentaCorrienteDolares
from Cuenta.CuentaInversiones import CuentaInversiones
from Cuenta.chequera import Chequera
from Transacciones.transacciones import Transaccion
from datetime import datetime
import json

class Gold(Cliente):

      def __init__(self,nombre,apellido,dni,nro_cliente):
            super().__init__(nombre,apellido,dni,nro_cliente)
            self.tipo_cliente = "Gold"
            self.limiteCajero = 20000
            self.tarjetasCredito = [] #Múltiples tarjetas de crédito, por lo cual las almacenamos en una lista
            self.tarjetas = [] #Se usa para almacenar todas las tarjetas (débito o crédito) y además para asignar números de indentificación a las mismas
            self.transacciones = []
            self.productos = []
            self.cajaDeAhorroDisponiblePesos = 1
            self.cajaDeAhorroDisponibleDolares = 1
            self.tarjetasDeDebitoDisponibles = 1
            self.cuentaInversionesDisponibles = 1
            self.chequerasDisponibles = 1
            self.cuentasCorrientesDisponibles = 1
            

      def getInfo(self):
            print("Nombre: "+self.nombre+" "+self.apellido+"\n"
                  "DNI: "+str(self.dni)+"\n"
                  "Tipo de cliente: "+self.tipo_cliente)
            
      def infoJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)
      
      def encontrarTarjeta(self,marcaTarjeta): # Funciona igual que encontrarCaja pero busca una tarjeta por su marca.
            for i in filter(lambda x: x.marca == marcaTarjeta, self.tarjetasCredito):
                  return i
            else:
                  return None
            
      def altaCajaAhorroPesos(self):
           if self.cajaDeAhorroDisponiblePesos > 0:
                  self.cajaAhorroPesos = CajaAhorroPesos("caja de ahorro en pesos",0,"pesos", (200 + len(self.productos) +1))
                  self.cajaDeAhorroDisponiblePesos -= 1
                  self.transacciones.append( Transaccion("aprobada","Alta_Caja_Ahorro_Pesos",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  self.productos += [self.cajaAhorroPesos.tipo]
           else:
                  print("Máximo número de cajas de ahorro alcanzado")
                  self.transacciones.append( Transaccion("rechazada","Alta_Caja_Ahorro_Pesos",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def altaCajaAhorroDolares(self):
           if self.cajaDeAhorroDisponibleDolares > 0:
                  self.cajaAhorroDolares = CajaAhorroDolares("caja de ahorro en dolares",0,"dolares", (200 + len(self.productos) +1))
                  self.cajaDeAhorroDisponibleDolares -= 1
                  self.transacciones.append( Transaccion("aprobada","Alta_Caja_Ahorro_Dolares",len(self.transacciones)+1,self.cajaAhorroDolares.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  self.productos += [self.cajaAhorroDolares.tipo]
           else:
                 print("Máximo número de cajas de ahorro alcanzado")
                 self.transacciones.append( Transaccion("rechazada","Alta_Caja_Ahorro_Dolares",len(self.transacciones)+1,self.cajaAhorroDolares.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def altaCuentaInversiones(self):
           if self.cuentaInversionesDisponibles > 0:
                  self.cuentaInversiones = CuentaInversiones("cuenta de inversiones",0,"pesos", (200 + len(self.productos) +1))
                  self.cuentaInversionesDisponibles -= 1
                  self.transacciones.append( Transaccion("aprobada","Alta_Cuenta_Inversiones",len(self.transacciones)+1,self.cuentaInversiones.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  self.productos += [self.cuentaInversiones.tipo]
           else:
                 self.transacciones.append( Transaccion("rechazada","Alta_Cuenta_Inversiones",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                 print("Máximo número de cuentas de inversiones alcanzado")
      
      def altaChequera(self):
           if self.chequerasDisponibles > 0:
                  self.chequera = Chequera("chequera",50,"pesos", (200 + len(self.productos) +1))
                  self.chequerasDisponibles -= 1
                  self.transacciones.append( Transaccion("aprobada","Alta_Chequera",len(self.transacciones)+1,self.chequera.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  self.productos += [self.chequera.tipo]
           else:
                 self.transacciones.append( Transaccion("rechazada","Alta_Chequera",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                 print("Máximo número de chequeras alcanzado")

      def altaCuentaCorrientePesos(self):
           if self.cuentasCorrientesDisponibles > 0:
                  self.cuentaCorrientePesos = CuentaCorrientePesos("cuenta corriente en pesos",0,"pesos", (200 + len(self.productos) +1))
                  self.cuentasCorrientesDisponibles -= 1
                  self.transacciones.append( Transaccion("aprobada","Alta_Cuenta_Corriente_Pesos",len(self.transacciones)+1,self.cuentaCorrientePesos.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  self.productos += [self.cuentaCorrientePesos.tipo]
           else:
                 self.transacciones.append( Transaccion("rechazada","Alta_Cuenta_Corriente_Pesos",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                 print("Máximo número de cuentas corrientes alcanzado")

      def altaCuentaCorrienteDolares(self):
           if self.cuentasCorrientesDisponibles > 0:
                  self.cuentaCorrienteDolares = CuentaCorrienteDolares("cuenta corriente en dolares",0,"dolares", (200 + len(self.productos) +1))
                  self.cuentasCorrientesDisponibles -= 1
                  self.transacciones.append( Transaccion("aprobada","Alta_Cuenta_Corriente_Dolares",len(self.transacciones)+1,self.cuentaCorrienteDolares.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  self.productos += [self.cuentaCorrienteDolares.tipo]
           else:
                 self.transacciones.append( Transaccion("rechazada","Alta_Cuenta_Corriente_Dolares",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                 print("Máximo número de cuentas corrientes alcanzado")

      def getCuentaCorrientePesos(self):
            if self.cuentasCorrientesDisponibles < 1:
                  print(self.cuentaCorrientePesos)
            else:
                  print("No se ha dado de alta una cuenta corriente en pesos")
      
      def getCuentaCorrienteDolares(self):
            if self.cuentasCorrientesDisponibles < 1:
                  print(self.cuentaCorrienteDolares)
            else:
                  print("No se ha dado de alta una cuenta corriente en dolares")

      def getChequeras(self):
            if self.chequerasDisponibles < 1:
                  print(self.chequera)
            else:
                  print("No se ha dado de alta una chequera")

      def getCuentaInversiones(self):
            if self.cuentaInversionesDisponibles < 1:
                  print(self.cuentaInversiones)
            else:
                  print("No se ha dado de alta una cuenta de inversiones")            

      def getSaldoCajaAhorroPesos(self):
            if self.cajaDeAhorroDisponiblePesos < 1:
                  print(self.cajaAhorroPesos)
            else:
                  print("No se ha dado de alta una caja de ahorro en pesos")

      def getSaldoCajaAhorroDolares(self):
            if self.cajaDeAhorroDisponibleDolares < 1:
                  print(self.cajaAhorroDolares)
            else:
                  print("No se ha dado de alta una caja de ahorro en dolares")
            
      def altaTarjetaDebito(self,marcaTarjeta):
            if self.tarjetasDeDebitoDisponibles > 0:
                  if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard"):
                        self.tarjetaDebito = Debito(marcaTarjeta,(2000 + len(self.tarjetas)+1))
                        self.tarjetasDeDebitoDisponibles -= 1
                        self.transacciones.append( Transaccion("aprobada","Alta_Tarjeta_Debito",len(self.transacciones)+1,marcaTarjeta ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        self.tarjetas += ["Debito"]
                  else:
                        self.transacciones.append( Transaccion("rechazada","Alta_Tarjeta_Debito",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("El cliente solo tiene acceso a tarjetas Mastercard o Visa")
            else: 
                  print("Máximo número de tarjetas de débito alcanzado")

      def getTarjetaDebito(self):
            if self.tarjetasDeDebitoDisponibles < 1:
                  print(self.tarjetaDebito)
            else:
                  print("No se ha dado de alta una tarjeta de débito")
      
      def altaTarjetaCredito(self,marcaTarjeta):
            if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard"):
                  if len(self.tarjetasCredito) < 2 :
                        if len(self.tarjetasCredito) == 0:
                              self.tarjetasCredito.append(Credito(marcaTarjeta,100000,150000,(2000 + len(self.tarjetas)+1)))
                              self.transacciones.append( Transaccion("aprobada","Alta_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                              self.tarjetas += ["Credito"]
                        elif len(self.tarjetasCredito) == 1 and marcaTarjeta != self.tarjetasCredito[0].marca:
                              self.tarjetasCredito.append(Credito(marcaTarjeta,100000,150000,(2000 + len(self.tarjetas)+1)))
                              self.transacciones.append( Transaccion("aprobada","Alta_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                              self.tarjetas += ["Credito"]
                        else:
                              print("Error: Solo puede poseer una tarjeta de cada marca")
                              self.transacciones.append( Transaccion("rechazada","Alta_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

                  elif len(self.tarjetasCredito) == 2:
                        print("Error: Máxima cantidad de tarjetas de crédito alcanzada")
                        self.transacciones.append( Transaccion("rechazada","Alta_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
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
            if len(self.tarjetasCredito) > 0:
                  for i in range(len(self.tarjetasCredito)):
                        print(str(self.tarjetasCredito[i])+"\n") 
            else:
                  print("No se ha dado de alta una tarjeta de crédito")

      def compraTarjetaCredito(self,marcaTarjeta,monto):
            if len(self.tarjetasCredito) > 0:
                tarjetaPago = self.encontrarTarjeta(marcaTarjeta)
            else:
                  print("Error: No se han dado de alta tarjetas de crédito")

            if tarjetaPago.limite >= monto:
                  tarjetaPago.limite -= monto
                  print("Pago de "+str(monto)+" pesos realizado correctamente. El saldo restante en tarjeta "+tarjetaPago.marca+" de id "+str(tarjetaPago.id)+" es de "+str(tarjetaPago.limite)+" pesos")
                  self.transacciones.append( Transaccion("aprobada","Compra_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,monto,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            else:
                  self.transacciones.append( Transaccion("rechazada","Compra_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,monto,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  print("Error: Saldo de tarjeta insuficiente")

      def compraTarjetaCreditoCuotas(self,marcaTarjeta,monto):
            if len(self.tarjetasCredito) > 0:
                tarjetaPago = self.encontrarTarjeta(marcaTarjeta)
            else:
                  print("Error: No se han dado de alta tarjetas de crédito")

            if tarjetaPago.limiteCuotas >= monto:
                  tarjetaPago.limiteCuotas -= monto
                  print("Pago de "+str(monto)+" pesos realizado correctamente. El saldo restante en tarjeta "+tarjetaPago.marca+" de id "+str(tarjetaPago.id)+" es de "+str(tarjetaPago.limiteCuotas)+" pesos")
                  self.transacciones.append( Transaccion("aprobada","Compra_Tarjeta_Credito_Cuotas",len(self.transacciones)+1,marcaTarjeta ,monto,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            else:
                  self.transacciones.append( Transaccion("rechazada","Compra_Tarjeta_Credito_Cuotas",len(self.transacciones)+1,marcaTarjeta ,monto,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  print("Error: Saldo de tarjeta insuficiente")

      def enviarTransferencia(self,montoTransfer,monedaTransfer):
            if self.cajaDeAhorroDisponiblePesos == 0 and monedaTransfer == "pesos":
                  
                  if  self.cajaAhorroPesos.saldo >= montoTransfer * 1.005: # Verifica que el cliente tenga el saldo equivalente al monto 
                        #de la transferencia y la comisión
                        self.cajaAhorroPesos.saldo = self.cajaAhorroPesos.saldo - montoTransfer * 1.005
                        print("Transferencia realizada, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.005)+" "+monedaTransfer+"\n"
                              +"Saldo actual: "+str(self.cajaAhorroPesos.saldo) + " "+monedaTransfer)
                        self.transacciones.append( Transaccion("aprobada","Enviar_Transferencia_Pesos",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,montoTransfer,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  else:
                        print("Error: verifique la moneda y el monto a transferir ingresados")
                        self.transacciones.append( Transaccion("rechazada","Enviar_Transferencia_Pesos",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,montoTransfer,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

            elif self.cajaDeAhorroDisponibleDolares == 0 and monedaTransfer == "dolares":

                  if  self.cajaAhorroDolares.saldo >= montoTransfer * 1.005:
                        self.cajaAhorroDolares.saldo = self.cajaAhorroDolares.saldo - montoTransfer * 1.005
                        print("Transferencia realizada, monto transferido: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.005)+" "+monedaTransfer+"\n"
                              +"Saldo actual: "+str(self.cajaAhorroDolares.saldo) + " "+monedaTransfer)
                        self.transacciones.append( Transaccion("aprobada","Enviar_Transferencia_Dolares",len(self.transacciones)+1,self.cajaAhorroDolares.tipo ,montoTransfer,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  else:
                        self.transacciones.append( Transaccion("rechazada","Enviar_Transferencia_Dolares",len(self.transacciones)+1,self.cajaAhorroDolares.tipo ,montoTransfer,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
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
                        self.transacciones.append( Transaccion("aprobada","Retiro_Por_Caja_Pesos",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,montoRetiro,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  else:
                        self.transacciones.append( Transaccion("rechazada","Retiro_Por_Caja_Pesos",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,montoRetiro,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Error: verifique la moneda y el monto a retirar ingresados")  

            elif self.cajaDeAhorroDisponibleDolares ==  0 and monedaRetiro == "dolares":

                  if montoRetiro <= self.cajaAhorroDolares.saldo:
                        self.cajaAhorroDolares.saldo = self.cajaAhorroDolares.saldo - montoRetiro
                        print("Retiro por caja realizado, monto: "+str(montoRetiro)+". Saldo actual: "+str(self.cajaAhorroDolares.saldo)+" "+monedaRetiro)
                        self.transacciones.append( Transaccion("aprobada","Retiro_Por_Caja_Dolares",len(self.transacciones)+1,self.cajaAhorroDolares.tipo ,montoRetiro,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  else:
                        self.transacciones.append( Transaccion("rechazada","Retiro_Por_Caja_Dolares",len(self.transacciones)+1,self.cajaAhorroDolares.tipo ,montoRetiro,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
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
                        self.transacciones.append( Transaccion("aprobada","Retiro_Cajero_Automatico",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,montoCajero,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        
                  elif montoCajero <= self.limiteCajero and montoCajero > self.cajaAhorroPesos.saldo:
                        print("Error: Saldo insuficiente")
                        self.transacciones.append( Transaccion("rechazada","Retiro_Cajero_Automatico",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,montoCajero,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

                  else: 
                        print("Error: Límite diario de retiro de cajero alcanzado, regrese mañana")
                        self.transacciones.append( Transaccion("rechazada","Retiro_Cajero_Automatico",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,montoCajero,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            else:
                  print("Debe dar de alta una caja de ahorro en pesos para retirar por cajero")

      def compraDolar(self,cantidadDolares):
           if self.cajaDeAhorroDisponiblePesos == 0 and self.cajaDeAhorroDisponibleDolares == 0:
                  montoPesos = Cliente.calcularMontoTotal(350,cantidadDolares) # Utlizzamos calcularMontoTotal() para que al precio 
                  # del dolar se le sumen los impuestos y así conseguir el precio de venta
                  if self.cajaAhorroPesos.saldo >= montoPesos:
                        self.cajaAhorroPesos.saldo -= montoPesos
                        self.cajaAhorroDolares.saldo += cantidadDolares
                        print("Operación realizada: "+str(cantidadDolares)+" dólares comprados por "+str(montoPesos)+" pesos")
                        self.transacciones.append( Transaccion("aprobada","Compra_Dolar",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,montoPesos,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  else:
                        print("Saldo insuficiente")
                        self.transacciones.append( Transaccion("rechazada","Compra_Dolar",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,montoPesos,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
           else:
                 print("Error: Debe poseer caja de ahorro en pesos y dólares para realizar esta transacción")

      def ventaDolar(self,cantidadDolares):
           if self.cajaDeAhorroDisponiblePesos == 0 and self.cajaDeAhorroDisponibleDolares == 0:
                  montoPesos = 350 * cantidadDolares #El precio de compra es el mismo al de venta pero no le sumamos los impuestos
                  if self.cajaAhorroDolares.saldo >= cantidadDolares:
                        self.cajaAhorroPesos.saldo += montoPesos
                        self.cajaAhorroDolares.saldo -= cantidadDolares
                        print("Operación realizada: "+str(cantidadDolares)+" dolares vendidos por "+str(montoPesos)+" pesos")
                        self.transacciones.append( Transaccion("aprobada","Venta_Dolar",len(self.transacciones)+1,self.cajaAhorroDolares.tipo ,cantidadDolares,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  else:
                        self.transacciones.append( Transaccion("rechazada","Venta_Dolar",len(self.transacciones)+1,self.cajaAhorroDolares.tipo ,cantidadDolares,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Saldo insuficiente")
           else:
                 print("Error: Debe poseer caja de ahorro en pesos y dólares para realizar esta transacción")

      def mostrarTransacciones(self):
            for i in range(len(self.transacciones)):
                  print(str(self.transacciones[i])+"\n")

      def exportarResumenTransacciones(self):
         formato_json = self.infoJson()
         with open("Resumen_" + str(self.dni) + ".json", "w") as nuevo_file:
           nuevo_file.write(formato_json)        



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