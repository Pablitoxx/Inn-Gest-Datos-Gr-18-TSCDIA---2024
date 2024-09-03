
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
         dni = input("DNI: ")
         email = input("email: ")
         telefono = input("Número tel: ")
         fechaNac = input("Fecha Nacimiento: ")
         nomUsuario = input("Nombre Usurio: ")
         clave = input("Contraseña: ")

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
       nomUsuario = input("Ingrese el nombre de usuario: ")
       clave = input("Ingrese la clave de usuario: ")
       if nomUsuario== usuarios and clave  == usuarios:
           break

 # Menu de opciones para seleccionar
    while True:  
        print("-" * 40)                                     
        print(format("\033[3;35m"+"Bienvenido a Bohemia" + "\033[0;m",'=^50'))
        print("-" * 40)  
        print("Seleccione la opcion que desee: \n")
        print("1- Reservar mesa")
        print("2- Consultar reserva")
        print("3- Mostrar reservas")
        print("4- Modificar reserva")
        print("5- Cancelar reserva")
        print("6- Modificar datos Usuario")
        print("7- Eliminar Usuario")
        print("8- Salir")
        print("-" * 40)
        menu_opcion= (input("Escribe la opción que desea escoger: "))
        print("-" * 40)