"""
主从配置
当主服务器收到消息后 立刻向从服务器发送消息，
同步从服务器，当主服务器停滞时候,其他服务器会立刻变为主服务器
以保证继续运行

由主服务器提供写入和更新，从服务器提供查询

mysql的服务器之间的主从同步是基于二进制日志机制的
"""