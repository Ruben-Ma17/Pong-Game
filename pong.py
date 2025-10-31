from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Pong")
window.fill((255,255,255))
game = True
clock = time.Clock()
Fps = 60
while game:
    window.fill((0,0,0))
    for e in event.get():
            if e.type == QUIT:
                print("Game.Quit")
                game = False
    clock.tick(Fps)
    display.update()
