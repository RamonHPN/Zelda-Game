import pygame
from pygame.locals import *
from sys import exit

mapa = [
         "pppppppppppppppppppppppppppppppppppppppp",
         "p   p                                  p",
         "p   p                                  p",
         "p   p                                  p",
         "p   p                                  p",
         "p                                      p",
         "p                                      p",
         "p            ppppppppp                 p",
         "p            p                         p",
         "pp           p               p         p",
         "p            p                         p",
         "p            ppppppppp                 p",
         "p                     p                p",
         "p                    p                 p",
         "p                   p                  p",
         "p                  p                   p",
         "p                 p                    p",
         "p                p                     p",
         "p               p                      p",
         "pppppppppppppppppppppppppppppppppppppppp",
]

mapa_coisas = [
         "                                        ",
         "                                        ",
         "             aaaaaaaaaaaaaa             ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                ccc                     ",
         "     a         ccc              a       ",
         "                ccc                     ",
         "                                        ",
         "                    a         a         ",
         "                                        ",
         "                                        ",
         "      a a a a a a a                     ",
         "                                        ",
         "                            a           ",
         "                                        ",
         "                                        ",
]

mapa_coisas2 = [
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
         "                                        ",
]
largura = 800
altura = 600

b_larg = largura // 40
b_alt = altura // 20

pygame.init()
tela = pygame.display.set_mode((largura, altura))

def imagens(obj, x, y):
    img_orig = obj.subsurface((x, y), (16, 16))
    img_util = pygame.transform.scale(img_orig, (b_larg, b_alt))
    return img_util

img = pygame.image.load("./basictiles.png").convert_alpha()

grama = imagens(img, 16, 128)
pedra = imagens(img, 48, 0)
arvore = imagens(img, 64, 144)
castelo = imagens(img, 48, 80)


for id_linha, linha in enumerate(mapa):
    for id_coluna, caracter in enumerate(linha):

        x = id_coluna * b_larg
        y = id_linha * b_alt

        if caracter == "p":
            tela.blit(pedra, (x, y))
        else:
            tela.blit(grama, (x, y))
pygame.display.update()

for id_linha, linha in enumerate(mapa_coisas):
    for id_coluna, caracter in enumerate(linha):

        x = id_coluna * b_larg
        y = id_linha * b_alt

        if caracter == "a":
            tela.blit(arvore, (x, y))
        elif caracter == "c":
            tela.blit(castelo, (x, y))

pygame.display.update()


while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()

