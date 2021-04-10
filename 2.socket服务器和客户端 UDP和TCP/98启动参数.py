import sys
"""
sys.argv 获取参数列表
isdigit() 检测是否由数字组成
"""
params = sys.argv
# print(params)
# ['p98启动参数.py', '8080', 'aaa', 'bbb', '123']
# 判断参数为2才继续执行
if len(params) != 2:
    print("启动参数个数错误!")
    exit()
else:
    if not params[1].isdigit():
        print("参数错误")
        exit()
    else:
        print("是数字",end="\t")
        port = int(params[1])
        print(port)

"""
 enumerate() 会把列表组合成一个索引序列
"""


