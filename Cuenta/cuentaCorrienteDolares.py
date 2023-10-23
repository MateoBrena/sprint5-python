from Cuenta.cuenta import Cuenta

class CuentaCorrienteDolares(Cuenta):
    def __init__(self,tipo,saldo,moneda):
            super().__init__(tipo,saldo,moneda)
    
    def __str__(self):
          return "Cuenta "+self.tipo+". Saldo: "+str(self.saldo)+ " "+self.moneda