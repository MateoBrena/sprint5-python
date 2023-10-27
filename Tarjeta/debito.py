class Debito():
     
     def __init__(self,marca,id):
          self.tipo = "Debito"
          self.marca = marca
          self.id = id

     def __str__(self):
          return "Tarjeta de "+self.tipo+ " de marca "+self.marca+". Número de id:"+str(self.id)