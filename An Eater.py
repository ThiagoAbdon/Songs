import sys
import os
from rich import print
from time import sleep

linhas = [
    ("take some of this, it'll calm you down", 0.040),
    ("you might as well just come around", 0.045),
    ("just come around", 0.075),
    ("lovee usss", 0.055),
    ("together",0.075),
    ("i need her, i need her", 0.090),
    ("i'll feed heer, i'll keep her", 0.090),
    ("i need her, i need her",0.090),
]

delays = [0.65, 0.75, 2.5, 0.75, 0.90, 2.45, 1.60, 6]


def loading():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("[grey50]Carregando música...[/grey50]")
    sleep(1)
    
    barra = ""
    for _ in range(20):
        barra += "█"
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"[grey50]Carregando música...[/grey50]")
        print(f"[green]{barra}[/green]")
        sleep(0.1)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[orange]♪ An Eater - Matt Martiasn ♪[/orange]")
    sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')


def show_music():
    loading()

    for i, (linha, velocidade) in enumerate(linhas):

        for letra in linha:
            print(f"[red]{letra}[/red]", end="") 
            sys.stdout.flush()
            sleep(velocidade)

        print()
        sleep(delays[i])  

show_music()

