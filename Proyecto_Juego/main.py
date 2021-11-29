import pygame
import constantes
import random
from juego import Juego

j=Juego()
while j.running:
    j.playing=True
    j.loop_juego()


pygame.init()
""" 
creamos la ventana y le indicamos un titulo
 """
screen = pygame.display.set_mode((constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT))
pygame.display.set_caption("SALTOS")
"""
definir los frames
"""
reloj = pygame.time.Clock()
FPS = 60
"""
Variables del juego
"""

"""
Otras variables
"""
gravedad = 1
Max_Platforms = 10
"""
Cargar la imagen de fondo
"""
fondo = pygame.image.load('img/fondo2.jpg').convert_alpha()
personajeDe_img = pygame.image.load('img/quieto.png').convert_alpha()
platform_img = pygame.image.load('img/platform.png').convert_alpha()


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


class Jugador():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(personajeDe_img, (70, 90))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def movimiento(self):
        dx = 0
        dy = 0
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_a]:
            dx = -10
            self.flip = True
        if tecla[pygame.K_d]:
            dx = 10
            self.flip = False

        # gravedad
        self.vel_y += gravedad
        dy += self.vel_y

        # asegurarse que no se sale de la pantalla
        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left
        if self.rect.right + dx > constantes.SCREEN_WIDTH:
            dx = constantes.SCREEN_WIDTH - self.rect.right

        # comprobar la colisión con las plataformas
        for platform in platform_grupo:
            # colisión en la dirección y
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # comprobar si es debajo del la plataforma
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = -20

        # comprobar la colisión con el suelo
        if self.rect.bottom + dy > constantes.SCREEN_HEIGHT:
            dy = 0
            self.vel_y = -20
        self.rect.x += dx
        self.rect.y += dy

    def dibujar(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 20, self.rect.y - 25))

    # def inicio_juego(self):
    # https://freakspot.net/creacion-de-un-videojuego-con-pygame/


# Clase para la plataforma
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_img, (width, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Instancia de jugador
jumpy = Jugador(constantes.SCREEN_WIDTH // 2, constantes.SCREEN_HEIGHT - 150)

# crear grupos de plataformas
platform_grupo = pygame.sprite.Group()

# crear plataformas temporales
for p in range(Max_Platforms):
    platform_width = random.randint(60, 90)
    platform_x = random.randint(0, constantes.SCREEN_WIDTH - platform_width)
    platform_y = p * random.randint(90, 120)
    platform = Platform(platform_x, platform_y, platform_width)
    platform_grupo.add(platform)

""" 
    el bucle principal del juego
    """

# def main_menu():
#     selected = "start"

while True:
    reloj.tick(FPS)
    jumpy.movimiento()
    # hace aparecer el fondo
    screen.blit(fondo, (0, 0))
    # dibuja
    platform_grupo.draw(screen)
    jumpy.dibujar()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #         quit()
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_UP:
    #             selected = "start"
    #         elif event.key == pygame.K_DOWN:
    #             selected = "quit"
    #         if event.key == pygame.K_SPACE:
    #             if selected == "start":
    #                 run = True
    #             if selected == "quit":
    #                 quit()
    # screen.fill(constantes.blue)
    # title = text_format("Saltos", constantes.font, 90, constantes.yellow)
    # if selected == "start":
    #     text_start = text_format("START", constantes.font, 75, constantes.white)
    # else:
    #     text_start = text_format("START", constantes.font, 75, constantes.black)
    # if selected == "quit":
    #     text_quit = text_format("QUIT", constantes.font, 75, constantes.white)
    # else:
    #     text_quit = text_format("QUIT", constantes.font, 75, constantes.black)
    # title_rect = title.get_rect()
    # start_rect = text_start.get_rect()
    # quit_rect = text_quit.get_rect()
    # screen.blit(title, (constantes.SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))
    # screen.blit(text_start, (constantes.SCREEN_WIDTH / 2 - (start_rect[2] / 2), 300))
    # screen.blit(text_quit, (constantes.SCREEN_WIDTH / 2 - (quit_rect[2] / 2), 360))
    pygame.display.update()

# main_menu()
pygame.quit()
