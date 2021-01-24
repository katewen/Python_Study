import re
import requests
from NetManager import *

# 网络请求
# 请求参数
# url = "http://y.webzcz.cn/api.php"
# para = {"types": "search", "count": 20, "source": "netease", "pages": 1, "name": "执迷不悟"}
# re = requests.post(url, data=para).json()
# musiclist = re
# for music in musiclist:
#     print(music)
# 网络请求数据
netmanager = NetManager()
# 搜索音乐
musiclist = netmanager.searchmusic("love",1)

# 返回数据写入桌面文件
musictext = open("/Users/erik/Desktop/music",mode="w+")
for music in  musiclist:
    print(music.name+music.artist[0])
    musictext.write(str(music.id)+" "+music.name+" "+music.artist[0]+" "+str(music.url_id)+"\n")
# 读取所写文件
musictext.read()

# 下载搜索结果音乐 并存储到桌面
music = musiclist[0]
musicurl = netmanager.dowloadmusci(music.id,music.source)
# 获取到音乐数据
musicget = requests.get(musicurl)
# 保存音乐路径
musicPath = "/Users/erik/Desktop/"+music.name+"-"+music.artist[0]+".mp3"
# 写入获取的文件 以二进制写入
with open(musicPath, 'wb') as file:
    for chunk in musicget.iter_content():
        file.write(chunk)



