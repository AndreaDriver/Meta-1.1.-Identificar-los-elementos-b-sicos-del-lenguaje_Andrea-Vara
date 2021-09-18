"""""
DESCRIPCION: Calculo de y calculo equivalente en el mínimo número de monedas 
($5, $2, $1, $0.5, $0.2, $0.1) de centimos
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 12/09/21
ULTIMA MODIFICACION: 12/09/21
"""""
#1 peso = 100 centimos

centimos = int(input("CENTIMOS: "))

print("EQUIVALENTE DE {} CENTIMOS EN MONEDA DE $5 ES {}, $2 ES {}, $1 ES {}, $0.5 ES {}, $0.2 ES {}, $0.1 ES {}".format(centimos, centimos/500, centimos/200, centimos/100, centimos/50, centimos/20, centimos/1))
