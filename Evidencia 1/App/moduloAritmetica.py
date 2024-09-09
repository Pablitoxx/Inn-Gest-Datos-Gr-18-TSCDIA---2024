def menuAritmetica():
    while True:
        print("Indique la operación que desea realizar \n\
            1- sumar dos números\n\
            2- restar dos números\n\
            3- dividir dos números\n\
            4- multiplicar dos números\n\
            5- sumar n cantidad de números\n\
            6- promediar n cantidad de números\n\
            7- salir")
        opcion= input("Escribe la opcion:  ")
        
        match opcion:
            case "1":
                num1,num2 =pedirDosNum()
                resultado=suma2Num(num1,num2)
                print("-" * 40)
                print(f"El resultado de sumar {num1} y {num2} es: {round(resultado,2)}")
                print("-" * 40)
            case "2":
                num1,num2 =pedirDosNum()
                resultado=resta2Num(num1,num2)
                print("-" * 40)
                print(f"El resultado de restar {num1} y {num2} es: {round(resultado,2)}")
                print("-" * 40)
            case "3":
                num1,num2 =pedirDosNum()
                resultado=div2Num(num1,num2)
                if resultado is not None: 
                    print("-" * 40) 
                    print(f"El resultado de dividir {num1} y {num2} es: {round(resultado, 2)}")
                else:
                    print("-" * 40) 
                    print("No se realizó la división debido a un divisor cero") 
                print("-" * 40)
                
                
            case "4":
                num1,num2 =pedirDosNum()
                resultado=multi2Num(num1,num2)
                print("-" * 40)
                print(f"El resultado de multiplicar {num1} y {num2} es: {round(resultado,2)}")
                print("-" * 40)
            case "5":
                cant,suma =pedirNNum()
                print("-" * 40)
                print(f"La suma de los {cant} números ingresados es: {round(suma,2)}")
                print("-" * 40)
            case "6":
                cant,suma=pedirNNum()
                resultado=promedioNNum(cant,suma)
                print("-" * 40)
                print(f"El resultado del promedio es: {round(resultado,2)}")
                print("-" * 40)
            case "7":
                print("Gracias por utilizar la Aritmetica")
                print("-" * 40)
                break
            case _:
                print("Por favor ingrese una opción valida")
                print("-" * 40)



def pedirDosNum():
    while True:
        try:
            num1= float(input("Por favor ingresa el primer número: "))
            num2= float(input("Por favor ingresa el segundo número: "))
            break
        except ValueError:
            print("Por favor ingrese solo números")     
    return num1,num2

def suma2Num(num1,num2):
    return num1 + num2

def resta2Num(num1,num2):
    return num1 - num2

def div2Num(num1,num2):
    if num2 == 0:
        return None
    return num1 / num2

def multi2Num(num1,num2):
    return num1 * num2

def pedirNNum():
    contN= 0
    suma= 0
    cantN= int(input("Cuántos números quiere usar? : "))
    while contN < cantN:
        try:
            num= float(input("Ingrese el número: "))
            suma= suma + num
            contN += 1

        except ValueError:
            print("Por favor ingrese solo Números")
    return cantN, suma


def promedioNNum(cantN,suma):
    return suma / cantN
    