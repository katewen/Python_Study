#导出bugly符号表并上传 笔趣阁
import os

buglyId = "03e28925fd"
buglykey = "eec1c494-0307-4932-8583-02d84fca270e"
packagename = "cn.xbqg.reader"
vesion = input("请输入版本号：")
# java -jar buglySymboliOS.jar -i /Users/batman/Desktop/test.app.dSYM -u -i
# d 900012345 -key abcdefghijk -package com.batman.demo -version 2.3.1
# bugly 官方命令
shell = "java -jar /Users/jishu/bin/buglySymboliOS.jar -i /Users/jishu/Desktop/hongyanreader.app.dSYM" + " -u" + " -id " + buglyId + " -key " + buglykey + " -package " + packagename + " -version " + vesion
os.system(shell)
print("上传符号表成功")