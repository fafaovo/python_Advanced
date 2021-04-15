import pygame
import sys
from pygame.locals import *

# 初始化
pygame.init()
# 初始化游戏窗口为640px*400px
DISPLAY = pygame.display.set_mode((640, 400))
# 设置窗口标题
pygame.display.set_caption('贪吃蛇')
# 定义一个变量来控制游戏速度
FPSCLOCK = pygame.time.Clock()
# 设置字体
font = pygame.font.SysFont("SIMYOU.TTF", 80)

# 定义颜色变量
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)

"""初始化贪吃蛇和食物"""
# 贪吃蛇的初始位置
snake_Head = [100, 100]
# 初始化贪吃蛇的长度 (注：这里以20*20为一个标准小格子)
snake_Body = [[80, 100], [60, 100], [40, 100]]
# 指定蛇初始前进的方向，向右
direction = "right"

# 给定第一枚食物的位置
food_Position = [300,300]
# 食物标记：0代表食物已被吃掉；1代表未被吃掉。
food_flag = 1

# 运行游戏
for event in pygame.event.get():
    if event.type == QUIT:
        """当接收到退出事件后,退出程序"""
        pygame.quit()
        sys.exit()
    # 判断键盘事件,用方向键 或 wasd 表示上下左右
    elif event.type == KEYDOWN:
        pass
