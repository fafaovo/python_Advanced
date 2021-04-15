import pygame
import sys

pygame.init()
# 窗口大小
DISPLAY = pygame.display.set_mode((640, 400))
# 设置标题
pygame.display.set_caption("Hello World")

while True:
    # 执行
    for event in pygame.event.get():
        """pygame.event.get() 他会从pygame事件队列中取出事件，并且从队列中删除事件"""
        if event.type == pygame.QUIT:
            """当接收到退出事件后,退出程序"""
            pygame.quit()
            sys.exit()
        """刷新窗体"""
        pygame.display.update()
