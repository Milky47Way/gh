from pygame import*

window = display.set_mode((500, 700))
display.set_caption('Доганялки')
background = transform.scale(image.load('background.png'), (500, 700))
clock = time.Clock() #photo
FPS = 60
while True:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(FPS)
