"""
pygame.display.set_caption()设置标题信息
pygame.display.get_caption()可以获得标题信息 返回一个元组

pygame.display.set_icon(surface对象) 设置icon图标
需要使用 image.load读进来图片
"""
import pygame
from sys import exit

pygame.init()
"""设置标题"""
pygame.display.set_caption('展示icon图标')
pygame.display.set_mode((100, 100), pygame.RESIZABLE)
"""导入图片并且作为icon"""
icon = pygame.image.load("favicon.ico")
pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
