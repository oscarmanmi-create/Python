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
 
class Wall(sprite.Sprite):
    def __init__(self, r, g, b, x, y, ancho, alto):
        super().__init__()
        self.r = r
        self.g = g
        self.b = b
        self.ancho = ancho
        self.alto = alto
        self.imagen = Surface((self.ancho, self.alto))
        self.imagen.fill((r, g, b))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
 
    def dibujar(self):
        draw.rect(ventana, (self.r, self.g, self.b), (self.rect.x, self.rect.y, self.ancho, self.alto))
 
ventana = display.set_mode((700, 500))
display.set_caption("Laberinto")
 
fondo = transform.scale(image.load("background.jpg"), (700, 500))
jugador = Player('hero.png', 5, 430, 5)
enemigo = Enemy('cyborg.png', 630, 300, 2)
tesoro = GameSprite('treasure.png', 630, 400, 0)
 
juego = True
fps = time.Clock()
 
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
font.init()
fuente = font.Font(None,80)
texto1 = fuente.render('YOU LOSE',True,(255,0,0))
texto2 = fuente.render('YOU WIN',True,(255,215,0))
w1 = Wall(0, 255, 15, 100, 20, 450, 10)
w2 = Wall(0, 255, 15, 100, 480, 450, 10)
w3 = Wall(0, 255, 15, 100, 20, 10, 380)
w4 = Wall(0, 255, 15, 200, 100, 10, 380)
w5 = Wall(0, 255, 15, 300, 20, 10, 380)
w6 = Wall(0, 255, 15, 400, 100, 10, 380)
 
finish = False
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
 
objetos = [enemigo, w1, w2, w3, w4, w5, w6]
 
while juego == True:
    eventos = event.get()
    for evento in eventos:
        if evento.type == QUIT:
            juego = False
 
    if finish == False:
        ventana.blit(fondo, (0,0))
        jugador.reset()
        jugador.update()
        enemigo.reset()
        enemigo.update()
        tesoro.reset()
        w1.dibujar()
        w2.dibujar()
        w3.dibujar()
        w4.dibujar()
        w5.dibujar()
        w6.dibujar()
 
        if (sprite.collide_rect(jugador, tesoro)):
            finish = True
            money.play()
            ventana.blit(texto2,(200,200))
        for objeto in objetos:
            if (sprite.collide_rect(jugador, objeto)):
                finish = True
                kick.play()
                ventana.blit(texto1,(200,200))
    display.update()
    fps.tick(60)