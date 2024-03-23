lista_compras = []

print()
print("Cuando termine de ingresar los productos ingresa la palabra terminar para finalizar la lista")
print()

while True:  
    producto = input("Ingresa un producto: ").strip().lower()
    
    if producto == "terminar":
        break    
    lista_compras.append(producto)

print("\nLista de Productos:")
if lista_compras:
    for producto in lista_compras:
        print(producto)
else:
    print("La lista de compras está vacía.")