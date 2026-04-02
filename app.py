# app.py
from servicio.servicios import *
from source.archivos import guardar_csv, cargar_csv

def obtener_dato_numerico(prompt, es_entero=False):
    """Solicita y valida una entrada numérica positiva."""
    while True:
        try:
            valor = input(prompt)
            numero = int(valor) if es_entero else float(valor)
            if numero >= 0:
                return numero
            print("[!] Error: El valor debe ser mayor o igual a cero.")
        except ValueError:
            print(f"[!] Error: Ingrese un número {'entero' if es_entero else 'válido'}.")

def ejecutar_accion(opcion, inventario):
    """Maneja la lógica de cada opción del menú."""
    
    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = obtener_dato_numerico("Precio: ")
        cantidad = obtener_dato_numerico("Cantidad: ", True)
        agregar_producto(inventario, nombre, precio, cantidad)
        print("-> Producto registrado con éxito.")

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Buscar nombre: ")
        encontrado = buscar_producto(inventario, nombre)
        print(f"Resultado: {encontrado}" if encontrado else "[!] No existe en el sistema.")

    elif opcion == "4":
        nombre = input("Nombre del producto a modificar: ")
        precio = obtener_dato_numerico("Nuevo precio (0 para ignorar): ")
        cantidad = obtener_dato_numerico("Nueva cantidad (0 para ignorar): ", True)
        if actualizar_producto(inventario, nombre, precio or None, cantidad or None):
            print("-> Actualización completada.")
        else:
            print("[!] Producto no localizado.")

    elif opcion == "5":
        nombre = input("Nombre a borrar: ")
        print("-> Borrado" if eliminar_producto(inventario, nombre) else "[!] No se encontró.")

    elif opcion == "6":
        resumen = calcular_estadisticas(inventario)
        if resumen:
            print("\n--- REPORTE DE INVENTARIO ---")
            print(f"• Total Unidades: {resumen['unidades']}")
            print(f"• Valor Monetario: ${resumen['valor']:,.2f}")
            print(f"• Producto Líder (Precio): {resumen['caro']['nombre']} (${resumen['caro']['precio']})")
            print(f"• Mayor Existencia: {resumen['stock']['nombre']} ({resumen['stock']['cantidad']} und)")
        else:
            print("[!] Inventario vacío.")

    elif opcion == "7":
        guardar_csv(inventario)
        print("-> Archivo guardado.")

    elif opcion == "8":
        importados, fallos = cargar_csv()
        if importados is not None:
            print(f"Leídos: {len(importados)} | Errores: {fallos}")
            confirmar = input("¿Desea limpiar el inventario actual antes de cargar? (S/N): ").lower()
            
            if confirmar == 's':
                inventario.clear()
                inventario.extend(importados)
            else:
                # Mezcla inteligente: si existe, suma stock; si no, agrega nuevo
                for item in importados:
                    existente = buscar_producto(inventario, item['nombre'])
                    if existente:
                        existente['cantidad'] += item['cantidad']
                        existente['precio'] = item['precio']
                    else:
                        inventario.append(item)
            print("-> Datos sincronizados.")

def menu_principal():
    inventario_actual = []
    
    while True:
        print(f"""
        {"="*35}
          GESTIÓN DE STOCK v2.0
        {"="*35}
        1. Registrar   2. Listar      3. Buscar
        4. Editar      5. Borrar      6. Reporte
        7. Guardar     8. Cargar      9. Salir
        """)
        
        seleccion = input("Seleccione una operación: ")

        if seleccion == "9":
            print("Cerrando sesión. ¡Hasta pronto!")
            break
        
        if seleccion in "12345678":
            ejecutar_accion(seleccion, inventario_actual)
        else:
            print("[!] Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
