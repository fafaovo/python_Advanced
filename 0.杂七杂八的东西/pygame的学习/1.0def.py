"""
pygame.cdrom	访问光驱
pygame.cursors	加载光标
pygame.display	访问显示设备
pygame.draw	绘制形状、线和点
pygame.event	管理事件
pygame.font	使用字体
pygame.image	加载和存储图片
pygame.joystick	使用游戏手柄或者 类似的东西
pygame.key	读取键盘按键
pygame.mixer	声音
pygame.mouse	鼠标
pygame.movie	播放视频
pygame.music	播放音频
pygame.overlay	访问高级视频叠加
pygame	就是我们在学的这个东西了……
pygame.rect	管理矩形区域
pygame.sndarray	操作声音数据
pygame.sprite	操作移动图像
pygame.surface	管理图像和屏幕
pygame.surfarray	管理点阵图像数据
pygame.time	管理时间和帧信息
pygame.transform	缩放和移动图像
"""
"""
事件     功能           参数
QUIT	用户按下关闭按钮	none
ATIVEEVENT	Pygame被激活或者隐藏	gain, state
KEYDOWN	键盘被按下	unicode, key, mod
KEYUP	键盘被放开	key, mod
MOUSEMOTION	鼠标移动	pos, rel, buttons
MOUSEBUTTONDOWN	鼠标按下	pos, button
MOUSEBUTTONUP	鼠标放开	pos, button
JOYAXISMOTION	游戏手柄(Joystick or pad)移动	joy, axis, value
JOYBALLMOTION	游戏球(Joy ball)?移动	joy, axis, value
JOYHATMOTION	游戏手柄(Joystick)?移动	joy, axis, value
JOYBUTTONDOWN	游戏手柄按下	joy, button
JOYBUTTONUP	游戏手柄放开	joy, button
VIDEORESIZE	Pygame窗口缩放	size, w, h
VIDEOEXPOSE	Pygame窗口部分公开(expose)?	none
USEREVENT	触发了一个用户事件	code
"""