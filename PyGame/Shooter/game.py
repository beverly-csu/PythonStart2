from pygame import *
import random

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < width - self.rect.width - 5:
            self.rect.x += self.speed
        if keys[K_SPACE]:
            self.fire()
    def fire(self):
        fire_sound.play()

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > height:
            self.rect.y = -100
            self.rect.x = random.randint(0, width - self.rect.width)
            lost += 1

lost = 0
width, height = 700, 500 
window = display.set_mode((width, height))
display.set_caption('Shooter')

FPS = 60
clock = time.Clock()

# mixer.init()
# mixer.music.load('bg.ogg')
# mixer.music.play()
# fire_sound = mixer.Sound('fire.wav')

background = transform.scale(image.load('bg.jpg'), (width, height))
player = Player('player.png', (width - 65) // 2, height - 70, 10)
monsters = sprite.Group()
for i in range(5):
    x = random.randint(0, width - 80)
    speed = random.randint(1, 8)
    enemy = Enemy('enemy.png', x, -100, speed)
    monsters.add(enemy)

finish = False
run = True
while run:
    if not finish:
        window.blit(background, (0, 0))
        player.update()
        player.reset()

        monsters.update()
        monsters.draw(window)

    for e in event.get():
        if e.type == QUIT:
            run = False

    clock.tick(FPS)
    display.update()