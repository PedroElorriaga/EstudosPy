import time

from colorama import Fore
from sintaxe import spacePrint, clear

clear()

print(Fore.GREEN + 'Cor verde' + Fore.RESET)
spacePrint()

print(Fore.RED + 'Cor vermelha' + Fore.RESET)
spacePrint()


for i in range(1,11):
    print('Contando: ', end='')
    print(Fore.CYAN, i ,Fore.RESET, end='\r')
    time.sleep(1)


print('Testando quantidade de elementos', end='\r')
print('Pedro')
