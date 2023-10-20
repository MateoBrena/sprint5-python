class Cuenta:
      # generales, consulat saldo, etc, genérico de cuentas
      def __init__(self,tipo,saldo):
            self.tipo = tipo
            self.saldo = saldo

      def __str__(self):
            return "Cuenta "+self.tipo+". Saldo: "+str(self.saldo)