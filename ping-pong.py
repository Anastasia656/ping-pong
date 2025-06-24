import pygame
H = 500
W = 700
Game = True
clock = pygame.time.Clock()
window = pygame.display.set_mode((W,H))#содаём окно
ball_img = pygame.Surface((30,30))
player_img = pygame.Surface((30,60))

class Base():#базовый класс
    def __init__(self,x,y,img,speed):
        self.hitbox = img.get_rect(center = (x,y))
        self.img = img
        self.speed = speed

class Ball(Base):
    def __init__(self, x, y, img, speed):
        super().__init__(x, y, img, speed)
        self.speed_x = speed
        self.speed_y = speed
    def move(self):#функция чтобы мяч двигался
        self.hitbox.x += self.speed_x
        self.hitbox.y += self.speed_y
        if self.hitbox.right > W:
            self.speed_x = -self.speed 
        elif self.hitbox.left < 0:
            self.speed_x = self.speed
        if self.hitbox.bottom > H:
            self.speed_y = -self.speed 
        elif self.hitbox.top < 0:
            self.speed_y = self.speed 
ball = Ball(W//2,H//2,ball_img,15)


while Game:
    window.fill((250,250,200))
    event_list = pygame.event.get()#подключаем события
    for event in event_list: 
        if event.type == pygame.QUIT: 
            Game = False
    window.blit(ball.img,ball.hitbox)#наносим мяч на экран
    ball.move()#заставляем мяч двигаться
    pygame.display.update() 
    clock.tick(30)