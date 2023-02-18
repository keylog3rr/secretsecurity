
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier
import sys
from colorama import Fore
import os
import time
import colorama


print("<<<<INSTALANDO LOS PAQUETES NECESARIO PARA EJECUTAR EL SCRIPT>>>>     SCRIPT HECHO POR ZQYS")
time.sleep(1)
print("...")
os.system("pip install phonenumbers")
os.system("pip install colorama")
print("")
print("OPERACION COMPLETADA...")
time.sleep(0.2)
print("iniciando script...")
time.sleep(0.1)
os.system("clear")


print(""" 



_¶¶¶¶¶
__¶__¶¶¶
__¶¶___¶¶¶
___¶¶____¶¶
____¶¶_____¶¶
______¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_______¶¶_______________________________¶¶
_________¶¶_____________________________¶¶¶
__________¶_______________________¶¶¶¶¶¶¶
_________¶___________________¶¶¶¶¶¶¶
_________¶______________¶¶¶¶¶¶¶
_________¶___________¶¶¶¶¶
_________¶____________¶¶
________¶¶_______¶¶¶___¶¶¶
________¶________¶¶¶¶____¶¶
________¶_______¶¶__¶¶¶___¶¶¶
________¶______¶¶_____¶¶____¶¶
_______¶¶_____¶¶_______¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶
_______¶¶_____¶¶_________¶¶¶___¶________¶¶
_______¶_____¶¶___________¶¶¶____________¶¶¶
_______¶____¶¶_____________¶¶_____¶¶¶¶¶¶¶¶¶
______¶¶____¶______________¶¶____¶¶¶¶
______¶¶___¶¶_____________¶¶____¶¶¶¶¶
______¶___¶¶______________¶¶___¶¶_¶¶¶¶
______¶¶_¶¶_______________¶¶__¶¶
_______¶¶¶_________________¶¶_¶¶
____________________________¶¶¶
_____________________________¶

 _______  _______  _______  _______  _______ _________   _______  _______  _______           _______ __________________         
(  ____ \(  ____ \(  ____ \(  ____ )(  ____ \\__   __/  (  ____ \(  ____ \(  ____ \|\     /|(  ____ )\__   __/\__   __/|\     /|
| (    \/| (    \/| (    \/| (    )|| (    \/   ) (     | (    \/| (    \/| (    \/| )   ( || (    )|   ) (      ) (   ( \   / )
| (_____ | (__    | |      | (____)|| (__       | |     | (_____ | (__    | |      | |   | || (____)|   | |      | |    \ (_) / 
(_____  )|  __)   | |      |     __)|  __)      | |     (_____  )|  __)   | |      | |   | ||     __)   | |      | |     \   /  
      ) || (      | |      | (\ (   | (         | |           ) || (      | |      | |   | || (\ (      | |      | |      ) (   
/\____) || (____/\| (____/\| ) \ \__| (____/\   | |     /\____) || (____/\| (____/\| (___) || ) \ \_____) (___   | |      | |   
\_______)(_______/(_______/|/   \__/(_______/   )_(     \_______)(_______/(_______/(_______)|/   \__/\_______/   )_(      \_/   
                                                                                                                                



 



 """)
    


print("[1] Scanear numero telefonico")
print("[2] Informacion del creador")
print("[3] Salir")





opcion = input("Elije entre el [1-2-3] -> ")
if opcion == "1":
    num = input("Ingrese el numero de telefono -> ")
    numero = phonenumbers.parse(num)
    zona= timezone.time_zones_for_geographical_number(numero)
    region = geocoder.description_for_number(numero, 'en')
    Carr  = carrier.name_for_number(numero, 'en')
    valido = phonenumbers.is_valid_number(numero)
    if valido == True:
        print("Zona ->", zona)
        print("Carrier ->", Carr)
        print("Region ->", region)
    elif valido == False:
        print(Fore.RED + "El numero no existe")

elif opcion == "3":
        sys.exit()

elif opcion == "2":
    print("Este script esta creado para Secret Security de parte de ZQYS.")
    print(Fore.LIGHTGREEN_EX + "Instagram - @payl0add")       
else:
    print("""Esa opcion no existe
Saliendo del programa""")