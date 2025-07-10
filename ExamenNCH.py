productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def stock_marca(marca):
    total=0
    marca=input("Ingrese marca a consultar: ").capitalize()
    if marca in len(productos):
        total+=productos()[1]
        print(f"El stock es de {total}")
    else:
        print("Ese modelo no existe")


def búsqueda_precio(p_min, p_max):
        while True:
            p_min=int(input("Ingrese precio minimo: "))
            if p_min < 0:
                print("Debe ingresar valor arriba de 0")
            elif p_min > 0:
                p_max=int(input("Ingrese precio minimo: "))
                if p_max < 0:
                    print("Debe ingresar valor arriba de 0")
                elif p_max > 0:
                    p_min>stock()[1]<p_max
                    if stock() in p_min and p_max:
                        stock()
                    else:
                        print("No hay notebooks en ese rango de precios")
                        return
                else:
                    print("Debe ingresar valores enteros")
            else:
                print("Debe ingresar valores enteros")



def eliminar_producto(modelo):
    while True:
        modelo=input("Ingrese el modelo: ")
        if modelo in productos():
            del modelo
            print("producto eliminado")
            input("Desea actualizar otro precio (s/n)?:")
            if "si":
                return
            elif "no":
                False
            else:
                print("Ponga si o no")
        elif modelo is not productos():
            print("Modelo no encontrado")
            False

opcion=0
while True:
    print("***MENU PRINCIPAL***")
    print("1.- STOCK DE MARCA")
    print("2.- BUSQUEDA POR PRECIOS")
    print("3.- ELIMINAR PRODUCTO")
    print("4.- SALIR")
    opcion=input("Elija una opcion: ")
    match opcion:
        case "1":
           stock_marca(marca)
        case "2":
            búsqueda_precio(p_min, p_max)
        case "3":
            eliminar_producto(modelo)
        case "4":
            print("Programa finalizado.")
            break
        case _:
            print("Opcion no valida")
    