from pygame import *
from random import randint
ventana = display.set_mode((700, 500))
display.set_caption('Space Invaders')
font.init()
mixer.init()
contador = 0
carrots = sprite.Group()
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
        self.inicial_x = self.rect.x
        self.inicial_y = self.rect.y
    # método que dibuja al personaje en la ventana
    def reset(self):
        ventana.blit(self.image, (self.rect.x, self.rect.y))
saltando = False
class Player(GameSprite):
    def update(self):
        teclas = key.get_pressed()
        if teclas[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if teclas[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed   
    def fire(self):
        carrot = Carrot('carrot.png',self.rect.right, self.rect.centery, 30, 40, 10)
        carrots.add(carrot)
class Enemy(GameSprite):
    direccion = 'I'
    def update(self):
        if self.rect.x <= self.inicial_x -50:
            self.direccion = "D"
        if self.rect.x >= self.inicial_x +50:
            self.direccion = "I"
        if self.direccion == 'I':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Carrot(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 620:
            self.kill()
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
wall = Wall(randint(0,250),randint(0,250),randint(0,250),100,400,100,100)
wall2 = Wall(randint(0,250),randint(0,250),randint(0,250),300,400,100,100)
wall3 = Wall(randint(0,250),randint(0,250),randint(0,250),500,400,100,100)
farmers = sprite.Group()
farmer1 = Enemy('farmer.png',wall.rect.centerx,wall.rect.top -100,80,100,5)  
farmers.add(farmer1)
farmer2 = Enemy('farmer.png',wall2.rect.centerx,wall2.rect.top -100,80,100,5)  
farmers.add(farmer2)
farmer3 = Enemy('farmer.png',wall3.rect.centerx,wall3.rect.top -100,80,100,5)  
farmers.add(farmer3)
fondo = transform.scale(image.load('fondo.jpg'),(700,500))
rabbit = Player('rabbit.png',20,400,80,100,10)
owl = GameSprite('owl.png',600,randint(200,400),80,100,0)
juego = True
clock = time.Clock()
fuente = font.SysFont('Arial', 40)
finish = False
lives = 8
recharge = False
game_bullets = 0
tiempo_recarga = 0 
while juego == True:
    if finish == False:
        if sprite.collide_rect(rabbit, wall):
            rabbit.rect.bottom = wall.rect.top
        elif sprite.collide_rect(rabbit, wall2):
            rabbit.rect.bottom = wall2.rect.top
        elif sprite.collide_rect(rabbit, wall3):
            rabbit.rect.bottom = wall3.rect.top
        elif saltando == False:
            rabbit.rect.y = 400
        ventana.blit(fondo, (0,0))
        rabbit.reset()
        rabbit.update()
        farmers.draw(ventana)
        farmers.update()
        carrots.draw(ventana)
        carrots.update()
        wall.dibujar()
        wall2.dibujar()
        wall3.dibujar()
        owl.reset()
        farmer_collision_list = sprite.groupcollide(farmers,carrots, True, True)
        if saltando == True:
            contador += 1
        if contador >= 60:
            contador = 0
            rabbit.rect.y += 100
            saltando = False
        if game_bullets == 3:
            recharge = True
            tiempo_recarga += 1
            recarga = fuente.render('Espera, recargando',True,(255,0,0))
            ventana.blit(recarga, (150,400))
            if tiempo_recarga == 120:
                recharge = False
                game_bullets = 0
        elif sprite.spritecollide(rabbit,farmers,False):
            lives -= 1 
        if lives == 8 or lives == 7:
            vidas = fuente.render('Vidas:'+ str(lives), True, (0,255,0))
            ventana.blit(vidas, (550,30))
        if lives == 6 or lives == 5:
            vidas = fuente.render('Vidas:'+ str(lives), True, (255,255,0))
            ventana.blit(vidas, (550,30))
        if lives == 4 or lives == 3:
            vidas = fuente.render('Vidas:'+ str(lives), True, (255,165,0))
            ventana.blit(vidas, (550,30))
        if lives == 2 or lives == 1:
            vidas = fuente.render('Vidas:'+ str(lives), True, (255,0,0))
            ventana.blit(vidas, (550,30))
        if lives <= 0:
            vidas = fuente.render('Vidas:'+ str(lives), True, (128,128,128))
            ventana.blit(vidas, (550,30))
            finish = True
            derrota = fuente.render('HAS PERDIDO',True,(255,0,0))
            ventana.blit(derrota, (100,200))
        if sprite.collide_rect(rabbit,owl):
            finish = True
            victoria = fuente.render('HAS GANADO',True,(0,255,0))
            ventana.blit(victoria, (100,200))
    eventos = event.get()
    for evento in eventos:
        if evento.type == QUIT:
            juego = False
        if evento.type == KEYDOWN:
            if evento.key == K_SPACE:
                rabbit.fire()
                game_bullets += 1  
            if evento.key == K_UP:
                if saltando == False:
                    rabbit.rect.y -= 100
                    saltando = True
    display.update()   
    clock.tick(60)