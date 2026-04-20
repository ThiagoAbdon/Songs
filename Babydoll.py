#começar com Babydoll em ASCII com tela de carregando em baixo
#depois começar letra da musica
#se possivel coração no final

import sys
from rich import print as rprint
from time import sleep
import os
import pyfiglet

babydoll = pyfiglet.figlet_format("BABY") + pyfiglet.figlet_format("DOLL")

linhas = [
    ("and i can't move on,",0.065),
    ("baby doll",0.08),
    ("waitin'on calls,",0.065),
    ("flippin' through stations",0.040),
    ("i'm outclassed and it's outrageous",0.055),
    ("and I' take it all, baby doll",0.06),
    ("whatever's been weighin' you down",0.06)
]

delays = [0.5, 0.5, 0.7, 0.4, 2.8, 1.0, 1.2]

def loading():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(babydoll)
    rprint("[gray50]Carregando música...[/gray50]")
    sleep(1)

    barra = ""
    for _ in range(20):
        barra += "█"
        os.system('cls' if os.name == 'nt' else "clear")
        print(babydoll)
        rprint(f"[gray50]Carregando música...[/gray50]")
        rprint(f"[green]{barra}[/green]")
        sleep(0.1)


def show_music():
    loading()
    os.system('cls' if os.name == 'nt' else 'clear')

    for i, (linha, velocidade) in enumerate (linhas):
        for letra in linha:
            rprint(f"[red]{letra}[/red]", end="")
            sys.stdout.flush()
            sleep(velocidade)

        print()
        sleep(delays[i])

show_music()
