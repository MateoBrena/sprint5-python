class Credito():
     
     def __init__(self,marca,limite,limiteCuotas):
          self.marca = marca
          self.limite = limite
          self.limiteCuotas = limiteCuotas
          self.tipo = "Crédito"

     def __str__(self):
          return "Tarjeta de "+self.tipo+ " de marca "+self.marca+". Con límite de "+str(self.limite)+" y límite de cuotas de "+str(self.limiteCuotas)