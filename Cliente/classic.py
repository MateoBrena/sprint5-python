from Cliente.cliente import Cliente
from Tarjeta.debito import Debito
from Cuenta.cajaAhorroPesos import CajaAhorroPesos
from Cuenta.cajaAhorroDolares import CajaAhorroDolares
from Transacciones.transacciones import Transaccion
from datetime import datetime
import json

class Classic(Cliente):
      
      def __init__(self,nombre,apellido,dni,nro_cliente):
            super().__init__(nombre,apellido,dni,nro_cliente)
            self.tipo_cliente = "Classic"
            self.limiteCajero = 10000
            self.retirosDisponibles = 5
            self.cajaDeAhorroDisponiblePesos = 1
            self.cajaDeAhorroDisponibleDolares = 1
            self.tarjetasDeDebitoDisponibles = 1
            self.productos = [] #Se usa para guardar algunos productos y además asignar números de identificación
            self.tarjetas = []
            self.transacciones = [] # Se guardan todas las transacciones para ser mostradas o importadas al archivo .json

      def getInfo(self):
            print("Nombre: "+self.nombre+" "+self.apellido+"\n"
                  "DNI: "+str(self.dni)+"\n"
                  "Tipo de cliente: "+self.tipo_cliente)
            
      def infoJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)
            
      def altaCajaAhorroPesos(self):
           if self.cajaDeAhorroDisponiblePesos > 0:
                  self.cajaAhorroPesos = CajaAhorroPesos("caja de ahorro en pesos",0,"pesos", (100 + len(self.productos) +1))
                  self.cajaDeAhorroDisponiblePesos -= 1
                  self.transacciones.append( Transaccion("aprobada","Alta_Caja_Ahorro_Pesos",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  self.productos += [self.cajaAhorroPesos.tipo]
           else:
                  print("Máximo número de cajas de ahorro alcanzado")
                  self.transacciones.append( Transaccion("rechazada","Alta_Caja_Ahorro_Pesos",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def altaCajaAhorroDolares(self):
           if self.cajaDeAhorroDisponibleDolares > 0:
                  self.cajaAhorroDolares = CajaAhorroDolares("caja de ahorro en dolares",0,"dolares",(100 + len(self.productos) +1))
                  self.cajaDeAhorroDisponibleDolares -= 1
                  self.transacciones.append( Transaccion("aprobada","Alta_Caja_Ahorro_Dolares",len(self.transacciones)+1,self.cajaAhorroDolares.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  self.productos += [self.cajaAhorroDolares.tipo]
           else:
                 print("Máximo número de cajas de ahorro alcanzado")
                 self.transacciones.append( Transaccion("rechazada","Alta_Caja_Ahorro_Dolares",len(self.transacciones)+1,self.cajaAhorroDolares.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def altaCuentaCorrientePesos(self):
            print("El cliente no tiene acceso a cuenta corriente")
            self.transacciones.append( Transaccion("rechazada","Alta_Cuenta_Corriente_Pesos",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def altaCuentaCorrienteDolares(self):
            print("El cliente no tiene acceso a cuenta corriente")
            self.transacciones.append( Transaccion("rechazada","Alta_Cuenta_Corriente_Dolares",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def altaCuentaDeInversion(self):
            print("El cliente no tiene acceso a cuenta de inversión")
            self.transacciones.append( Transaccion("rechazada","Alta_Cuenta_Inversion",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def altaTarjetaCredito(self,marcaTarjeta):
            print("El cliente no tiene acceso a tarjeta de crédito")
            self.transacciones.append( Transaccion("rechazada","Alta_Tarjeta_Credito",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def altaChequera(self):
            print("El cliente no tiene acceso a chequera")
            self.transacciones.append( Transaccion("rechazada","Alta_Chequera",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def compraTarjetaCredito(self):
            print("Error: El cliente no posee tarjeta de crédito")
            self.transacciones.append( Transaccion("rechazada","Compra_Tarjeta_Credito",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def compraTarjetaCreditoCuotas(self):
            print("Error: El cliente no posee tarjeta de crédito")
            self.transacciones.append( Transaccion("rechazada","Compra_Tarjeta_Credito_Cuotas",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def getSaldoCajaAhorroPesos(self):
            if self.cajaDeAhorroDisponiblePesos == 0:
                  print(self.cajaAhorroPesos)
            else:
                  return "No se ha dado de alta una caja de ahorro en pesos"

      def getSaldoCajaAhorroDolares(self):
            if self.cajaDeAhorroDisponibleDolares == 0:
                  print(str(self.cajaAhorroDolares) +". Costo mensual de mantenimiento: U$D 4") 
            else:
                  return "No se ha dado de alta una caja de ahorro en dolares"
      
      def altaTarjetaDebito(self,marcaTarjeta):
            if self.tarjetasDeDebitoDisponibles > 0:
                  if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard"):
                        self.tarjetaDebito = Debito(marcaTarjeta,(1000 + len(self.tarjetas)+1))
                        self.tarjetas += ["Debito"]
                        self.tarjetasDeDebitoDisponibles -= 1
                        self.transacciones.append( Transaccion("aprobada","Alta_Tarjeta_Debito",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  else:
                        print("El cliente solo tiene acceso a tarjetas Mastercard o Visa")
                        self.transacciones.append( Transaccion("rechazada","Alta_Tarjeta_Debito",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            else: 
                  print("Máximo número de tarjetas de débito alcanzado")

      def getTarjetaDebito(self):
            if self.tarjetasDeDebitoDisponibles > 0:
                  print(self.tarjetaDebito)
            else:
                  print("No se ha dado de alta una tarjeta de débito")
      
      def enviarTransferencia(self,montoTransfer,monedaTransfer):
            if self.cajaDeAhorroDisponiblePesos == 0 and monedaTransfer == "pesos" :
                  if  self.cajaAhorroPesos.saldo >= montoTransfer * 1.01:
                        self.cajaAhorroPesos.saldo = self.cajaAhorroPesos.saldo - montoTransfer * 1.01
                        self.transacciones.append( Transaccion("aprobada","Envio_Transeferencia_Pesos",len(self.transacciones)+1,self.cajaAhorroPesos.tipo ,montoTransfer,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Transferencia realizada, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.01)+" "+monedaTransfer+"\n"
                              +"Saldo actual: "+str(self.cajaAhorroPesos.saldo) + " "+monedaTransfer)
                  else:
                        self.transacciones.append( Transaccion("rechazada","Envio_Transeferencia_Pesos",len(self.transacciones)+1,self.cajaAhorroPesos.tipo,montoTransfer,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Error: verifique la moneda y el monto a transferir ingresados")

            elif self.cajaDeAhorroDisponibleDolares == 0 and monedaTransfer == "dolares" :
                  if  self.cajaAhorroDolares.saldo >= montoTransfer * 1.01:
                        self.cajaAhorroDolares.saldo = self.cajaAhorroDolares.saldo - montoTransfer * 1.01
                        self.transacciones.append( Transaccion("aprobada","Envio_Transeferencia_Dolares",len(self.transacciones)+1,self.cajaAhorroDolares.tipo,montoTransfer,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Transferencia realizada, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.01)+" "+monedaTransfer+"\n"
                              +"Saldo actual: "+str(self.cajaAhorroDolares.saldo) + " "+monedaTransfer)
                  else:
                        self.transacciones.append( Transaccion("rechazada","Envio_Transeferencia_Dolares",len(self.transacciones)+1,self.cajaAhorroDolares.tipo,montoTransfer,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Error: Verifique la moneda y el monto a transferir ingresados")
            else: 
                  print("Error: Debe dar de alta una caja de ahorro en la moneda en la que quiere enviar transferencias")

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
                        self.transacciones.append( Transaccion("aprobada","Retiro_Por_Caja_Pesos",len(self.transacciones)+1,self.cajaAhorroPesos.tipo,montoRetiro,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Retiro por caja realizado, monto: "+str(montoRetiro)+". Saldo actual: "+str(self.cajaAhorroPesos.saldo)+" "+monedaRetiro)
                  else:
                        self.transacciones.append( Transaccion("rechazada","Retiro_Por_Caja_Pesos",len(self.transacciones)+1,self.cajaAhorroPesos.tipo,montoRetiro,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Error: verifique la moneda y el monto a retirar ingresados")  

            elif self.cajaDeAhorroDisponibleDolares ==  0 and monedaRetiro == "dolares":
                  if montoRetiro <= self.cajaAhorroDolares.saldo:
                        self.cajaAhorroDolares.saldo = self.cajaAhorroDolares.saldo - montoRetiro
                        self.transacciones.append( Transaccion("aprobada","Retiro_Por_Caja_Dolares",len(self.transacciones)+1,self.cajaAhorroDolares.tipo,montoRetiro,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Retiro por caja realizado, monto: "+str(montoRetiro)+". Saldo actual: "+str(self.cajaAhorroDolares.saldo)+" "+monedaRetiro)
                  else:
                        self.transacciones.append( Transaccion("rechazada","Retiro_Por_Caja_Dolares",len(self.transacciones)+1,self.cajaAhorroDolares.tipo,montoRetiro,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Error: verifique la moneda y el monto a retirar ingresados")
            else: 
                  print("Debe dar de alta una caja de ahorro en la moneda deseada para hacer retiros por caja")
                  
      def retiroCajero(self,montoCajero):
            if self.cajaDeAhorroDisponiblePesos == 0:
                  if montoCajero <= self.limiteCajero and montoCajero <= self.cajaAhorroPesos.saldo and self.retirosDisponibles > 0:
                        self.cajaAhorroPesos.saldo -= montoCajero
                        self.limiteCajero -= montoCajero
                        self.retirosDisponibles -= 1
                        self.transacciones.append( Transaccion("aprobada","Retiro_Cajero_Automatico",len(self.transacciones)+1,self.cajaAhorroPesos.tipo,montoCajero,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Retiro por cajero, monto retirado: "+str(montoCajero)+"\n"+
                              "Saldo disponible: "+str(self.cajaAhorroPesos.saldo)+"\n"+
                              "Limite de retiro por cajero disponible: "+str(self.limiteCajero)+"\n"+
                              "Retiros diarios disponibles: "+str(self.retirosDisponibles))
                  elif montoCajero <= self.limiteCajero and montoCajero > self.cajaAhorroPesos.saldo and self.retirosDisponibles > 0:
                        print("Error: Saldo insuficiente")
                        self.transacciones.append( Transaccion("rechazada","Retiro_Cajero_Automatico",len(self.transacciones)+1,self.cajaAhorroPesos.tipo,montoCajero,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  else: 
                        print("Error: Límite diario de retiro de cajero alcanzado, regrese mañana")
                        self.transacciones.append( Transaccion("rechazada","Retiro_Cajero_Automatico",len(self.transacciones)+1,self.cajaAhorroPesos.tipo,montoCajero,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            else:
                  print("Debe dar de alta una caja de ahorro en pesos para retirar por cajero")

      def compraDolar(self,cantidadDolares):
           if self.cajaDeAhorroDisponiblePesos == 0 and self.cajaDeAhorroDisponibleDolares == 0:
                  montoPesos = Cliente.calcularMontoTotal(350,cantidadDolares)
                  if self.cajaAhorroPesos.saldo >= montoPesos:
                        self.cajaAhorroPesos.saldo -= montoPesos
                        self.cajaAhorroDolares.saldo += cantidadDolares
                        self.transacciones.append( Transaccion("aprobada","Compra_Dolar",len(self.transacciones)+1,self.cajaAhorroPesos.tipo,montoPesos,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Operación realizada: "+str(cantidadDolares)+" dólares comprados por "+str(montoPesos)+" pesos")
                  else:
                        self.transacciones.append( Transaccion("rechazada","Compra_Dolar",len(self.transacciones)+1,self.cajaAhorroPesos.tipo,montoPesos,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Saldo insuficiente")
           else:
                 print("Error: Debe poseer caja de ahorro en pesos y dólares para realizar esta transacción")

      def ventaDolar(self,cantidadDolares):
           if self.cajaDeAhorroDisponiblePesos == 0 and self.cajaDeAhorroDisponibleDolares == 0:
                  montoPesos = 350 * cantidadDolares
                  if self.cajaAhorroDolares.saldo >= cantidadDolares:
                        self.cajaAhorroPesos.saldo += montoPesos
                        self.cajaAhorroDolares.saldo -= cantidadDolares
                        self.transacciones.append( Transaccion("aprobada","Venta_Dolar",len(self.transacciones)+1,self.cajaAhorroDolares.tipo,cantidadDolares,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        print("Operación realizada: "+str(cantidadDolares)+" dólares vendidos por "+str(montoPesos)+" pesos")
                  else:
                        self.transacciones.append( Transaccion("rechazada","Venta_Dolar",len(self.transacciones)+1,self.cajaAhorroDolares.tipo,cantidadDolares,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
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
- Caja de ahorro en pesos.
- Opcionalmente, caja de ahorro en dólares con cargo mensual.
- Hasta 5 retiros de dinero en efectivo sin comisiones, luego se aplica 
una tarifa. El límite diario de retiro es de $10,000 por cajero.
- No tienen acceso a tarjetas de crédito.
- Comisión del 1% por transferencias salientes y 0.5% por 
transferencias entrantes.

"""
