# 音乐下载器
import re
import requests
from NetManager import *

def searchmusic(musicname,pageno):
    # 网络请求数据
    netmanager = NetManager()
    # 搜索音乐
    musiclist = netmanager.searchmusic(musicname, pageno)
    # 打印搜索结果
    index = 0
    for music in musiclist:
        index += 1
        artistname = " - "
        for artist in music.artist:
            artistname = artistname + artist + ","
        artistname = artistname[:-1]
        print(str(index) + "、" + music.name + artistname)
    # 下一页
    print("11、下一页")
    return musiclist

def downloadmusic(downloadpath,musicurl):
    # 获取到音乐数据
    musicget = requests.get(musicurl)
    artistname = ""
    for artist in music.artist:
        artistname = artistname + artist + ","
    # 删除最后一位
    artistname = artistname[:-1]
    # 保存音乐路径
    musicPath = downloadpath + music.name + "-" + artistname + ".mp3"
    # 写入获取的文件 以二进制写入
    with open(musicPath, 'wb') as file:
        print("downloading")
        for chunk in musicget.iter_content():
            file.write(chunk)
        print("下载音乐完成")


if __name__ == '__main__':
    pageno = 1

    netmanager = NetManager()
    # 监听键盘输入
    inputmusicname = input("请输入音乐名：")
    musiclist = searchmusic(inputmusicname,pageno)
    selected = input("请选择：")
    while selected == "11":
        pageno += 1
        musiclist = searchmusic(inputmusicname,pageno)
        selected = input("请选择：")
    else:
        # 下载搜索结果音乐 并存储到桌面
        while int(selected)>=11 or int(selected) <0 :
            selected = input("请重新选择:")
            continue
        else:
            music = musiclist[int(selected) - 1]
            musicurl = netmanager.dowloadmusci(music.id, music.source)
            downloadmusic("/Users/jishu/Desktop/", musicurl)
# # 返回数据写入桌面文件
# musictext = open("/Users/erik/Desktop/music",mode="w+")
# for music in  musiclist:
#     print(music.name+music.artist[0])
#     musictext.write(str(music.id)+" "+music.name+" "+music.artist[0]+" "+str(music.url_id)+"\n")
# # 读取所写文件
# musictext.read()