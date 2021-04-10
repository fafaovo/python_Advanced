import pygame
from pygame.locals import *
from sys import exit

# 初始化
pygame.init()
# 设置显示的窗口,单位是像素
screen = pygame.display.set_mode((640, 480), 0, 32)
# 设置标题
pygame.display.set_caption("Hello World")

# 加载并切换图像
background = pygame.image.load("sushiplate.jpg").convert()
mouse = pygame.image.load("fugu.png").convert_alpha()

while True:
    # 退出事件退出程序
    for event in pygame.event.get():
        if event.type == QUIT:
            # 256也可以
            pygame.quit()
            exit()
    # 将背景图放到屏幕上
    screen.blit(background, (0, 0))

    # 获取鼠标位置
    x, y = pygame.mouse.get_pos()
    # 计算鼠标中心位置
    x -= mouse.get_width()/2
    y -= mouse.get_height()/2
    # 把光标放上去
    screen.blit(mouse, (x, y))



    # 刷新屏幕
    pygame.display.update()

