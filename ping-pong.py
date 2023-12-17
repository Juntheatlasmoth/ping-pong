from pygame import *
import time as t

width = 600
height = 500

window = display.set_mode((width, height))
backdrop = (128, 180, 196)

clock = time.Clock()
gameover = False


class gamesprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, s):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = s

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




    def draw(self):
            window.blit(self.image, (self.rect.x, self.rect.y))


class player(gamesprite):
     def update1(self):
          keyspressed = key.get_pressed()

          if keyspressed[K_w] == True and self.rect.y > 0:
               self.rect.y -= self.speed

          if keyspressed[K_s] == True and self.rect.bottom < height:
               self.rect.y += self.speed
    


     def update2(self):
          keyspressed = key.get_pressed()

          if keyspressed[K_UP] == True and self.rect.y > 0:
               self.rect.y -= self.speed

          if keyspressed[K_DOWN] == True and self.rect.bottom < height:
               self.rect.y += self.speed


player1 = player("racket.png", 0, 200, 30, 140, 4)
player2 = player("racket.png", 570, 200, 30, 140, 4)


player_group = sprite.Group()
player_group.add(player1)
player_group.add(player2)


class Ball(gamesprite):
     
    def __init__(self, img, x, y, w, h, s):
        super().__init__(img, x, y, w, h, s)
        self.speed_x = self.speed
        self.speed_y = self.speed
        self.bounce_cd = False
        self.bounce_cd_start = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y <= 0 or self.rect.bottom >= height:
             self.speed_y *= -1

        if self.bounce_cd == False:
             
            if len(sprite.spritecollide(self, player_group, False)) != 0:
                self.speed_x *= -1
                self.bounce_cd = True
                self.bounce_cd_start = t.time()


        if self.bounce_cd == True:
            if t.time() - self.bounce_cd_start >= 0.00000000001:
                self.bounce_cd = False




    
ball = Ball("tennis_ball.png", 200, 200, 50, 50, 4)

while gameover == False:
    for e in event.get():
        if e.type == QUIT:
            gameover = True


    window.fill(backdrop)
    player_group.draw(window)
    ball.draw()

    player1.update1()
    player2.update2()
    ball.update()
    display.update()
    clock.tick(60)