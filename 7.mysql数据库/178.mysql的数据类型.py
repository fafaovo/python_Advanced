"""
常用的:
整形
tinyint -128-127  unsigned 0-255    1个字节
int -21亿-21亿    unsigned 0-42亿    4个字节
浮点型
float 默认保留小数点后6位        4字节
double 默认保留小数点后16位      8字节
定义方式: float(M,D) M表示总数字的位数 D表示小数的位数
定点数
decimal(M,D) M表示总数字的位数(最大为55) D表示小数的位数
字符串
varchar 65535字节
text 64kb
为什么不用char呢 char占用你给的字节数 varchar占用你使用的字节数
存储数据经常变化用varchar
知道固定长度用char
尽量用varchar
枚举类型
enum 参考C中的枚举
语法定义 gender enum(值，值，值)
时间类型
m

"""