class Cliente:
     
     def __init__(self,nombre,apellido,dni,nro_cliente):
           self.nombre = nombre
           self.apellido = apellido
           self.dni = dni
           self.nro_cliente = nro_cliente


     def calcularMontoTotal(precioDolar,cantidad): # Ej (350,200)
           impuestoPais = 0.3
           impuestoGanancias = 0.35

           montoOperacion = cantidad * precioDolar
           pais = montoOperacion * impuestoPais
           ganancias = montoOperacion * impuestoGanancias

           total = montoOperacion + pais + ganancias

           return total
     
     def descontarComision(monto, porcentajeComision): # Ej (1000,10)
           comision = (porcentajeComision / 100) * monto
           montoConDescuento = monto- comision
           return montoConDescuento
     
     def CalcularPlazoFijo(monto,interes): # Ej (100,0.50)
           montoConIntereses = monto * (interes + 1)
           return montoConIntereses
           
           