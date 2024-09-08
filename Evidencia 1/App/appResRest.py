import moduloRecuperacion
usuarios = {}
# login

while True:
   print ("Bienvenido")
   ingreso_usuario = input("¿Esta usted registrado?  si/no: ")
   if ingreso_usuario == "no":
      print("-" * 40)
      print ("Por favor ingrese sus datos de Registro")
      print("-" * 40)
      apellido = input("Apellido/s: ")
      nombre = input("Nombre/s: ")
      while True:
         dni = input("DNI: ")
         if dni in usuarios:
            print ("DNI ya registrado por favor ingrese otro")
         else:
            break
      email = input("email: ")
      telefono = input("Número tel: ")
      fechaNac = input("Fecha Nacimiento: ")

           # Validación del nombre de usuario
      while True:
         nomUsuario = input("Nombre de Usuario:  ")
            
            # Verificar longitud del nombre de usuario
         if len(nomUsuario) < 6 or len(nomUsuario) > 12:
            print("El nombre de usuario debe tener entre 6 y 12 caracteres")
            continue
            
            # Verificar el nombre de usuario
         usuario_existe = False
         for persona in usuarios.values():
            if persona["nombre usuario"] == nomUsuario:
               usuario_existe = True
               break
            
         if usuario_existe:
               print("Nombre de usuario ya registrado, por favor ingrese otro.")
         else:
            break

      while True:   
         clave = input("Contraseña: \n")
         if len(clave) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
            continue

         # Inicializar las variables de cada tipo de caracter
         tiene_min = False
         tiene_mayus = False
         tiene_num = False
         tiene_esp = False

         for caracter in clave:
            if caracter.islower():  # Verifica si es minúscula
               tiene_min = True
            elif caracter.isupper():  # Verifica si es mayúscula
               tiene_mayus = True
            elif caracter.isdigit():  # Verifica si es un número
               tiene_num = True
            elif not caracter.isalnum():  # Verifica si es un carácter especial (ni letra ni número)
               tiene_esp = True

         cumple_cond = sum([tiene_min,tiene_mayus,tiene_num,tiene_esp])
         if cumple_cond < 2:
            print("La contraseña debe tener al menos dos de las siguientes condiciones:\n minúscula, mayúscula, número o carácter especial")
         else:
            print("Contraseña válida")
            break

      persona = {
         "apellido": apellido,
         "nombre": nombre,
         "dni": dni,
         "email": email,
         "telefono": telefono,
         "fecha nac": fechaNac,
         "nombre usuario": nomUsuario,
         "clave": clave
      }

      usuarios[dni] = persona
      print("Registro Exitoso")

   elif ingreso_usuario == "si":
      contraseña_olvidada = input("Olvido su contraseña? si/no   ")
      if contraseña_olvidada == "si":
         moduloRecuperacion.recuperarPass()
         continue
      else:
         nomUsuario = input("Ingrese el nombre de usuario: ")
         intentos = 4  # Inicializar intentos antes de buscar el usuario

            # Verificar si el nombre de usuario existe
         usuario_encontrado = False  # Variable para verificar si se encuentra el usuario
         for persona in usuarios.values():
            if persona["nombre usuario"] == nomUsuario:
               usuario_encontrado = True  # Usuario encontrado
               # Intentar hasta 4 veces
               while intentos > 0:
                  clave = input("Ingrese la clave de usuario: ")
                  if persona["clave"] == clave:
                     print("¡Bienvenido, has ingresado correctamente!")
                     break  # Salir del bucle de contraseña si es correcta
                  else:
                     intentos -= 1
                     print(f"Contraseña incorrecta. Te quedan {intentos} intentos.\n")

                    # Verificar si los intentos se agotaron
               if intentos == 0:
                  print("Has superado el número de intentos permitidos. Acceso denegado.\n")
                    
                    # Salir del bucle de búsqueda de usuario ya que se procesó el login
               break

         if not usuario_encontrado:
            print("Nombre de usuario incorrecto.\n")
            continue  # Volver a preguntar si está registrado o no

            # Mostrar el menú del sistema solo si la autenticación fue ex
      if intentos > 0:
         # Mostrar el menú del sistema
         while True:  
            print("-" * 40)                                     
            print(format("\033[3;35m"+"Bienvenido a Bohemia" + "\033[0;m",'=^50'))
            print("-" * 40)  
            print("Seleccione la opción que desee: \n")
            print("1- Reservar mesa")
            print("2- Consultar reserva")
            print("3- Mostrar reservas")
            print("4- Modificar reserva")
            print("5- Cancelar reserva")
            print("6- Modificar datos Usuario")
            print("7- Eliminar Usuario")
            print("8- Salir")
            print("-" * 40)
            menu_opcion = input("Escribe la opción que desea escoger: ")
            print("-" * 40)
            if menu_opcion == "8":
                  print("Gracias por utilizar el sistema.\n")
                  print("-" * 40)
                  break  # Salir del menú y del programa
            break  # Salir del bucle principal después de mostrar el menú

   else:
      print("Entrada no válida. Por favor, ingrese 'si' o 'no'.\n")
      continue  # Vuelve al inicio del bucle