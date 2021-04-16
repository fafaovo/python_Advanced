"""
pygame.event.KEYDOWN 键盘按下事件
    1.event.unicode 按键的unicode码[不推荐使用]
    2.event.key 按键的常量名称
    3.event.mod 按键修饰符的组合值
pygame.event.KEYUP   键盘释放事件
    1.event.key 按键的常量名称
    2.event.mod 按键修饰符的组合值
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
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.unicode == "":
                """返回键盘的unicode码"""
                print(f"[KEYDOWN]: # {event.key} {event.mod}")
            else:
                print(f"[KEYDOWN]:{event.key} {event.mod}")
    pygame.display.update()
