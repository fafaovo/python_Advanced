"""
pygame.event.MOUSEMOTION 鼠标移动事件
    只要鼠标移动就会返回的事件
    1.event.pos 鼠标当前坐标值(x,y) 相对于窗口左上角
    2.event.rel 鼠标相对运动距离(x,y) 相对于上次事件
    3.event.buttons 返回鼠标按键状态
    假设鼠标有三个键 对应(a,b,c)
    如果鼠标移动时,这三个处于按下状态，对应的值为1.反之则0
pygame.event.MOUSEBUTTONUP 鼠标键释放事件
    1.event.pos 坐标
    2.event.button 返回按下键编号n 取整 与设备相关
pygame.event.MOUSEBUTTONDOWN 鼠标键按下事件
    和 MOUSEBUTTONUP 一样

"""
import pygame
import random
from sys import exit

pygame.init()
size = width,height = 600, 400
cur = pygame.display.set_mode(size)
pygame.display.set_caption("pygame事件处理")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEMOTION:
            print(f"[MOUSEMOTION]:{event.pos} {event.rel} {event.buttons}")
        elif event.type == pygame.MOUSEBUTTONUP:
            print(f"[MOUSEBUTTONUP]:{event.pos} {event.button}")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"[MOUSEBUTTONDOWN]:{event.pos} {event.button}")
    pygame.display.update()