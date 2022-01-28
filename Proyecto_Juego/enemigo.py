import pygame
import constantes
class Enemigo(pygame.sprite.Sprite):
    def __init__(self,SCREEN_WIDTH, y,img,scale):
        pygame.sprite.Sprite.__init__(self)
        image= img.obtener_imagen(0,32,32,scale,(0,0,0))
        image.set_colorkey((0,0,0))
        self.image=image
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = y
