import pygame
pygame.font.init()
H = 500
W = 700
Game = True
clock = pygame.time.Clock()
window = pygame.display.set_mode((W,H))#содаём окно
ball_img = pygame.Surface((30,30))
player_1_img = pygame.Surface((30,80))
player_2_img = pygame.Surface((30,80)) 
font = pygame.font.Font(None,80)

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
            self.hitbox.center = (W//2,H//2)
            player_1.score += 1 
            player_1.score_img = font.render(str(player_1.score),True,(0,0,0))
        elif self.hitbox.left < 0: 
            self.speed_x = self.speed 
            self.hitbox.center = (W//2,H//2) 
            player_2.score += 1 
            player_2.score_img = font.render(str(player_2.score),True,(0,0,0)) 
        if self.hitbox.bottom > H:
            self.speed_y = -self.speed 
        elif self.hitbox.top < 0:
            self.speed_y = self.speed 
ball = Ball(W//2,H//2,ball_img,10)

class Player(Base):
    def __init__(self, x, y, img, speed):
        super().__init__(x, y, img, speed)
        self.speed_y = speed
        self.score = 0 
        self.score_img = font.render(str(self.score),True,(0,0,0))
    def move(self):
        buttons = pygame.key.get_pressed()
        if buttons[pygame.K_w] == True:
            self.hitbox.y -= self.speed
            if self.hitbox.top < 0:
                self.hitbox.top = 0
        if buttons[pygame.K_s] == True:
            self.hitbox.y += self.speed
            if self.hitbox.bottom > H:
                self.hitbox.bottom = H
        if self.hitbox.colliderect(ball.hitbox) == True:
            ball.speed_x = ball.speed
    def avto_pilot(self):
        if self.hitbox.centery > ball.hitbox.centery:
            self.speed_y = -self.speed 
        if self.hitbox.centery < ball.hitbox.centery:
            self.speed_y = self.speed     
        if self.hitbox.colliderect(ball.hitbox) == True:
            ball.speed_x = -ball.speed
        self.hitbox.y += self.speed_y

player_1 =Player(30,250,player_1_img,10)
player_2 =Player(W-30,250,player_1_img,6)

while Game:
    window.fill((250,250,200))
    event_list = pygame.event.get()#подключаем события
    for event in event_list: 
        if event.type == pygame.QUIT: 
            Game = False
    window.blit(ball.img,ball.hitbox)#наносим мяч на экран  
    window.blit(player_1.img,player_1.hitbox)
    window.blit(player_2.img,player_2.hitbox)
    window.blit(player_1.score_img,(80,30))
    window.blit(player_2.score_img,(W-80,30))
    ball.move()#заставляем мяч двигаться
    player_1.move()
    player_2.avto_pilot()

    pygame.display.update() 
    clock.tick(30)