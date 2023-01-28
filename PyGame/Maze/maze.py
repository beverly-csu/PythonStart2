from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Лабиринт')

background = transform.scale(image.load('background.jpg'), (700, 500))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = 'left'

    def update(self):
        if self.rect.x <= 520:
            self.direction = 'right'
        if self.rect.x >= 620:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed

hero = Player('hero.png', 100, 200, 5)
enemy = Enemy('cyborg.png', 620, 300, 3)
treasure = GameSprite('treasure.png', 400, 400, 0)

rect1 = rect.Rect(x1, y1, width, height)
rect1 = rect.Rect(x2, y2, width, height)
# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))

    hero.update()
    hero.reset()
    enemy.update()
    enemy.reset()
    treasure.reset()

    display.update()
    clock.tick(FPS)