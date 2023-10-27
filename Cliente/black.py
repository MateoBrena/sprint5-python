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

class Black(Cliente):
      
      def __init__(self,nombre,apellido,dni,nro_cliente):
            super().__init__(nombre,apellido,dni,nro_cliente)
            self.tipo_cliente = "Black"
            self.limiteCajero = 100000
            self.cuentasCorrientesDisponibles = 3
            self.cuentaInversionesDisponibles = 2
            self.chequerasDisponibles = 2
            self.tarjetasCredito = []
            self.tarjetasDebito = [] #Este cliente tiene tarjetas de crédito y débito separadas 
            # ya que es el único que puede poseer múltiples de cada una
            self.cajasAhorro = [] #Al tener la posibilidad de hasta 5 cajas de ahorro, usamos una lista para almacenarlas
            self.tarjetas = []
            self.productos = []
            self.transacciones = []


      def getInfo(self): #Obtener información básica del cliente
            print("Nombre: "+self.nombre+" "+self.apellido+"\n"
                  "DNI: "+str(self.dni)+"\n"
                  "Tipo de cliente: "+self.tipo_cliente)
            
      def infoJson(self): #Tomamos toda la información del cliente y 
        # la convertimos a JSON para poder exportarla al archivo cuando sea necesario
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)
      
      def encontrarCaja(self,nroCaja): #Devuelve una caja de ahorro que coincida con el nro_cuenta buscado si es que existe
            for i in filter(lambda x: x.nro_cuenta == nroCaja, self.cajasAhorro):
                  return i
            else:
                  return None
            
      def encontrarTarjeta(self,marcaTarjeta): # Funciona igual que encontrarCaja pero busca una tarjeta por su marca.
            for i in filter(lambda x: x.marca == marcaTarjeta, self.tarjetasCredito):
                  return i
            else:
                  return None
            
      def altaCajaAhorroPesos(self):
           if len(self.cajasAhorro) < 5:
                  self.cajasAhorro.append(CajaAhorroPesos("caja de ahorro en pesos",0,"pesos" ,(300 + len(self.productos) +1))) #Crea la caja de ahorro y la introduce dentro de la lista CajasAhorro
                  self.productos += ["caja de ahorro en pesos"] # Agrega el tipo de producto a la lista, cuya longitud debe aumentar para asignar a nuevos productos nuevos valores de identificación que no se repitan
                  self.transacciones.append(Transaccion("aprobada","Alta_Caja_Ahorro",len(self.transacciones)+1,"caja de ahorro en pesos" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S"))) #Crea la transacción y la introduce en la lista transacciones para poder ser utilizada cuando sea necesario

      def getSaldoCajaAhorroPesos(self,nroDeCuenta): #Utilizada para devolver la información sobre una caja de ahorro,
             # se busca por el nro_cuenta de la caja usando la función encontrarCaja()
             if len(self.cajasAhorro) > 0:
                cuentaSeleccionada = self.encontrarCaja(nroDeCuenta)
             else:
                  print("Error: No se han dado de alta cajas de ahorro en pesos")

             print(cuentaSeleccionada)
      
      def altaCajaAhorroDolares(self):
           if len(self.cajasAhorro) < 5:
                  self.cajasAhorro.append(CajaAhorroDolares("caja de ahorro en dolares",0,"dolares",(300 + len(self.productos) +1))) 
                  self.productos += ["caja de ahorro en dolares"]
                  self.transacciones.append(Transaccion("aprobada","Alta_Caja_Ahorro",len(self.transacciones)+1,"caja de ahorro en dolares" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def getSaldoCajaAhorroDolares(self,nroCuenta):
             if len(self.cajasAhorro) > 0:
                cuentaSeleccionadaD = self.encontrarCaja(nroCuenta)
             else:
                  print("Error: No se han dado de alta cajas de ahorro en dolares")

             print(cuentaSeleccionadaD)
      
      def altaCuentaInversiones(self):
           if self.cuentaInversionesDisponibles > 0:
                  self.cuentaInversiones = CuentaInversiones("cuenta de inversiones",0,"pesos",(300 + len(self.productos) +1))
                  self.cuentaInversionesDisponibles -= 1
                  self.transacciones.append( Transaccion("aprobada","Alta_Cuenta_Inversiones",len(self.transacciones)+1,self.cuentaInversiones.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  self.productos += [self.cuentaInversiones.tipo]
           else:
                 self.transacciones.append( Transaccion("rechazada","Alta_Cuenta_Inversiones",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                 print("Máximo número de cuentas de inversiones alcanzado")

      def altaChequera(self):
           if self.chequerasDisponibles > 0:
                  self.chequera = Chequera("chequera",100,"pesos", (300 + len(self.productos) +1))
                  self.chequerasDisponibles -= 1
                  self.transacciones.append( Transaccion("aprobada","Alta_Chequera",len(self.transacciones)+1,self.chequera.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  self.productos += [self.chequera.tipo]
           else:
                 self.transacciones.append( Transaccion("rechazada","Alta_Chequera",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                 print("Máximo número de chequeras alcanzado")

      def getChequeras(self):
            if self.chequerasDisponibles < 2:
                  print(self.chequera)
            else:
                  print("No se ha dado de alta una chequera")

      def getTarjetasDebito(self):
            if len(self.tarjetasDebito) > 0:
                  for i in range(len(self.tarjetasDebito)):
                        print(str(self.tarjetasDebito[i])+"\n") 
            else:
                  print("No se ha dado de alta una tarjeta de débito")

      def getCuentaInversiones(self):
            if self.cuentaInversionesDisponibles < 2:
                  print(self.cuentaInversiones)
            else:
                  print("No se ha dado de alta una cuenta de inversiones"  )
            
      def altaCuentaCorrientePesos(self):
           if self.cuentasCorrientesDisponibles > 0:
                  self.cuentaCorrientePesos = CuentaCorrientePesos("cuenta corriente en pesos",0,"pesos",(300 + len(self.productos) +1))
                  self.cuentasCorrientesDisponibles -= 1
                  self.transacciones.append( Transaccion("aprobada","Alta_Cuenta_Corriente_Pesos",len(self.transacciones)+1,self.cuentaCorrientePesos.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  self.productos += [self.cuentaCorrientePesos.tipo]
           else:
                 self.transacciones.append( Transaccion("rechazada","Alta_Cuenta_Corriente_Pesos",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                 print("Máximo número de cuentas corrientes alcanzado")

      def altaCuentaCorrienteDolares(self):
           if self.cuentasCorrientesDisponibles > 0:
                  self.cuentaCorrienteDolares = CuentaCorrienteDolares("cuenta corriente en dolares",0,"dolares",(300 + len(self.productos) +1))
                  self.cuentasCorrientesDisponibles -= 1
                  self.transacciones.append( Transaccion("aprobada","Alta_Cuenta_Corriente_Dolares",len(self.transacciones)+1,self.cuentaCorrienteDolares.tipo ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  self.productos += [self.cuentaCorrienteDolares.tipo]
           else:
                 self.transacciones.append( Transaccion("rechazada","Alta_Cuenta_Corriente_Dolares",len(self.transacciones)+1,"N/A" ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                 print("Máximo número de cuentas corrientes alcanzado")

      def getCuentaCorrientePesos(self):
            if self.cuentasCorrientesDisponibles < 3:
                  print(self.cuentaCorrientePesos)
            else:
                  print("No se ha dado de alta una cuenta corriente en pesos")
      
      def getCuentaCorrienteDolares(self):
            if self.cuentasCorrientesDisponibles < 3:
                  print(self.cuentaCorrienteDolares)
            else:
                  print("No se ha dado de alta una cuenta corriente en dolares")

      def altaTarjetaDebito(self,marcaTarjeta):
            if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard" or marcaTarjeta == "Amex"):
                  if len(self.tarjetasDebito) < 5 : #Máximo 5 tarjetas de débito
                        self.tarjetasDebito.append(Debito(marcaTarjeta,(3000 + len(self.tarjetas)+1)))
                        self.tarjetas += ["Debito"] #Funciona de la misma forma que productos, pero con las tarjetas del cliente
                        self.transacciones.append( Transaccion("aprobada","Alta_Tarjeta_Debito",len(self.transacciones)+1,marcaTarjeta ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  else:
                        print("El cliente solo tiene acceso a 5 tarjetas de débito")
                        self.transacciones.append( Transaccion("rechazada","Alta_Tarjeta_Debito",len(self.transacciones)+1,marcaTarjeta ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            else:
                  print("El cliente solo tiene acceso a tarjetas Mastercard, Visa o Amex")
      
      def altaTarjetaCredito(self,marcaTarjeta):
            if(marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard" or marcaTarjeta == "Amex"):
                  if len(self.tarjetasCredito) < 3 : #No quedó muy prolijo, pero queríamos asegurarnos 
                        #de que el cliente no pudiera crear dos tarjetas de la misma marca, sino una de cada una
                        if len(self.tarjetasCredito) == 0:
                              self.tarjetasCredito.append(Credito(marcaTarjeta,500000,600000,(3000 + len(self.tarjetas)+1)))
                              self.tarjetas += ["Credito"]
                              self.transacciones.append( Transaccion("aprobada","Alta_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        elif len(self.tarjetasCredito) == 1 and marcaTarjeta != self.tarjetasCredito[0].marca:
                              self.tarjetasCredito.append(Credito(marcaTarjeta,500000,600000,(3000 + len(self.tarjetas)+1)))
                              self.tarjetas += ["Credito"]
                              self.transacciones.append( Transaccion("aprobada","Alta_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        elif (len(self.tarjetasCredito) == 2) and (marcaTarjeta != self.tarjetasCredito[0].marca and marcaTarjeta != self.tarjetasCredito[1].marca):
                              self.tarjetasCredito.append(Credito(marcaTarjeta,500000,600000,(3000 + len(self.tarjetas)+1)))
                              self.tarjetas += ["Credito"]
                              self.transacciones.append( Transaccion("aprobada","Alta_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                        else:
                              print("Error: Solo puede poseer una tarjeta de cada marca")
                              self.transacciones.append( Transaccion("rechazada","Alta_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

                  elif len(self.tarjetasCredito) == 3:
                        print("Error: Máxima cantidad de tarjetas de crédito alcanzada")
                        self.transacciones.append( Transaccion("rechazada","Alta_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,"N/A",datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            else:
                  print("El cliente solo tiene acceso a tarjetas Mastercard, Visa o Amex") 

      def getTarjetasCredito(self):
            if len(self.tarjetasCredito) > 0: # Recorre la lista de tarjetas e imprime todas las que tenga almacenadas dentro
                  for i in range(len(self.tarjetasCredito)):
                        print(str(self.tarjetasCredito[i])+"\n") 
            else:
                  print("No se ha dado de alta una tarjeta de crédito")

      def agregarExtension(self, tarjetaElegida): #Agrega extensiones a las tarjetas de crédito, 
            # según la marca elegida cuando se ejecute la función
            if (len(self.tarjetasCredito) > 0 and tarjetaElegida == self.tarjetasCredito[0].marca) and self.tarjetasCredito[0].extensiones < 10:
                  self.tarjetasCredito[0].extensiones += 1
            elif (len(self.tarjetasCredito) > 0 and tarjetaElegida == self.tarjetasCredito[0].marca) and self.tarjetasCredito[0].extensiones == 10:
                  print("No se pueden agregar más extensiones")
            elif (len(self.tarjetasCredito) > 0 and tarjetaElegida == self.tarjetasCredito[1].marca) and self.tarjetasCredito[1].extensiones < 10:
                  self.tarjetasCredito[1].extensiones += 1
            elif (len(self.tarjetasCredito) > 0 and tarjetaElegida == self.tarjetasCredito[1].marca) and self.tarjetasCredito[1].extensiones == 10:
                  print("No se pueden agregar más extensiones")
            elif (len(self.tarjetasCredito) > 0 and tarjetaElegida == self.tarjetasCredito[2].marca) and self.tarjetasCredito[2].extensiones < 10:
                  self.tarjetasCredito[2].extensiones += 1
            elif (len(self.tarjetasCredito) > 0 and tarjetaElegida == self.tarjetasCredito[2].marca) and self.tarjetasCredito[2].extensiones == 10:
                  print("No se pueden agregar más extensiones")
            elif len(self.tarjetasCredito) == 0:
                  print("No se posee ninguna tarjeta de crédito, no se pueden agregar extensiones")


      def compraTarjetaCredito(self,marcaTarjeta,monto): #En la función es obligatorio pasar por parámetro la marca de la tarjeta 
                #Con la que se quiera realizar la compra. Ya que solo puede haber una de cada una
            if len(self.tarjetasCredito) > 0:
                tarjetaPago = self.encontrarTarjeta(marcaTarjeta) 
            else:
                  print("Error: No se han dado de alta tarjetas de crédito")

            if tarjetaPago.limite >= monto:
                  tarjetaPago.limite -= monto
                  print("Pago de "+str(monto)+" pesos realizado correctamente. El saldo restante en tarjeta "+tarjetaPago.marca+" de id "+str(tarjetaPago.id)+" es de "+str(tarjetaPago.limite)+" pesos")
                  self.transacciones.append( Transaccion("aprobada","Compra_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,monto,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            else:
                  print("Error: Saldo de tarjeta insuficiente")
                  self.transacciones.append( Transaccion("rechazada","Compra_Tarjeta_Credito",len(self.transacciones)+1,marcaTarjeta ,monto,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def compraTarjetaCreditoCuotas(self,marcaTarjeta,monto): #Funciona de la misma manera que la función anterior, 
            # Pero toma en cuenta el limite de cuotas
            if len(self.tarjetasCredito) > 0:
                tarjetaPago = self.encontrarTarjeta(marcaTarjeta) 
            else:
                  print("Error: No se han dado de alta tarjetas de crédito")

            if tarjetaPago.limiteCuotas >= monto:
                  tarjetaPago.limiteCuotas -= monto
                  print("Pago de "+str(monto)+" pesos realizado correctamente. El saldo restante en tarjeta "+tarjetaPago.marca+" de id "+str(tarjetaPago.id)+" es de "+str(tarjetaPago.limiteCuotas)+" pesos")
                  self.transacciones.append( Transaccion("aprobada","Compra_Tarjeta_Credito_Cuotas",len(self.transacciones)+1,marcaTarjeta ,monto,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            else:
                  print("Error: Saldo de tarjeta insuficiente")
                  self.transacciones.append( Transaccion("rechazada","Compra_Tarjeta_Credito_Cuotas",len(self.transacciones)+1,marcaTarjeta ,monto,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))


      def recibirTransferencia(self,montoTransfer,monedaTransfer,nroCuentaDestino): #A diferencia de los otros clientes, cuando se 
            # trata de un cliente Black, al ser los únicos capaces de poseer más de una caja de ahorro
            # # debemos especificar el nro_cuenta de las mismas para seleccionar una y realizar las operaciones
            if len(self.cajasAhorro) > 0:
                  cuentaEncontrada = self.encontrarCaja(nroCuentaDestino)
            else:
                  print("Error: No se han dado de alta tarjetas de crédito")

            if cuentaEncontrada.moneda == monedaTransfer:
                  cuentaEncontrada.saldo += montoTransfer
                  print("Transferencia recibida, monto: "+str(montoTransfer)+" "+monedaTransfer+". Saldo actual: "+str(cuentaEncontrada.saldo) + " "+monedaTransfer)
            
            elif cuentaEncontrada.moneda != monedaTransfer:
                  print("Error: Asegúrese de transferir la moneda correcta a la caja de ahorro")

      def enviarTransferencia(self,montoTransfer,monedaTransfer,nroCuentaDestino):
            if len(self.cajasAhorro) > 0:
                 cuentaUbicada = self.encontrarCaja(nroCuentaDestino)
            else:
                  print("Error: No se han dado de alta cajas de ahorro")

            if cuentaUbicada.moneda == monedaTransfer and cuentaUbicada.saldo >= montoTransfer:
                  cuentaUbicada.saldo -= montoTransfer
                  print("Transferencia realizada correctamente, monto transferido: "+str(montoTransfer)+" "+monedaTransfer+". Saldo actual: "+str(cuentaUbicada.saldo) + " "+monedaTransfer)
                  self.transacciones.append( Transaccion("aprobada","Enviar_Transferencia",len(self.transacciones)+1,cuentaUbicada.tipo ,montoTransfer,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

            elif cuentaUbicada.saldo < montoTransfer:
                  print("Error: Saldo insuficiente")
                  self.transacciones.append( Transaccion("rechazada","Enviar_Transferencia",len(self.transacciones)+1,cuentaUbicada.tipo ,montoTransfer,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

            elif cuentaUbicada.moneda != monedaTransfer:
                  print("Error: Asegúrese de transferir la moneda correcta desde la caja de ahorro")

      def retiroPorCaja(self,montoRetiro,monedaRetiro,nroCuentaRetiro):
            if len(self.cajasAhorro) > 0:
                  cuentaParaRetiro = self.encontrarCaja(nroCuentaRetiro)

            else:
                  print("Error: No se han dado de alta cajas de ahorro")

            if cuentaParaRetiro.moneda == monedaRetiro and cuentaParaRetiro.saldo >= montoRetiro:
                  cuentaParaRetiro.saldo -= montoRetiro
                  print("Retiro realizado correctamente, monto retirado: "+str(montoRetiro)+" "+monedaRetiro+". Saldo actual: "+str(cuentaParaRetiro.saldo) + " "+monedaRetiro)
                  self.transacciones.append(Transaccion("aprobada","Retiro_Por_Caja",len(self.transacciones)+1,cuentaParaRetiro.tipo ,montoRetiro,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

            elif cuentaParaRetiro.saldo < montoRetiro:
                  print("Error: Saldo insuficiente")
                  self.transacciones.append( Transaccion("rechazada","Retiro_Por_Caja",len(self.transacciones)+1,cuentaParaRetiro.tipo ,montoRetiro,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

            elif cuentaParaRetiro.moneda != monedaRetiro:
                  print("Error: Asegúrese de solicitar la moneda correcta desde la caja de ahorro para su retiro")


      def encontrarCajaEnPesos(self,monedaCaja):#Devuelve una caja de ahorro en pesos si es que existe
            for i in filter(lambda x: x.moneda == monedaCaja, self.cajasAhorro):
                  return i
            else:
                  return None
            
      def encontrarCajaEnDolares(self,monedaCaja): #Devuelve una caja de ahorro en dólares si es que existe
            for i in filter(lambda x: x.moneda == monedaCaja, self.cajasAhorro):
                  return i
            else:
                  return None

      def retiroCajero(self,montoCajero,nroCuentaCajero): #Nuevamente, debemos especificar un número de cuenta de caja de ahorro.
            # En los cajeros todos los clientes pueden retirar pesos únicamente, Ya que por caja pueden retirar ambas monedas
            if len(self.cajasAhorro) > 0:
                  cuentaRetiroCajero = self.encontrarCaja(nroCuentaCajero)
            else:
                  print("Error: No se han dado de alta cajas de ahorro en pesos")

            if montoCajero <= cuentaRetiroCajero.saldo and montoCajero <= self.limiteCajero:
                  cuentaRetiroCajero.saldo -= montoCajero
                  self.limiteCajero -= montoCajero
                  print("Retiro por cajero exitoso, monto retirado: "+str(montoCajero)+"\n"+
                              "Saldo disponible: "+str(cuentaRetiroCajero.saldo)+"\n"+
                              "Limite de retiro por cajero disponible: "+str(self.limiteCajero))
                  self.transacciones.append(Transaccion("aprobada","Retiro_Cajero_Automatico",len(self.transacciones)+1,cuentaRetiroCajero.tipo ,montoCajero,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

            elif montoCajero <= self.limiteCajero and montoCajero > cuentaRetiroCajero.saldo:
                        print("Error: Saldo insuficiente")
                        self.transacciones.append(Transaccion("rechazada","Retiro_Cajero_Automatico",len(self.transacciones)+1,cuentaRetiroCajero.tipo ,montoCajero,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

            else: 
                  print("Error: Límite diario de retiro de cajero alcanzado, regrese mañana")
                  self.transacciones.append(Transaccion("rechazada","Retiro_Cajero_Automatico",len(self.transacciones)+1,cuentaRetiroCajero.tipo ,montoCajero,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))



      def compraDolar(self,cantidadDolares,cuentaPesos,cuentaDolares):
            cajaPesos = self.encontrarCajaEnPesos("pesos") #Verificamos que haya una caja de ahorro en pesos
            cajaDolares = self.encontrarCajaEnPesos("dolares") # y una en dolares ya que ambas son necesarias para la operacion

            cajaParaComprar = self.encontrarCaja(cuentaPesos) # Ubicamos la cuenta en pesos para comprar usd
            cajaParaDepositar = self.encontrarCaja(cuentaDolares) # Ubicamos la cuenta en dolares para depositar usd

            if cajaPesos != None and cajaDolares != None:
                  montoPesos = Cliente.calcularMontoTotal(350,cantidadDolares)
                  if montoPesos <= cajaParaComprar.saldo:
                        cajaParaComprar.saldo -= montoPesos #Restamos la cantidad de pesos
                        cajaParaDepositar.saldo += cantidadDolares #Acreditamos los dolares en la cuenta
                        print("Operación realizada: "+str(cantidadDolares)+" dólares comprados por "+str(montoPesos)+" pesos")
                        self.transacciones.append( Transaccion("aprobada","Compra_Dolar",len(self.transacciones)+1,cajaParaComprar.tipo ,montoPesos,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

                  else:
                        print("Saldo insuficiente")
                        self.transacciones.append( Transaccion("rechazada","Compra_Dolar",len(self.transacciones)+1,cajaParaComprar.tipo ,montoPesos,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

            else:
                  print("Error: Debe poseer caja de ahorro en pesos y dólares para realizar esta transacción")

      def ventaDolar(self,cantidadDolares,cuentaPesos,cuentaDolares): #Esta función hace prácticamente lo mismo que la anterior, 
            # Excepto que funciona a la inversa a la hora de restar y asignar los montos de los pesos y dolares
            cajaPesos = self.encontrarCajaEnPesos("pesos")
            cajaDolares = self.encontrarCajaEnPesos("dolares")

            cajaParaComprar = self.encontrarCaja(cuentaDolares)
            cajaParaDepositar = self.encontrarCaja(cuentaPesos)

            if cajaPesos != None and cajaDolares != None:
                  montoPesos = cantidadDolares * 350
                  if cantidadDolares <= cajaParaComprar.saldo:
                        cajaParaComprar.saldo -= cantidadDolares
                        cajaParaDepositar.saldo += montoPesos
                        print("Operación realizada: "+str(cantidadDolares)+" dolares vendidos por "+str(montoPesos)+" pesos")
                        self.transacciones.append( Transaccion("aprobada","Venta_Dolar",len(self.transacciones)+1,cajaParaComprar.tipo ,cantidadDolares,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                  else: 
                        print("Saldo insuficiente")
                        self.transacciones.append( Transaccion("rechazada","Venta_Dolar",len(self.transacciones)+1,cajaParaComprar.tipo ,cantidadDolares,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

      def mostrarTransacciones(self): #Muestra todas las transacciones realizadas por consola
            for i in range(len(self.transacciones)):
                  print(str(self.transacciones[i])+"\n")

      def exportarResumenTransacciones(self): #Crea un archivo json con toda la información del cliente y sus transacciones
         formato_json = self.infoJson()
         with open("Resumen_" + str(self.dni) + ".json", "w") as nuevo_file:
           nuevo_file.write(formato_json)    


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