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

class Wall(sprite.Sprite):
    def __init__(self, c1, c2, c3, wall_x, wall_y, width, height):
        super().__init__()
        self.color1 = c1
        self.color2 = c2
        self.color3 = c3
        self.width = width
        self.height = height
        self.image = Surface((width, height))
        self.image.fill((c1, c2, c3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

hero = Player('hero.png', 100, 200, 5)
enemy = Enemy('cyborg.png', 620, 300, 3)
treasure = GameSprite('treasure.png', 400, 400, 0)

w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)

# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()

font.init()
win = font.Font(None, 70).render('You win!', True, (0, 255, 255))
lose = font.Font(None, 70).render('You lose!', True, (255, 0, 0))

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        hero.update()
        hero.reset()
        enemy.update()
        enemy.reset()
        treasure.reset()
        w1.draw()
        w2.draw()
        w3.draw()
        if sprite.collide_rect(hero, treasure):
            result = win
            finish = True
        if sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) \
            or sprite.collide_rect(hero, w3) or \
                sprite.collide_rect(hero, enemy):
            finish = True
            result = lose
    else:
        window.blit(result, (200, 200))

    display.update()
    clock.tick(FPS)