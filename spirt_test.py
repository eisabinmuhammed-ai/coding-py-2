import pygame 
import random
pygame.init()
scce=pygame.USEREVENT+1
bcce=pygame.USEREVENT+2
blue=pygame.Color("blue")
darkblue=pygame.Color("Dark blue")
skyblue=pygame.Color("sky blue")
yellow=pygame.Color("yellow")
red=pygame.Color("red")
orenge=pygame.Color("orenge")
white=pygame.Color("white")
class sprait(pygame.sprite.Sprite):
    def __init__(self,color,hight,whidth,hight):
        self.image=pygame.surface({whidth,hight})
        self.image.fill(coloer)
        self.rect=self.image.get_rect()
        self.velocety=[random.choice[(-1,1)],random.choice[(-1,1)]]
    def update(self):
        self.rect.move_ip(self.velocety)
        boudry_hit=False
        if  self.rect.left<= 0 or self.rect.bottom>=400:
            self.velocety[1]=-self.velocety[1]
            boudry_hit=True
        if boudry_hit:
            pygame.event.post(pygame.event.Event(scce))
            pygame.event.post(pygame.event.Event(bcce))
        def cc():
            self.image.fill(random.choice([yellow,red,orenge,white]))
def cbc():
     global bg_color
     bg_color=random.choice([yellow,red,orenge,white])
