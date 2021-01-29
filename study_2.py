import re
import requests
from urllib import request
from urllib import parse
import json

file = open('/Users/jishu/Desktop/网易云逆向.rtf', mode='r')
file.read()
print(file.read())

# file2 = open('/Users/jishu/Desktop/python.txt', mode='x')
# file2.write('你是知道我的吧，哈哈哈哈哈')

file3 = open('/Users/jishu/Desktop/python.txt', mode='a+')
file3.write('shide ba sfasdfasdf')

re = request.urlopen('http://www.baidu.com')
content = re.read()
string = str(content, encoding='utf8')
if not content:
    print('请求失败')
else:
    file3.write(string)

paras = parse.urlencode({'types': 'search', 'count': 20, 'source': 'netease', 'pages': '1', 'name': '是想你的声音啊'})
paras = paras.encode('utf-8')
musicRequest = request.urlopen('http://y.webzcz.cn/api.php', data=paras)
print(musicRequest.read().decode('utf-8') + '\n')
# 返回搜索结果 列表 json转为python类型
musicList = musicRequest.read().decode('utf-8')
print(musicList)
