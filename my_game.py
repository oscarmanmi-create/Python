from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, imagen, x, y, velocidad):
        super().__init__()
        self.imagen = transform.scale(image.load(imagen), (65, 65))
        self.velocidad = velocidad
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
 
    def reset(self):
        ventana.blit(self.imagen, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        teclas = key.get_pressed()
        if teclas[K_UP] and self.rect.y > 0:
            self.rect.y -= self.velocidad
        if teclas[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.velocidad
        if teclas[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.velocidad
        if teclas[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocidad

class Enemy(GameSprite):
    direccion = 'I'
    def update(self):
        if self.rect.x <= 450:
            self.direccion = "D"
        if self.rect.x >= 635:
            self.direccion = "I"
        if self.direccion == 'I':
            self.rect.x -= self.velocidad
        else:
            self.rect.x += self.velocidad

ventana = display.set_mode((700, 500))
display.set_caption("Laberinto")
fondo = transform.scale(image.load("background.jpg"), (700, 500))
jugador = Player('hero.png', 5, 430, 5)
enemigo = Enemy('cyborg.png', 630, 300, 2)
tesoro = GameSprite('treasure.png', 630, 400, 0)