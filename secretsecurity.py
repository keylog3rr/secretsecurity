
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

 _______  _______  _______  _______  _______ _________   _______  _______  _______           _______ __________________         
(  ____ \(  ____ \(  ____ \(  ____ )(  ____ \\__   __/  (  ____ \(  ____ \(  ____ \|\     /|(  ____ )\__   __/\__   __/|\     /|
| (    \/| (    \/| (    \/| (    )|| (    \/   ) (     | (    \/| (    \/| (    \/| )   ( || (    )|   ) (      ) (   ( \   / )
| (_____ | (__    | |      | (____)|| (__       | |     | (_____ | (__    | |      | |   | || (____)|   | |      | |    \ (_) / 
(_____  )|  __)   | |      |     __)|  __)      | |     (_____  )|  __)   | |      | |   | ||     __)   | |      | |     \   /  
      ) || (      | |      | (\ (   | (         | |           ) || (      | |      | |   | || (\ (      | |      | |      ) (   
/\____) || (____/\| (____/\| ) \ \__| (____/\   | |     /\____) || (____/\| (____/\| (___) || ) \ \_____) (___   | |      | |   
\_______)(_______/(_______/|/   \__/(_______/   )_(     \_______)(_______/(_______/(_______)|/   \__/\_______/   )_(      \_/   
                                                                                                                                

Hecho por ZQYS. 

Para mis amigos de secret security les dejo este script hecho por mi,
es normalito pero aca se los dejo espero les sirva de algo,
y lleven su  grupo a la cima.



 



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