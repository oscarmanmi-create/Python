# ¡Crea tu propio juego de disparos!
 
from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Space Invaders')
font.init()
mixer.init()
fail = 0
bullets = sprite.Group()
# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)
 
        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    # método que dibuja al personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
# clase del jugador principal
class Player(GameSprite):
    def update(self):
        teclas = key.get_pressed()
        if teclas[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if teclas[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx, self.rect.top, 30, 40, 10)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        global fail
        self.rect.y += self.speed
        if self.rect.y >=500:
            self.rect.x = randint(60,540)
            self.rect.y = 0
            self.speed = randint(1,3)
            fail +=1
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >=500:
            self.rect.x = randint(60,540)
            self.rect.y = 0
            self.speed = randint(1,2)
fuente = font.SysFont('Arial', 40)
fuente2 = font.SysFont('Arial', 80, bold = True)
juego = True
fps = time.Clock()
fondo = transform.scale(image.load('galaxy.jpg'), (700, 500))
jugador = Player('rocket.png', 300, 400, 80, 100, 10)
enemigos = sprite.Group()
asteroides = sprite.Group()
for i in range(5):
    enemigo = Enemy('ufo.png',randint(60,540), 0, 100, 60,randint(1,3))
    enemigos.add(enemigo)
for i in range (2):
    asteroide = Asteroid('asteroid.png',randint(60,540), 0,50, 30,randint(1,2))
    asteroides.add(asteroide)
mixer.music.load('galaxy.mp3')
mixer.music.play()
disparo = mixer.Sound('fire.ogg')
puntos = 0
lives = 4
finish = False
recharge = False
game_bullets = 0
tiempo_recarga = 0 
while juego == True:
    if finish == False:
        fallos = fuente.render('Fallos:' + str(fail),True,(255,0,0))
        aciertos = fuente.render('Aciertos:' + str(puntos),True, (0,255,0))
        window.blit(fondo, (0,0))
        window.blit(fallos, (40,60))
        window.blit(aciertos, (40,30))
        jugador.reset()
        jugador.update()
        enemigos.draw(window)
        enemigos.update()
        bullets.draw(window)
        bullets.update()
        asteroides.draw(window)
        asteroides.update()
        collision_list = sprite.groupcollide(enemigos,bullets,True,True)
        for collision in collision_list:
            enemigo = Enemy('ufo.png',randint(60,540), 0, 100, 60,randint(1,3))
            enemigos.add(enemigo)
            puntos += 1
            if puntos >= 15:
                finish = True
                victoria = fuente2.render('HAS GANADO',True,(0,255,0))
                window.blit(victoria, (100,200))
        if game_bullets == 10:
            recharge = True
            tiempo_recarga += 1
            recarga = fuente.render('Espera, recargando',True,(255,0,0))
            window.blit(recarga, (150,400))
            if tiempo_recarga == 120:
                recharge = False
                game_bullets = 0
        if fail >= 5:
            finish = True
            derrota = fuente2.render('HAS PERDIDO',True,(255,0,0))
            window.blit(derrota, (100,200))
        if sprite.spritecollide(jugador,asteroides,True):
            lives -= 2
            asteroide = Asteroid('asteroid.png',randint(60,540), 0,50, 30,randint(1,2))
            asteroides.add(asteroide)
        elif sprite.spritecollide(jugador,enemigos,True):
            lives -= 1
            enemigo = Enemy('ufo.png',randint(60,540), 0, 100, 60,randint(1,3))
            enemigos.add(enemigo)
        if lives == 4:
            vidas = fuente.render('Vidas:'+ str(lives), True, (0,255,0))
            window.blit(vidas, (550,30))
        if lives == 3:
            vidas = fuente.render('Vidas:'+ str(lives), True, (255,255,0))
            window.blit(vidas, (550,30))
        if lives == 2:
            vidas = fuente.render('Vidas:'+ str(lives), True, (255,165,0))
            window.blit(vidas, (550,30))
        if lives == 1:
            vidas = fuente.render('Vidas:'+ str(lives), True, (255,0,0))
            window.blit(vidas, (550,30))
        if lives <= 0:
            vidas = fuente.render('Vidas:'+ str(lives), True, (128,128,128))
            window.blit(vidas, (550,30))
            finish = True
            derrota = fuente2.render('HAS PERDIDO',True,(255,0,0))
            window.blit(derrota, (100,200))
    eventos = event.get()
    for evento in eventos:
        if evento.type == QUIT:
            juego = False
        elif evento.type == KEYDOWN:
            if evento.key == K_SPACE:
                if recharge == False:
                    jugador.fire()
                    disparo.play() 
                    game_bullets += 1
            

    display.update()
    fps.tick(60)