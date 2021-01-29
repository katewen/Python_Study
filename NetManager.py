import json
import requests
from Music import *
# 网络请求类
class NetManager():
    def __init__(self):
        print(self)
    # 搜索
    def searchmusic(self,musicname,pageno):
        url = "http://y.webzcz.cn/api.php"
        para = {"types": "search", "count": 10, "source": "netease", "pages": pageno, "name": musicname}
        musics = requests.post(url, data=para).json()
        musicslist = list()
        for musicDic in musics:
            music = Music(musicDic)
            musicslist.append(music)
        return musicslist
    # 下载
    def dowloadmusci(self,musicid,source):
        url = "http://y.webzcz.cn/api.php"
        para = {"types": "url", "id": musicid, "source": source}
        musicurl = requests.post(url, data=para).json()
        return musicurl["url"]
