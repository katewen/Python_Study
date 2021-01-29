
#导出bugly符号表并上传
import os

buglyId = "4a44bfe394"
buglykey = "b9730fc1-a376-4922-b6bf-7c1d0a24ee1b"
packagename = "cn.ecook.ecook"
vesion = input("请输入版本号：")
# java -jar buglySymboliOS.jar -i /Users/batman/Desktop/test.app.dSYM -u -i
# d 900012345 -key abcdefghijk -package com.batman.demo -version 2.3.1
# bugly 官方命令
shell = "java -jar /Users/jishu/bin/buglySymboliOS.jar -i /Users/jishu/Desktop/eCook.app.dSYM" + " -u" + " -id " + buglyId + " -key " + buglykey + " -package " + packagename + " -version " + vesion
os.system(shell)
print("上传符号表成功")
