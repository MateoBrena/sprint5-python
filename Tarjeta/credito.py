class Credito():
     
     def __init__(self,marca,limite,limiteCuotas):
          self.marca = marca
          self.limite = limite
          self.limiteCuotas = limiteCuotas
          self.tipo = "Crédito"
          self.extensiones = 0

     def __str__(self):
          return ("Tarjeta de "+self.tipo+ " de marca "+self.marca+"\n"+
                  "Con límite de "+str(self.limite)+" en un pago y "+str(self.limiteCuotas)+" en cuotas"+"\n"+
                  "Cantidad de extensiones: "+str(self.extensiones))