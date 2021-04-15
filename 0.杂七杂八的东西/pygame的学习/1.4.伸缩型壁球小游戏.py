"""
pygame.VIDEORESIZE
这是窗口大小更改的事件
事件发生后，返回event.size.包含新窗口的宽高
可以使用.size[0]宽度 .size[1]高度或者event.w event.h获得
"""
import pygame
from sys import exit

pygame.init()
size = width, height = 600, 400
"""设置窗口大小可调整"""
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
speed = [1, 1]
pygame.display.set_caption("壁球小游戏键盘操作版")
ball = pygame.image.load("images/PYG02-ball.gif")
ballrect = ball.get_rect()
WHITE = 255, 255, 255
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else ((abs(speed[0]) - 1) * int(speed[0] / abs(speed[0])))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else ((abs(speed[1]) - 1) * int(speed[1] / abs(speed[1])))
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if event.type == pygame.VIDEORESIZE:
            """触发事件"""
            size = width, height = event.size[0], event.size[1]
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(WHITE)
    screen.blit(ball, ballrect)
    pygame.display.update()
    clock.tick(300)

