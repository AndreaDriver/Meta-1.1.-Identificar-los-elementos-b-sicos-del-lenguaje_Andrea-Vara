"""""
DESCRIPCION: Imprimir perimetro y area, con el radio
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 11/09/21
ULTIMA MODIFICACION: 17/09/21
"""""
import math

radio=float(input("Dame el radio: "))

print("PERIMETRO ", round((2*math.pi*radio),2))
print("AREA ", round((math.pi*(radio**2)),2))