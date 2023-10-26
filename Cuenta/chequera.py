from Cuenta.cuenta import Cuenta

class Chequera(Cuenta):
    def __init__(self,tipo,saldo,moneda):
            super().__init__(tipo,saldo,moneda)
    
    def __str__(self):
          return "Cuenta: "+self.tipo + ". Cheques disponibles: "+ str(self.saldo)