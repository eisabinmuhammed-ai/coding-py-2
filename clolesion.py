import pygame
import random
SCREEN_WIDTH,screen_hight
Movment_speed=5
Font_size=72
pygame.init()
background_image=pygame.transform.scale(pygame.image.load("bg.jpg"),(SCREEN_WIDTH,screen_hight))
font=pygame.font.Sysfont("Times new Romen",Font_size)
class sprite(pygame.sprite.Sprite):
    def __init__(self,color,hight,width):
        self.image=pygame.Surface([width,hight])
        self.image.fill(pygame.color("Dodgerblue"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,hight))
        self.rect=self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x=max(min(self.rect.x+x_change,SCREEN_WIDTH-self.rect.width),0)
        self.rect.y=max(min(self.rect.y+y_change,screen_hight-self.rect.hight),0)
screen=pygame.display.set_mode((SCREEN_WIDTH,screen_hight))
pygame.display.set_caption("sprite collesion")
all_spritegroup=pygame.sprite.group()
sprite1=Sprite(pygame.Colour('black'),20,30)
sprite1.rect.x,sprite1.rect.y=random.randint(0,SCRREN_WIDTH-sprite1.rect.width),
random.randint(0,screen_hight-sprite1.rect.hight)
sprite2=Sprite(pygame.Colour('red'),20,30)
sprite2.rect.x,sprite2.rect.y=random.randint(0,SCRREN_WIDTH-sprite2.rect.width),
random.randint(0,screen_hight-sprite2.rect.hight)
all_spritegroup.add(sprite2)
running,won=True,False
clock=pygame.time.clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type==py.KEYDOWN and event.key==pygame.k_x):
            running=False
    if not won:
         keys=pygame.key.get_press()
         x_change=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]*Movment_speed)
         y_change=(keys[pygame.K_DOWN]-keys[pygame.K_UP]*Movment_speed)
         sprite1.move(x_change,y_change)
         if sprite1.rect.colliderect(sprite2.rect):
            all_spritegroup.remove(sprite2)
            won=True
    screen.bitt(background_image,(0,0))
    all_spritegroup.draw(screen)
    if won:
        win_text=font.render("you_win",True,pygame.Color('black'))
        screen_blit(win_text,((SCREEN_WIDTH-win_text.get_width())//2,(screen_hight-win_text.get_height())//2))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()