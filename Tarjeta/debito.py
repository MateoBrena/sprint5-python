class Debito():
     
     def __init__(self,marca):
          self.tipo = "Débito"
          self.marca = marca

     def __str__(self):
          return "Tarjeta de "+self.tipo+ " de marca "+self.marca