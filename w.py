import random 
import time
from colorama import *
import os
try:
    from colorama import *
except:
    os.system("pip install colorama")
da = 0
net = 0
print(Fore.YELLOW +"Чтоб пропустить нажмите Enter")
rch = input(Fore.BLUE + "Раномные шаги:")
if rch == "":
    rch = 3
rch = int(rch)

if rch > 500:
    s = 0.01
elif rch > 100:
    s = 0.05
elif rch > 20:
    s = 0.1
elif rch > 10:
    s = 0.5
else:
    s = 1
for i in range(rch):
    a = random.randint(1, 2)
    if a == 1:
        da += 1
        print(Fore.BLUE + "|"+ Fore.GREEN + f"Поехать {da}")
    else:
        net += 1
        print(Fore.BLUE + "|"+ Fore.RED + f"Не поехать {net}")
    time.sleep(s)
if da == net:
    a = random.randint(1, 2)
    if a == 1:
        da += 1
        print(Fore.BLUE + "|"+ Fore.GREEN + f"Поехать {da}" + Fore.YELLOW + "    Дополнительно")
    else:
        net += 1
        print(Fore.BLUE + "|"+ Fore.RED + f"Не поехать {net}" + Fore.YELLOW + "    Дополнительно")
    time.sleep(s)
    if da > net:
        print(Fore.BLUE + "|--------")
        print(Fore.YELLOW +"|Ты едешь")
        print(Fore.BLUE + "|--------")
    else:
        print(Fore.BLUE + "|-----------")
        print(Fore.YELLOW +"|Ты не едешь")
        print(Fore.BLUE + "|-----------")

elif da > net:
    print(Fore.BLUE + "|--------")
    print(Fore.YELLOW +"|Ты едешь")
    print(Fore.BLUE + "|--------")
else:
    print(Fore.BLUE + "|-----------")
    print(Fore.YELLOW +"|Ты не едешь")
    print(Fore.BLUE + "|-----------")
