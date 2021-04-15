import pygame
import sys

"""
pygame.image.load(路径) 将图片载入游戏支持JPG PNG GIF等等
在pygame中导入如何的图片都表示为Surface对象 
get_rect()已对象外形向切的矩形
在pygame提供一个move(x,y)可以让图形横轴移动x像素 纵轴移动y像素
fill填充背景颜色
"""
pygame.init()
# 修改窗体的尺寸
size = width, height = 600, 400
# 壁球的速度
speed = [1, 1]
# 设置刷新颜色
BLACK = 0, 0, 0
# 设置窗口大小
screen = pygame.display.set_mode(size)
# 设置标题
pygame.display.set_caption("PYGAME壁球")
# 载入图片 并且生成surface对象
ball = pygame.image.load("images/PYG02-ball.gif")
ballrect = ball.get_rect()

while True:
    # 执行
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ballrect = ballrect.move(speed[0], speed[1])
    """如果左边大于0了或者右边大于框的大小了"""
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        """注意这是个符号"""
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    """
    来解释一下原理，当小球正好遇到屏幕时，偏移量取反,那么他就会往反方向移动
    """
    # 填充背景
    screen.fill(BLACK)
    # 放置球以及偏移量
    screen.blit(ball, ballrect)

    """
    pygame.time.Clock()创建一个Clock对象，用于操作时间
    Clock对象.tick(帧率) 假设是100表示每秒刷新100次
    """
    clock = pygame.time.Clock()
    clock.tick(300)


    """刷新窗体"""
    pygame.display.update()

