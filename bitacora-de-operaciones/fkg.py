# -*- coding: utf-8 -*-
import datetime
print("fkg\n")

prefijo = 'Registro'


while True:
    ahora = datetime.datetime.now()

    anho = str(ahora.strftime("%G"))
    numero_semana = str(ahora.strftime("%V"))
    numero_dia = str(ahora.strftime("%u"))
    hora = str(ahora.strftime("%H"))
    minuto = str(ahora.strftime("%M"))
    segundo = str(ahora.strftime("%S"))
    microsegundos = str(ahora.strftime("%f"))
    print(f"{anho}.{numero_semana}.{numero_dia}.{hora}.{minuto}.{segundo}.{microsegundos}.stdin")
