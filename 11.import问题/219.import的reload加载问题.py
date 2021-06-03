# 参考C编译后，修改原模块内容并不会对已经编译好的程序产生影响
# import自带防止重复包含
# reload当你对模块进行修改时,刷新正在使用这个模块
# from importlib import reload
# reload(模块名)
"""
>>> import reload_text
>>> reload_text.test()
--------11--------
>>> reload_text.test()
--------11--------
>>> reload_text.test()
--------11--------
>>> reload
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reload' is not defined
>>> from importlib import reload
>>> reload(reload_text)
<module 'reload_text' from 'F:\\Class\\PythonNode\\进阶\\11.import问题\\reload_text.py'>
>>> reload_text.test()
--------11--------
--------11--------
--------11--------
--------11--------
--------11--------
--------11--------
>>>exit();
"""

