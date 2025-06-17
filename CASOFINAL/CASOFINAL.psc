Proceso CosméticosCastillo
	// Se definen las variables
	Definir inventario como cadena
	dimension inventario[100,3] // Matriz para almacenar el inventario 
	definir totalProductos Como Entero
	definir opcioon como caracter
	definir nombre como cadena 
	definir cantidad Como Entero
	definir precio Como Real
	
	totalProductos=0
	// Se establece el ciclo para que se repita continuamente
	Repetir 
		Escribir "---- Menú ----"
		Escribir "1. Agregar producto"
		Escribir "2. Ver inventario"
		Escribir "3. Salir"
		Escribir "Elija una opción (1/2/3): "
		Leer opcioon // Se lee la opción que elige el usuario
		
		Si opcioon="1" Entonces
			Escribir "Ingrese el nombre del producto:"
			Leer nombre
			Escribir "Ingrese la cantidad:"
			Leer cantidad
			Escribir "Ingrese el precio:"
			Leer precio 
			
			Inventario[totalProductos + 1,1]=nombre
			inventario[totalProductos + 1,2]=ConvertirATexto(cantidad) // Se convierte la cantidad a texto
			inventario[totalProductos + 1,3]=ConvertirATexto(precio) // Se convierte el precio a texto
			
			totalProductos=totalProductos+1 
			Escribir "Producto agregado con éxito!" 
		SiNo
			si opcioon="2" Entonces
				si totalProductos=0 Entonces
					Escribir "No hay productos en el inventario!"
				sino 
					Escribir "Inventario actual:"
					para i=1 Hasta totalProductos
						Escribir i, ".", inventario[i,1], " - cantidad: ", inventario[i,2], " - precio: C$", inventario[i,3]
					FinPara
				FinSi
			sino 
				si opcioon="3" Entonces
					Escribir "Gracias por hacer uso del sistema. Hasta luego!"
					salir=Verdadero
				SiNo
					Escribir "Opción inválida. Intente nuevamente!"
				FinSi
			FinSi
		FinSi
	Hasta Que salir=Verdadero
	
FinProceso
