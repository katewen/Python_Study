
# 音乐类模型
class Music():
    # 构建方法
    def __init__(self,dic):
        # self.id = id
        # self.name = name
        # self.artist = artist
        # self.album = album
        # self.pic_id = pic_id
        # self.url_id = url_id
        # self.lyric_id = lyric_id
        # self.source = source
        self.id = dic["id"]
        self.name = dic["name"]
        self.artist = dic["artist"]
        self.album = dic["album"]
        self.pic_id = dic["pic_id"]
        self.url_id = dic["url_id"]
        self.lyric_id = dic["lyric_id"]
        self.source = dic["source"]
    # 自定义方法
    # def initwithdic(self,dic):
    #     self.id = dic["id"]
    #     self.name = dic["name"]
    #     self.artist = dic["artist"]
    #     self.album = dic["album"]
    #     self.pic_id = dic["pic_id"]
    #     self.url_id = dic["url_id"]
    #     self.lyric_id = dic["lyric_id"]
    #     self.source = dic["source"]
    #     return self