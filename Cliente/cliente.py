class Cliente:
     
     def __init__(self,nombre,apellido,dni,nro_cliente):
           self.nombre = nombre
           self.apellido = apellido
           self.dni = dni
           self.nro_cliente = nro_cliente


     def calcularMontoTotal(self,precioDolar,cantidad):
           impuestoPais = 0.3
           impuestoGanancias = 0.35

           montoOperacion = cantidad * precioDolar
           pais = montoOperacion * impuestoPais
           ganancias = montoOperacion * impuestoGanancias

           total = montoOperacion + pais + ganancias

           return total
           
     

     # métodos_de_cliente:
    #def obtener_tarjetas_disponibles():
    #def obtener_cuentas_disponibles():
    #def realizar_transferencia():
    #def obtener_limite_retiro_diario():

    #obtener saldo, cuestiones generales, que sean común en todos los tipos de cliente.


#class Transaccion:
 #    "Transacciones"