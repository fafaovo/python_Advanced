import pygame
from sys import exit

pygame.init()
screen = width, height = 600, 400
pm = pygame.display.set_mode(screen)
pygame.display.set_caption("鼠标追踪")
icon = pygame.image.load("favicon.ico")
pygame.display.set_icon(icon)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pm.fill((255, 255, 255))
    pygame.display.update()
