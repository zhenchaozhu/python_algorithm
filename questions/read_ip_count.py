# coding: utf-8
"""
    读取一个ip列表的日志文件,并返回每个ip出现的次数
"""

file_path = '../iplist.txt'

ip_map = {}
with open(file_path, 'r') as f:
    content = f.readlines()
    for data in content:
        data = data.strip()
        if data in ip_map:
            ip_map[data] += 1
        else:
            ip_map[data] = 1

print ip_map