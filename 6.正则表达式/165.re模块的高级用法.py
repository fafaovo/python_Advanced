"""
match   匹配满足开头的正则表达式
search  匹配满足条件的正则表达式
findall 搜索全部满足条件的，返回列表

sub(正则表达式,新的内容,要替换的字符串)
按照查找字符串并且替换成指定的内容
返回替换后的字符串

split(正則表達式,代拆分的字符串) 返回值是一个列表

"""
import re
result = re.match("\d+", "阅读次数9999,转发次数9999")
result1 = re.search("\d+", "阅读次数9999,转发次数9997")
result2 = re.findall("\d+", "阅读次数9999,转发次数6666")
result3 = re.sub("\d+", "0", "阅读次数9999,转发次数6666")
result4 = re.split(":| ", "info:hello@163.com zhangsan liwei")
if result:
    print(f"match匹配成功,结果是:{result.group()}")
else:
    print("match匹配失败")
if result1:
    print(f"search匹配成功,结果是:{result1.group()}")
else:
    print("search匹配失败")
if result2:
    print(f"findall匹配成功,结果是:{result2}")
else:
    print("findall匹配失败")

print(f"sub替换后的内容:{result3}")
print(result4)