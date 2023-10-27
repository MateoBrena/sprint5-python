from Cliente.classic import Classic
from Cliente.gold import Gold
from Cliente.black import Black

cliente1 = Classic("Pedro","Gonzalez",12345678,1)
cliente2 = Gold("Juan","Gutierrez",12345679,2)
cliente3 = Black("Pedro","Arias",12345670,3)

"""
cliente1.getInfo()
print()
cliente1.altaCajaAhorroPesos()
cliente1.altaCajaAhorroDolares()
cliente1.altaCajaAhorroPesos() #No va a permitir crear más cajas de ahorro si el cliente no tiene ese beneficio, figurará transacción rechazada
print()
cliente1.getSaldoCajaAhorroPesos()
print()
cliente1.getSaldoCajaAhorroDolares()
print()
cliente1.recibirTransferencia(200000,"pesos")
print()
cliente1.retiroCajero(500)
print()
cliente1.recibirTransferencia(1000,"dolares")
print()
cliente1.altaTarjetaCredito("Visa") # Este tipo de cliente no tiene acceso a tarjetas de débito, también generará la transacción rechazada
cliente1.altaTarjetaDebito("Mastercard")
print()
cliente1.compraDolar(200)
print()
cliente1.getSaldoCajaAhorroPesos()
print()
cliente1.getSaldoCajaAhorroDolares()
print()
cliente1.exportarResumenTransacciones()
# cliente2.mostrarTransacciones()
"""


"""
cliente2.getInfo()
print()
cliente2.altaCajaAhorroPesos()
cliente2.altaCajaAhorroDolares()
cliente2.altaCajaAhorroDolares() #No va a permitir crear más cajas de ahorro si el cliente no tiene ese beneficio, figurará transacción rechazada
print()
cliente2.getSaldoCajaAhorroPesos()
print()
cliente2.getSaldoCajaAhorroDolares()
print()
cliente2.recibirTransferencia(200000,"pesos")
print()
cliente2.retiroCajero(5000)
print()
cliente2.recibirTransferencia(1000,"dolares")
print()
cliente2.altaCuentaInversiones()
cliente2.altaCuentaCorrientePesos()
cliente2.retiroPorCaja(100,"dolares")
cliente2.altaTarjetaCredito("Visa")
cliente2.altaTarjetaCredito("Mastercard")
cliente2.altaTarjetaCredito("Amex") #El cliente no posee acceso a tarjetas marca Amex, pero esto no generará una transacción rechazada
cliente2.altaTarjetaCredito("Mastercard")# El cliente recibirá la transacción rechazada por intentar dar de alta una tarjeta de 
#marca que ya posee, además de exederse de la cantidad permitida
cliente2.altaTarjetaDebito("Visa")
print()
cliente2.compraTarjetaCreditoCuotas("Visa",70000)
print()
cliente2.ventaDolar(200)
print()
cliente2.getSaldoCajaAhorroPesos()
print()
cliente2.getSaldoCajaAhorroDolares()
print()
cliente2.exportarResumenTransacciones()
# cliente2.mostrarTransacciones()
"""


"""
cliente3.getInfo()
print()
cliente3.altaCajaAhorroPesos()
cliente3.altaCajaAhorroDolares()
cliente3.altaCajaAhorroDolares() # Este cliente puede seguir creando cajas de ahorro hasta llegar al límite de 5
cliente3.getSaldoCajaAhorroPesos(301) #Este cliente debe especificar nro de cuenta para consultar 
# el saldo, de la caja de ahorro ya que posee más de una
print()
cliente3.getSaldoCajaAhorroDolares(302)
print()
cliente3.recibirTransferencia(200000,"pesos",301)
print()
cliente3.retiroPorCaja(150000,"dolares",301) #El id de la cuenta corresponde a una caja de ahorro en pesos, al colocar dolar 
# como la moneda, se producirá un error aunque no generará una tranascción rechazada. En cambio intentar retirar más del monto disponible 
# dará como resultado una transacción rechazada
print()
cliente3.recibirTransferencia(800,"dolares",302)
print()
cliente3.retiroPorCaja(100,"dolares",303) #Si bien este id hace referencia a una cuenta en dolares, la misma no tiene saldo 
# por lo que generará una transacción rechazada ya que los fondos son insuficientes
cliente3.altaTarjetaCredito("Visa")
cliente3.altaTarjetaCredito("Mastercard")
cliente3.altaTarjetaCredito("Amex")
cliente3.altaTarjetaCredito("Mastercard")# El cliente recibirá la transacción rechazada por intentar dar de alta una tarjeta de 
#marca que ya posee
cliente3.altaTarjetaCredito("Visa")
cliente3.altaTarjetaDebito("Visa")
cliente3.altaTarjetaDebito("Mastercard")
print()
cliente3.compraTarjetaCredito("Visa",400000)
print()
cliente3.ventaDolar(200,301,302)
print()
cliente3.altaCuentaCorrienteDolares()
print()
cliente3.altaCuentaCorrientePesos()
print()
print()
cliente3.altaChequera()
print()
cliente3.getSaldoCajaAhorroPesos(301)
print()
cliente3.getSaldoCajaAhorroDolares(302)
print()
cliente3.compraTarjetaCredito("Visa",250000) #El cliente superará el límite de la tarjeta, la transacción será rechazada
print()
cliente3.exportarResumenTransacciones()
#cliente3.mostrarTransacciones()

"""