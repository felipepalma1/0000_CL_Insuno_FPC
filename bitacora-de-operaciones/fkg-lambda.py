# -*- coding: utf-8 -*-
import datetime
import shutil
from colorama import Fore, init
init()

# print("fkg\n")

prefijo = 'Registro'

ahora = datetime.datetime.now()

anho = str(ahora.strftime("%G"))
numero_semana = str(ahora.strftime("%V"))
numero_dia = str(ahora.strftime("%u"))
hora = str(ahora.strftime("%H"))
minuto = str(ahora.strftime("%M"))
segundo = str(ahora.strftime("%S"))
microsegundos = str(ahora.strftime("%f"))
nombreArchivo = f"{anho}.{numero_semana}.{numero_dia}.{hora}.{minuto}.{segundo}.{microsegundos}.stdin"
final = f"archivador/{nombreArchivo}"

f = open(nombreArchivo, "x") 

print(Fore.GREEN + "Creado" + " : " + nombreArchivo)
shutil.move(nombreArchivo, "archivador")



#print(Fore.GREEN + "Recursos Python")
#print(f"{anho}.{numero_semana}.{numero_dia}.{hora}.{minuto}.{segundo}.{microsegundos}.stdin")
