class Cuenta:

      def __init__(self,tipo,saldo,moneda,nro_cuenta):
            self.tipo = tipo
            self.saldo = saldo
            self.moneda = moneda
            self.nro_cuenta = nro_cuenta

      def __str__(self):
            return "Cuenta "+self.tipo+". Saldo: "+str(self.saldo)+" "+self.moneda