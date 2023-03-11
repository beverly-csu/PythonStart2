from time import time as millis
from pygame import *
font.init()
import random

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width=65, height=65):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    prev_shot = millis()
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < width - self.rect.width - 5:
            self.rect.x += self.speed
        if keys[K_SPACE]:
            self.fire()
    def fire(self):
        if millis() - self.prev_shot > 0.2:
            fire_sound.play()
            x = self.rect.centerx
            y = self.rect.y
            bullet = Bullet('bullet.png', x, y, 10, 10, 20)
            bullets.add(bullet)
            self.prev_shot = millis()

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > height:
            self.rect.y = -100
            self.rect.x = random.randint(0, width - self.rect.width)
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -self.rect.height:
            self.kill()

lost = 0
score = 0
width, height = 700, 500 
window = display.set_mode((width, height))
display.set_caption('Shooter')

FPS = 60
clock = time.Clock()

my_font = font.Font('Lemon Tuesday.otf', 40)
my_font2 = font.Font('Lemon Tuesday.otf', 72)

mixer.init()
mixer.music.load('bg.ogg')
mixer.music.play()
mixer.music.set_volume(0.05)
fire_sound = mixer.Sound('fire.wav')
fire_sound.set_volume(0.05)

background = transform.scale(image.load('bg.jpg'), (width, height))
player = Player('player.png', (width - 65) // 2, height - 70, 10)
monsters = sprite.Group()
for i in range(5):
    x = random.randint(0, width - 80)
    speed = random.randint(1, 8)
    enemy = Enemy('enemy.png', x, -100, speed)
    monsters.add(enemy)

bullets = sprite.Group()

finish = False
run = True
while run:
    if not finish:
        window.blit(background, (0, 0))
        player.update()
        player.reset()

        monsters.update()
        monsters.draw(window)

        bullets.update()
        bullets.draw(window)

        score_text = my_font.render('Счёт: ' + str(score), True, (230, 230, 230))
        lost_text = my_font.render('Пропущенно: ' + str(lost), True, (230, 230, 230))
        window.blit(score_text, (10, 10))
        window.blit(lost_text, (10, 50))

        collided = sprite.groupcollide(monsters, bullets, True, True)
        if len(collided) != 0:
            for i in range(len(collided)):
                score += 1
                x = random.randint(0, width - 80)
                speed = random.randint(1, 8)
                enemy = Enemy('enemy.png', x, -100, speed)
                monsters.add(enemy)

        if score >= 10:
            ## 1 вариант
            # win_text = my_font.render('Вы выиграли!', True, (230, 230, 230))
            # window.blit(win_text, (270, 200))
            ## 1 вариант
            ## 2 вариант
            result_text = my_font2.render('Вы выиграли!', True, (230, 230, 230))
            text_rect = result_text.get_rect()
            bg_rect = background.get_rect()
            text_rect.center = bg_rect.center
            window.blit(result_text, (text_rect.x, text_rect.y))
            ## 2 вариант
            finish = True
        if lost >= 3:
            ## 1 вариант
            # win_text = my_font.render('Вы проиграли!', True, (230, 230, 230))
            # window.blit(win_text, (270, 200))
            ## 1 вариант
            ## 2 вариант
            result_text = my_font2.render('Вы проиграли!', True, (230, 230, 230))
            text_rect = result_text.get_rect()
            bg_rect = background.get_rect()
            text_rect.center = bg_rect.center
            window.blit(result_text, (text_rect.x, text_rect.y))
            ## 2 вариант
            finish = True
        last_time = millis()
    else:
        window.blit(background, (0, 0))
        window.blit(result_text, (text_rect.x, text_rect.y))
        if millis() - last_time > 5:
            score = 0
            lost = 0
            bg_rect = background.get_rect()
            player.rect.centerx = bg_rect.centerx
            monsters.empty()
            for i in range(5):
                x = random.randint(0, width - 80)
                speed = random.randint(1, 8)
                enemy = Enemy('enemy.png', x, -100, speed)
                monsters.add(enemy)
            bullets.empty()
            finish = False
            



    for e in event.get():
        if e.type == QUIT:
            run = False

    clock.tick(FPS)
    display.update()