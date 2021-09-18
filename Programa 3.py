"""""
DESCRIPCION: De una cantidad de segundos y sale el número de días, horas,
minutos y segundos.
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 11/09/21
ULTIMA MODIFICACION: 17/09/21
"""""

segundos = int(input("SEGUNDOS: "))

print("SEGUNDOS ", segundos)
print("DIAS", round((segundos/86400),2))
print("HORAS ", round((segundos/3600),2))
print("MINUTOS ",   round((segundos/60),2))