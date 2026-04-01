def crear_producto(id,n,p,q):
    product = {
        "id":id,
        "name":n,
        "price":p,
        "quantity":q
    }
    return product

def mostrar_inventario(producto):
    if not producto:
        print(f" El inventario está vacío.")
    else:
        for i in producto:
            print (i)    
        
    
