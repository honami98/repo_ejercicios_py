print("*---------- PROGRAMA ----------*")
print("--------------------------------")

print("\n Elige una opción:")
opc = input(" 1 - Empezar\n 0 - Cerrar\n")
int_opc = int(opc)

while (int_opc != 0 and int_opc == 1):

  print("*---------- MENU ----------*")
  print("----------------------------")

  print("\n Elige una opción:")
  menuOpc = input(" 1 - Crear usuario\n 2 - Login\n 0 - Salir\n")
  int_menuOpc = int(menuOpc)

  if int_menuOpc == 1:
 
    print("*---------- INICIAR SESION ----------*")
    print("---------------------------------------")

    user_name = input("Ingresa nombre: ")
    user_email = input("Ingresa email: ")
    user_phone = input("Ingresa número de teléfono: ")
    user_password = input("Ingresa contraseña: ")

  elif int_menuOpc == 2:

    print("*---------- LOGIN ----------*")
    print("------------------------------")

    captcha = 1

    user_validation = input("Ingrese su email o su número de telefono: ")
    password_validation = input("Ingrese su contraseña: ")
    captcha_validation = input("CAPTCHA - Resuelva la siguiente ecuación: x+8-7 ,x= ?")
    int_captcha = int(captcha_validation)

    if user_email == user_validation or user_phone == user_validation:
        if password_validation == user_password:
          if int_captcha == captcha:
            login = True
            print("Bienvenido" , user_name)

            while (login == True):
                print("*--------- USER MENU ---------*")
                print("-----------------------------")

                print("\n Choice an option:")
                menuOpc2 = input(" 1 - Juego\n 2 - Tarjeta de credito\n 0 - Regresar\n")
                int_menuOpc2 = int(menuOpc2)

                if int_menuOpc2 == 1:

                  print("*---------- JUEGO ----------*")
                  print("--------------------------------")

                  import random
                  vidas = 7
                  puntos = 0

                  while(vidas != 0):
                      num = random.randint(0, 9)
                      if num == 0:
                          vidas -=1
                          print ("vidas: ", vidas)
                      else:
                          puntos +=2
                          print ("puntos: ", puntos)

                elif int_menuOpc2 == 2:
                  print("*---------- COMPRA ----------*")
                  print("------------------------------")

                  compra = input("Ingrese el valor de su compra: ")
                  int_compra = int(compra)
                  cuotas = input("Ingrese el número de Cuotas: ")
                  int_cuotas = int(cuotas)
                  pagar = input("Desea inicar los pagos, ingrese 1 para SI / 2 para NO ")
                  int_pagar = int(pagar)

                  montoCuota = int_compra / int_cuotas

                  print("*---------- PAGO ----------*")
                  print("------------------------------")

                  while (pagar != 2):
                      if int_cuotas == 0:
                        print ("Su compra fue pagada completamente!")
                        break
                      else:
                        int_cuotas -=1
                        int_compra -= montoCuota
                        print ("cuotas restante: ", int_cuotas)
                        print ("monto restante: ", int_compra)

                  print ("Gracias por su compra!")

                elif int_menuOpc2 == 0:
                  break


    else:
      print("el usuario o la contraseña son inválidos")





print("Gracias!")