import sys

# 添加环境变量路径
sys.path.append("F:\\Class\\PythonNode")  # 末尾
sys.path.insert(0, "F:\\Class\\PythonNode")  # 开头

print("python模块的搜索路径,系统环境变量")
for i in sys.path:
    print(i)
