# PanCamp

## Descripción
Sistema de gestion de una panaderia que servirá para manejar todas las operaciones relacionadas con la administración de productos, proveedores, empleados, clientes, así como la generación de informes relevantes.

Dentro de este programa el acceso a los modulos está organizado por medio de menús en los cuales, dependiendo de la opción que escoja el usuario se le dará el acceso a los diferentes apartados.

## Tecnologias usadas

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![json](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)

## Características
|Archivo|Función|
|--|--|
|**Compras.json**|Archivo en el que se van a almacenar los datos del historial de compras|
|**Datos.json**|Archivo en el cual se encuentran los productos disponibles, con su respectivo nombre y precio|
|**PanCamp.py**|Archivo en que está el código del programa en sí|
|**Ventas.json**|Archivo en el que se van a almacenar los datos del historial de ventas de la panaderia|

## Funcionalidades 

El programa está dividido en diferentes modulos, los cuales contienen diferentes funcionalidades,las cuales son:

**Ventas:** El sistema de gestión permite registrar cada transacción de venta con la siguiente información: 
- Fecha de la venta.
- Información del cliente (nombre, dirección).
- Información del empleado que realizó la venta (nombre, cargo).
- Productos vendidos (nombre, cantidad, precio).

**Compras:** El sistema permite regitrar cada compra realizada a los proveedores con la siguiente información:
- Fecha de la compra.
- Información del proveedor (nombre, contacto).
- Productos comprados (nombre, cantidad, precio de compra).

**Generación de informes**
- ***Informes de ventas:***
Listado de todas las ventas realizadas en un período de tiempo específico, incluyendo detalles de los productos vendidos y el total de ingresos.

- ***Informes de stock***:
Listado de todos los productos con su cantidad en stock para gestionar de manera proactiva los inventarios.

## Instrucciones de uso

1. Debes clonar este repositorio en tu maquina local
```bash
git clone https://github.com/BrayanStivenMaldonado/Trabajo_Python_MaldonadoBrayan.git
```

2. Dentro de VSC vas a ejecutar el archivo .py en la terminal o con alguna extension, por ejemplo **CodeRunner**

## Desarrollado

Este programa fue desarrollado por ***Brayan Maldonado***, estudiante de Campuslands.
