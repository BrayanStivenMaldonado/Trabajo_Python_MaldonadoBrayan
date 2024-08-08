from os import system
import json
from datetime import date

#FUNCION PARA ABRIR LOS DATOS DEL JSON CON LA INFORMACIÓN DE LOS PRODUCTOS
def abrirArchivo():
    miJSON=[]
    with open('Datos.json','r',encoding='utf-8') as openfile:
        miJSON = json.load(openfile)  
    return miJSON

#FUNCION PARA GUARDAR DATOS DEL JSON QUE CONTIENE EL HISTORIAL DE VENTAS
def abrirVentas():
    Ventas=[]
    with open('Ventas.json','r',encoding='utf-8') as openfile:
        Ventas = json.load(openfile)  
    return Ventas
def guardarVentas(miVenta): 
    with open("Ventas.json","w",encoding='utf-8') as outfile:
        json.dump(miVenta,outfile)      

#Inicio del programa     

BoolGeneral = True

while BoolGeneral == True:

    RegistroVentas = abrirVentas()

    boolTryCatch = True
    while boolTryCatch == True:
        try: 
            Eleccion = int(input("""---Bienvenido a PanCamp---
1. Ventas y Compras
2. Generación de informes
3. Cerrar programa
                                 
¿A qué apartado desea acceder?: 
"""))  
            system("cls")  
            boolTryCatch=False
        except ValueError:
            input("Debes ingresar una opción válida, presiona ENTER para volver a intentarlo")
            system("cls")

#                                             INICIO DE LOS MODULOS

    if Eleccion == 1:
        print("---VENTAS Y COMPRAS---")  
        boolVentas = True
        while boolVentas == True:
            GeneralData = abrirArchivo()
            contador = 1
            for i in GeneralData:
                print(contador,i["Tipo"])
                contador += 1
            print("5 Salir")
            EleVentas = int(input("\nEscoja el grupo de productos que desea ver: "))
            system("cls")
            if EleVentas == 5: 
                boolVentas = False
                break
            GeneralData = abrirArchivo()
            print("Nombre del producto                      Precio")
            print("")
            contador = 1
            for i in GeneralData[EleVentas-1]["Contenido"]:
                print(contador,i["Nombre"],"|  $",i["Precio"])
                contador += 1
            ProductoComprar = int(input("\n Ingrese el id del producto que desea comprar: "))
            CantidadComprar = int(input("Cuántas unidades desea llevar?: "))

            NombreProdCompra = GeneralData[EleVentas-1]["Contenido"][ProductoComprar-1]["Nombre"]
            PrecioUnidadCompra =  GeneralData[EleVentas-1]["Contenido"][ProductoComprar-1]["Precio"]
            Fecha = date.today()
            FechaCompra = Fecha.isoformat()

            RegistroVentas = abrirVentas()
            
            RegistroVentas["HistorialVentas"].append(
                {
                    "Fecha" : FechaCompra,
                    "InfoCliente" : {
                        "NombreCliente" : str(input("Nombre del cliente: ")),
                        "DireccionCliente" : str(input("Dirección del cliente: "))
                    },
                    "InfoEmpleado" : {
                        "NombreEmpleado" : str(input("Nombre del empleado que realizó la venta: ")),
                        "CargoEmpleado" : str(input("Cargo del empleado: "))
                    },
                    "InfoProducto" : {
                        "Nombre" : NombreProdCompra,
                        "Cantidad" : CantidadComprar,
                        "PrecioUnidad" : PrecioUnidadCompra,
                        "PrecioTotal" : PrecioUnidadCompra*CantidadComprar
                    }
                }
            )
            guardarVentas(RegistroVentas)
            
            system("cls")
            input("Venta realizada con éxito, Presione ENTER para continuar\n")
        

    elif Eleccion == 2:
        input("GENERACION DE INFORMES")
        system("cls")

    elif Eleccion == 3:
        input("Gracias por preferir PanCamp, nos vemos luego :D")
        BoolGeneral = False
        system("cls")

    else:
        input("Debes ingresar una opción válida, Presiona ENTER para volver a intentarlo")
        system("cls")