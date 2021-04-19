"""
re 正则表达式模块
re.match(pattern,string,flags=0)
pattern :正则表达式
string : 要匹配的字符串
falgs : 匹配模式

匹配成功会返回一个match object对象:
group() 返回匹配到的字符串
start() 返回匹配开始的位置
end() 返回匹配结束的位置
span() 返回一个元组包含匹配(开始,结束)的位置
"""
import re
# 1. 通过match 方法验证正则
result = re.match("^[0-9a-zA-Z]{4,20}@[0-9a-zA-Z]{2,5}\.com$", "hello@163.com")
if result:
    print(f"匹配成功,匹配到的字符串为:{result.group()}")
else:
    print("匹配失败")