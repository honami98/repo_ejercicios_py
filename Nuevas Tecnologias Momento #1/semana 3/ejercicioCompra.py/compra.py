print("********** COMPRA ************")
print("------------------------------")

compra = input("Ingresa el valor de su compra: ")
int_compra = int(compra)
cuotas = input("Ingrese el número de cuotas: ")
int_cuotas = int(cuotas)
pagar = input("¿Quiere inicar los pagos inmediatamente?, ingrese 1 para SI / 2 para NO ")
int_pagar = int(pagar)

montoCuota = int_compra / int_cuotas

print("*---------- PAGO ----------*")
print("------------------------------")

while (pagar != 2):
    if int_cuotas == 0:
      print ("Su comprfue pagada completamente!")
      break
    else:
      int_cuotas -=1
      int_compra -= montoCuota
      print ("cuotas restante: ", int_cuotas)
      print ("monto restante: ", int_compra)

print ("Gracias por su pago")