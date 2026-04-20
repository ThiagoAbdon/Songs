import sys
from rich import print
from time import sleep

# Lista de tuplas com as letras da música e a velocidade de digitação de cada linha
# Cada item é: ("texto da linha", velocidade_em_segundos_por_letra)
linhas = [
    ("Don't you give me up",0.09),
    ("Please, don't give me up",0.09),
    ("Honey, I belong",0.08),
    ("With you and only you",0.07),
    ("babyyyyy",0.09),
    ("Only u, my girl",0.06),
    ("Only u, babe",0.06),
    ("Only u, darling",0.06),
    ("Only u, babe",0.06),
    ("Only u, my girl",0.062),
    ("Only u, babe",0.062),
    ("Only u, darling",0.062),
    ("Only you ❤",0.06),
]

# Pausa (em segundos) após cada linha ser exibida
# Simula o ritmo da música entre os versos
delays = [0.85, 0.75, 1, 1, 1.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.4, 0.4, 1]

def show_music():
     # Percorre cada linha junto com seu índice
    # enumerate() retorna o índice (i) e o valor (linha, velocidade) ao mesmo tempo
    for i, (linha, velocidade) in enumerate(linhas):


        # Percorre letra por letra da linha atual
        for letra in linha:
            print(f"[red]{letra}[/red]", end="")    # end="" evita pular de linha a cada letra
            sys.stdout.flush()      # força o terminal a exibir a letra na hora, sem esperar buffer
            sleep(velocidade)       # pausa entre cada letra, dando efeito de digitação
        
        print()                     # pula linha após terminar de "digitar" o verso
        sleep(delays[i])            # pausa antes do próximo verso, seguindo o ritmo da música
    
show_music()   # chama a função para iniciar a exibição