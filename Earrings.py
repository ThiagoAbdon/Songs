import sys
import os
from rich import print
from time import sleep

linhas = [
    ("Her love is in your head",0.07),
    ("You lost your earrings in her bed",0.065),
    ("You couldn't tell her that you lost 'em",0.06),
    ("'Cause you're scared and you're not talking",0.06),
    ("So, you think of what to say",0.065),
    ("Then save it for another day",0.065),
    ("'Cause you just never had the heart",0.06),
    ("Now they just drift further apart",0.06),
    ("♪From youu♪",0.12),
    ("-Extra, extra",0.07),
    ("Read all about it",0.07),
    ("Mac is in his feelings and he can't get out of it",0.055),
    ("-Extra, extra",0.07),
    ("Read all about it",0.07),
    ("Mac is in his feelings and he can't get out of it",0.055),
    ("-Extra, extra",0.07),
    ("Read all about it",0.07),
    ("Mac is in his feelings and he can't get out of it",0.055),
    ("-Extra, extra",0.07),
    ("Read all about it",0.07),
    ("Mac is in his feelings and he can't get out of it",0.055),

]

delays = [0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.7, 0.4, 0.4, 0.5, 0.4, 0.4, 0.5, 0.4, 0.4, 0.5, 0.4, 0.4, 1.0]

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
    print("[red]♪ Earrings - Malcolm Todd ♪[/red]")
    sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')


def show_music():
    loading()

    for i, (linha, velocidade) in enumerate(linhas):

        for letra in linha:
            print(f"[yellow]{letra}[/yellow]", end="") 
            sys.stdout.flush()
            sleep(velocidade)

        print()
        sleep(delays[i])  

        if i == 8:  
            os.system('cls' if os.name == 'nt' else 'clear')

show_music()


