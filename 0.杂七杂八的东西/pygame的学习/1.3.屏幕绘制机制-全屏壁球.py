"""
屏幕尺寸和模式
pygame.display.set_mode() 设置相关屏幕模式
pygame.display.Info() 生成屏幕相关信息

窗口标题和图标
pygame.display.set_caption()设置标题信息
pygame.display.set_icon() 设置图标信息
pygame.display.get_caption() 获得图标

"""
"""
pygame.display.set_mode(r=(0,0),flags=0) 设置相关屏幕模式
r是游戏分辨率，采用(width, height)输入
flags是用来控制显示类型,可用|组合使用,常用显示器标签如下
pygame.RESIZABLE 窗口大小可调
pygame.NOFRAME 窗口无边界
pygame.FULLSCREEN 窗口全屏显示

pygame.display.Info() 生成屏幕相关信息
产生一个显示信息对象videoInfo 表达当前屏幕的参数
current_w 当前显示模式的像素宽度
current_h 当前显示模式的像素高度
值得注意的是调用set_mode前获得的是操作系统的
调用之后是用户设置的游戏窗体的信息
"""
import pygame
from sys import exit

pygame.init()
"""获取操作系统的信息"""
vInfo = pygame.display.Info()
"""将宽高设置为屏幕大小"""
size = width, height = vInfo.current_w,vInfo.current_h
"""设置全屏"""
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else ((abs(speed[0]) - 1) * int(speed[0] / abs(speed[0])))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else ((abs(speed[1]) - 1) * int(speed[1] / abs(speed[1])))
            elif event.key == pygame.K_ESCAPE:
                """添加使用esc退出"""
                pygame.quit()
                exit()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(WHITE)
    screen.blit(ball, ballrect)
    pygame.display.update()
    clock.tick(300)
    print(f"x轴{speed[0]} 和 y轴{speed[1]}")
