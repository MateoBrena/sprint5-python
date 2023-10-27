from Cuenta.cuenta import Cuenta

class CuentaInversiones(Cuenta):
    def __init__(self,tipo,saldo,moneda,nro_cuenta):
            super().__init__(tipo,saldo,moneda,nro_cuenta)
    
    def __str__(self):
          return "Cuenta: "+self.tipo+". Saldo: "+str(self.saldo)+ " "+self.moneda+" con id : "+str(self.nro_cuenta)