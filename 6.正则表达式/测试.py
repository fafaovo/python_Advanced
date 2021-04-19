import re
import random
result =re.match("\d?\d|100", str(random.randint(0, 100)))
if result:
    print(f"匹配成功{result.group()}")
else:
    print(f"匹配失败{result.group()}")

result = re.match("^\w{4,20}@(163|126|qq|sina)\.com$","1206180803@qq.com")
if result:
    print(f"匹配成功{result.group()}")
    print(f"提取子字符串{result.group(1)}")
else:
    print(f"匹配失败{result.group()}")