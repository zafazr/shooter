#Создай собственный Шутер!
 
from pygame import *
from random import *
 
counter_missings = 0
finish = False
 
init()
 
window = display.set_mode((700,500))
display.set_caption('Shooter')
 
clock = time.Clock()
 
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
 
 
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed = 5, w = 65, h = 65):
        super().__init__()
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(img), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
 
    def paint(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
 
class Rocket(GameSprite):
    def move(self):
        if keys[K_a] and self.rect.x >0:
            self.rect.x -= 7
 
        if keys[K_d] and self.rect.x < 630:
            self.rect.x += 7
 
class Ufo(GameSprite):
    def update(self):
        global counter_missings
        self.rect.y += self.speed
        if self.rect.y >= 500:
            counter_missings += 1
            self.rect.y = -50
            self.rect.x = randint(10, 630)

class Asteroid(GameSprite):
    def update(self):
        global counter_missings
        self.rect.y += self.speed
        if self.rect.y >= 500:
            counter_missings += 1
            self.rect.y = -50
            self.rect.x = randint(10, 630)
 
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

        
font = font.SysFont("Arial", 50)
lose = font.render('YOU LOSE!', True, (255,0,0))
background = transform.scale(image.load('galaxy.jpg'), (700,500))
rocket = Rocket('rocket.png', 300, 430, 10)
ufo1 = Ufo('ufo.png', randint(10, 630), 0, 3)
ufo2 = Ufo('ufo.png', randint(10, 630), 0, 3)
ufo3 = Ufo('ufo.png', randint(10, 630), 0, 3)
ufo4 = Ufo('ufo.png', randint(10, 630), 0, 3)
ufo5 = Ufo('ufo.png', randint(10, 630), 0, 3)

asteroid = Asteroid('asteroid.png', randint(10, 630), 0, 3)
asteroid2 = Asteroid('asteroid.png', randint(10, 630), 0, 3)
asteroid3 = Asteroid('asteroid.png', randint(10, 630), 0, 3)



ufos = sprite.Group()
ufos.add(ufo1)
ufos.add(ufo2)
ufos.add(ufo3)
ufos.add(ufo4)
ufos.add(ufo5)

asteroids = sprite.Group()
asteroids.add(asteroid)
asteroids.add(asteroid2)
asteroids.add(asteroid3)
 
bullets = sprite.Group()
 
game = True
while game:
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                bullets.add(Bullet('bullet.png',rocket.rect.centerx-7,rocket.rect.top,30,15,30))    

   
    #printing
    window.blit(background, (0,0))
    rocket.paint()
    ufos.draw(window)
    bullets.draw(window)
    asteroids.draw(window)
    if counter_missings == 3:
        window.blit(lose,(250,200))
 
    #moves
    rocket.move()
    ufos.update()
    bullets.update()
    asteroids.update()

    sprite.groupcollide(bullets, ufos, True, True)
    if len(ufos) < 5:
        ufos.add(Ufo('ufo.png', randint(10, 630), 0, 3))
 
    sprite.spritecollide(rocket, ufos, True)
    
    display.update()
    clock.tick(60)