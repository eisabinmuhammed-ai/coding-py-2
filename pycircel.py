import pygame
pygame.init()
Window=pygame.display.set_mode((400,400))
Window.fill((255,255,255))
green=(0,255,0)
pygame.draw.circle(Window,green,(300,300),50)
pygame.draw.circle(Window,green,(100,100),50,3)
pygame.display.update()
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
pygame.quit()
