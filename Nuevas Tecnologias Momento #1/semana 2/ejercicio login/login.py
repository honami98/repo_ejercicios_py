print("*---------- SIGN UP ----------*")
print("------------------------------")

user_name = input("Ingrese su nombre: ")
user_email = input("Ingrese su email: ")
user_phone = input("Ingrese su número de teléfono: ")
user_password = input("Ingrese su contraseña: ")


print("*---------- LOGIN ----------*")
print("------------------------------")

captcha = 1

user_validation = input("Ingrese su email o número de telefono: ")
password_validation = input("Ingrese su contraseña: ")
captcha_validation = input("CAPTCHA - Resuelva la siguiente ecuación: x+8-7, x= ?")
int_captcha = int(captcha_validation)

if user_email == user_validation or user_phone == user_validation:
    if password_validation == user_password:
      if int_captcha == captcha:
        print("Hola, " , user_name , "¿cómo estás?")
else:
  print("Usurario o contraseña inválidos")