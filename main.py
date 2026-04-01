# Ruta principal donde usamos todas las funciones del programa
from ui.menus import *
from source.funciones import *

# Variable inicializadora
start = 1

# Este diccionario/lista de productos
products = []

while start != 0:  # Controla el flujo del programa con una comparación
    
    mostrar_menu()

    option = input("Seleccione una opción: ")   

    if option == "1":
        product_id = int(input("Ingrese el ID del producto: "))
        name = str(input("Ingrese el nombre del producto: "))
        quantity = int(input("Ingrese la cantidad de productos: "))
        price = int(input("Ingrese el precio del producto: "))
        
        product = crear_producto(product_id, name, quantity, price)
        products.append(product)
        print(products)

    elif option == "2":
        
        mostrar_inventario(products)

        


    elif option == "0":
        print("Adiós, usuario")
        start = 0
    else: 
        print("Opción no válida")
    
 