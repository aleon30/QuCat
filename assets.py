import pygame
from configuracion import ANCHO, ALTO

def cargar_sprite_gato(ruta, tamaño):
    sprite = pygame.image.load(ruta).convert_alpha()
    return pygame.transform.smoothscale(sprite, tamaño)

def cargar_activos():
    fondo = pygame.image.load("img/fondo.jpeg").convert()
    fondo_escala = pygame.transform.scale(fondo, (ANCHO, ALTO))

    titulo_qucat = pygame.image.load("img/QuCatTitulo.png").convert_alpha()
    titulo_victoria = pygame.image.load("img/titulo_victoria.png").convert_alpha()
    titulo_derrota = pygame.image.load("img/titulo_derrota.png").convert_alpha()
    
    medidor_img = pygame.transform.smoothscale(pygame.image.load("img/medidor.jpeg").convert(), (60, 60))
    suelo_img = pygame.image.load("img/suelo.jpeg").convert()

    return {
        "fondo": fondo_escala,
        "titulo_qucat": titulo_qucat,
        "titulo_victoria": titulo_victoria,
        "titulo_derrota": titulo_derrota,
        "medidor": medidor_img,
        "suelo": pygame.transform.scale(suelo_img, (ANCHO, 100)),
    }