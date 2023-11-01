# [ Code Review ]

# 자세히 보아야 예쁘다
# 오래 보아야 사랑스럽다
# 우리의 코드도 그렇다

# 첫 눈을 기다리며
# 미리 메리 크리스마스❄️☃️
# SSAFY 9기 화이팅!

# from. 김하림
# --------------------------------------------------------------------------

import pygame
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")

class SnowFlake():
    def __init__(self, size, position, wind=False):
        self.size = size
        self.position = position
        self.wind = wind    
    
    def fall(self, speed):
        self.position[1] += speed               #y position

        
    def draw(self):
        pygame.draw.circle(screen, WHITE, self.position, self.size)

done = False

clock = pygame.time.Clock()

speed = 1
snow_list = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLACK)

    y_position = 0 #makes it look like it only stays at 0
    x_position = random.randint(0,700)

    speed = 1
    y_position += speed

    flake = SnowFlake(2, [x_position, y_position], False)

    snow_list.append(flake)

    for flake in snow_list:
        flake.draw()  
        flake.fall(speed) #def fall (self, speed):

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit() 