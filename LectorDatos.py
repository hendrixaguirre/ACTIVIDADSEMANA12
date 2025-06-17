#Se utiliza el try.. except
try:
    with open("productos.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea=linea.strip()
            datos=linea.split(";")
            if len(datos) == 3:
                nombre, precio, cantidad = datos
                print (f"Producto: {nombre}. Precio: C${precio}. Cantidad: {cantidad} unidades")
            else:
                print ("Línea con formato incorrecto:", linea)
except FileNotFoundError:
    print ("El archivo 'productos.csv' no se fue encontrado.")