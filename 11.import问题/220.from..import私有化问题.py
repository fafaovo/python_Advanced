# _变量名 使用 from xxx import * 不能被导入
from module1 import *

print(name)
# age 此时是私有变量，无法获取到
