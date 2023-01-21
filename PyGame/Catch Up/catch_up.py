from os import close
from pygame import *

#создай окно игры
size = (700, 500)
window = display.set_mode(size)
display.set_caption('Догонялки [Catch Up]')
#задай фон сцены
background = transform.scale(image.load('background.png'), (700, 500))
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
#обработай событие «клик по кнопке "Закрыть окно"»
game = True
clock = time.Clock()
FPS = 60
x1, y1 = 50, 100
x2, y2 = 500, 100
while game:
    key_pressed = key.get_pressed()
    # 1 player
    if key_pressed[K_s] and y1 < 395:
        y1 += 10
    if key_pressed[K_w] and y1 > 5:
        y1 -= 10
    if key_pressed[K_a] and x1 > 5:
        x1 -= 10
    if key_pressed[K_d] and x1 < 595:
        x1 += 10
    # 2 player
    if key_pressed[K_DOWN] and y2 < 395:
        y2 += 10
    if key_pressed[K_UP] and y2 > 5:
        y2 -= 10
    if key_pressed[K_LEFT] and x2 > 5:
        x2 -= 10
    if key_pressed[K_RIGHT] and x2 < 595:
        x2 += 10

    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False 

    clock.tick(FPS)
    display.update()