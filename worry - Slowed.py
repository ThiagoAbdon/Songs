import sys
import os
from rich import print
from time import sleep

linhas = [
    ("One summer night",0.090),
    ("The fade",0.060),
    ("of night",0.060),
    ("The fade",0.060),
    ("of night",0.060),
    ("The fade of-",0.060),
    ("One summer night",0.090),
    ("The fade",0.060),
    ("of night",0.060),
    ("The fade",0.060),
    ("of night",0.060),
    ("The fade of-",0.060), 
]

delays = [1, 0.75, 0.75, 0.75, 0.75, 2.50, 1, 0.75, 0.75, 0.75, 0.75, 10]


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
    print("[white]♪ worry - slowed ♪[/white]")
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