# servicios.py

def agregar_producto(inventario, nombre, precio, cantidad):
    """Inserta un diccionario con los datos del producto en la lista."""
    nuevo = {
        "nombre": nombre.strip().title(), # Limpia espacios y capitaliza
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(nuevo)


def mostrar_inventario(inventario):
    """Imprime una tabla formateada de los productos disponibles."""
    if not inventario:
        return print("\n[!] No hay existencias registradas.")

    print(f"\n{'ID':<4} | {'PRODUCTO':<15} | {'PRECIO':<10} | {'STOCK':<8}")
    print("-" * 45)
    
    for indice, p in enumerate(inventario, start=1):
        print(f"{indice:<4} | {p['nombre']:<15} | ${p['precio']:>8.2f} | {p['cantidad']:>5} und")


def buscar_producto(inventario, nombre):
    """Localiza un producto. Retorna el diccionario o None si no existe."""
    # Usamos next con un generador para una búsqueda más eficiente
    return next((p for p in inventario if p['nombre'].lower() == nombre.lower()), None)


def actualizar_producto(inventario, nombre, n_precio=None, n_cantidad=None):
    """Modifica valores específicos de un producto si este se encuentra."""
    item = buscar_producto(inventario, nombre)
    if item:
        # Solo actualiza si el valor no es None ni cero (según lógica de app.py)
        if n_precio: item['precio'] = n_precio
        if n_cantidad: item['cantidad'] = n_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    """Remueve el producto del inventario basándose en su nombre."""
    inicial = len(inventario)
    # Reconstruimos la lista excluyendo el nombre (enfoque funcional)
    inventario[:] = [p for p in inventario if p['nombre'].lower() != nombre.lower()]
    return len(inventario) < inicial


def calcular_estadisticas(inventario):
    """Genera un resumen técnico del inventario actual."""
    if not inventario:
        return None

    # Función interna para calcular valor por producto
    obtener_subtotal = lambda p: p['precio'] * p['cantidad']

    return {
        "unidades": sum(p['cantidad'] for p in inventario),
        "valor": sum(map(obtener_subtotal, inventario)),
        "caro": max(inventario, key=lambda x: x['precio']),
        "stock": max(inventario, key=lambda x: x['cantidad'])
    }
