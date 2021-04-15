import pygame
from sys import exit

pygame.init()
# 屏幕大小
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
# 设置速度
speed = [1, 1]
# 设置标题
pygame.display.set_caption("壁球小游戏键盘操作版")
# 导入小球 转换成Surface对象
ball = pygame.image.load("images/PYG02-ball.gif")
ballrect = ball.get_rect()
# 背景颜色
WHITE = 255, 255, 255
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        """判断退出"""
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            """KEYDOWN对键盘敲击的事件定义"""
        elif event.type == pygame.KEYDOWN:
            """三目表达式 xxx if 表达式 else xxx 条件放在了中间"""
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else ((abs(speed[0]) - 1) * int(speed[0] / abs(speed[0])))
                """
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0] - 1) * int(speed[0] / abs(speed[0])))
                我们来拆开这段代码
                xxx = 三目表达式(xxx if aaa else xxx  aaa是判断条件)
                如果速度等于0时，我们不再让他运行
                然后我们来拆else部分  (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
                if speed[0] == 0:
                    speed[0] = speed[0]
                else:
                    speed[0] = speed[0] - 1
                    if speed[0] < 0:
                        speed[0] = abs(speed[0])
                """
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
                """
                if speed[0] > 0:
                    speed[0] = speed[0] + 1
                else:
                    speed[0] = speed[0] - 1
                """
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else ((abs(speed[1]) - 1) * int(speed[1] / abs(speed[1])))
    """使小球运行"""
    # ballrect = ballrect.move(speed[0], speed[1])
    """当小球的左边小于0或者右边大于整个界面的宽度时候，就超出屏幕了，此时将他往反方向拉"""
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    """填充屏幕为白色"""
    screen.fill(WHITE)
    """打印球"""
    screen.blit(ball, ballrect)
    """刷新屏幕"""
    pygame.display.update()
    clock.tick(300)
    print(f"x轴{speed[0]} 和 y轴{speed[1]}")
