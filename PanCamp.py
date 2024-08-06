from os import system
import json

def abrirArchivo():
    miJSON=[]
    with open('Datos.json','r',encoding='utf-8') as openfile:
        miJSON = json.load(openfile)  
    return miJSON
  
def guardarArchivo(miData): 
    with open("Datos.json","w",encoding='utf-8') as outfile:
        json.dump(miData,outfile)

#Inicio del programa     

BoolGeneral = True

while BoolGeneral == True:

    boolTryCatch = True

    while boolTryCatch == True:
        try: 
            Eleccion = int(input("""---Bienvenido a PanCamp---
            ¿A qué apartado desea acceder?
            1. Ventas y Compras
            2. Generación de informes
            3. Cerrar programa
            """))  
            system("cls")  
            boolTryCatch=False
        except ValueError:
            input("Debes ingresar una opción válida, presiona ENTER para volver a intentarlo")
            system("cls")

#                                                                     INICIO DE LOS MODULOS

    if Eleccion == 1:
        print("---VENTAS Y COMPRAS---")  
        GeneralData = abrirArchivo()
        print("Nombre del producto            Precio")
        print("")
        for i in GeneralData[0]["Panaderia"]:
            print(i["Nombre"],"|  $",i["Precio"])
        

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