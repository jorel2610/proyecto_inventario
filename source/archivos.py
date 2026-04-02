
# archivos.py
import csv
import os

def guardar_csv(inventario, nombre_archivo="inventario.csv"):
    """Exporta la lista de productos a un archivo CSV."""
    if not inventario:
        return print("[!] Cancelado: El inventario está vacío.")

    try:
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
            # Definimos las columnas
            columnas = ["nombre", "precio", "cantidad"]
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            
            escritor.writeheader()
            escritor.writerows(inventario)
            
        print(f"[CSV] Datos exportados exitosamente a '{nombre_archivo}'.")
    except IOError as e:
        print(f"[!] Error de escritura: {e}")


def cargar_csv(nombre_archivo="inventario.csv"):
    """Lee el archivo CSV y reconstruye la lista de productos."""
    # Verificamos si el archivo existe antes de intentar abrirlo
    if not os.path.exists(nombre_archivo):
        print(f"[!] Error: No se encontró el archivo '{nombre_archivo}'.")
        return None, 0

    productos = []
    conteo_errores = 0

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            # Verificación rápida de estructura
            campos_requeridos = {"nombre", "precio", "cantidad"}
            if not campos_requeridos.issubset(set(lector.fieldnames or [])):
                print("[!] Error: El formato del CSV es incompatible.")
                return None, 0

            for fila in lector:
                try:
                    # Procesamiento y limpieza de datos en una sola estructura
                    p_nombre = fila['nombre'].strip()
                    p_precio = float(fila['precio'])
                    p_cantidad = int(fila['cantidad'])

                    if p_precio < 0 or p_cantidad < 0:
                        raise ValueError("Valores negativos")

                    productos.append({
                        "nombre": p_nombre,
                        "precio": p_precio,
                        "cantidad": p_cantidad
                    })
                except (ValueError, KeyError, TypeError):
                    conteo_errores += 1
                    
        return productos, conteo_errores

    except Exception as e:
        print(f"[!] Error inesperado durante la carga: {e}")
        return None, 0
