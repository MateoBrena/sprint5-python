class Transaccion:
     
     def __init__(self,estado,tipo,numero,cuenta,monto,fecha):
           self.estado = estado
           self.tipo = tipo
           self.numero = numero
           self.cuenta = cuenta
           self.monto = monto
           self.fecha = fecha

     def __str__(self):
           return ("Estado: "+self.estado+"\n"+
                   "Número: "+str(self.numero)+"\n"+
                   "Cuenta: "+str(self.cuenta)+"\n"+
                   "Tipo: "+self.tipo+"\n"+
                   "Monto: "+str(self.monto)+"\n"+
                   "Fecha: "+str(self.fecha))
