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

hero = GameSprite('hero.png', 100, 200, 0)
enemy = GameSprite('cyborg.png', 200, 200, 0)
treasure = GameSprite('treasure.png', 400, 400, 0)

# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))

    hero.reset()
    enemy.reset()
    treasure.reset()

    display.update()
    clock.tick(FPS)