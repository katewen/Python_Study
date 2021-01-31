
#打包bugly符号表并上传
import os
# 网厨buglyID
buglyId = "4a44bfe394"
# 网厨bugly key
buglykey = "b9730fc1-a376-4922-b6bf-7c1d0a24ee1b"
# 网厨包名
packagename = "cn.ecook.ecook"
# 符号表对应版本号
vesion = input("请输入版本号(须加build，Eg:16.1.8.1)：")
dsymFile = input("请输入符号表文件绝对路径：")
# java -jar buglySymboliOS.jar -i /Users/batman/Desktop/test.app.dSYM -u -i
# d 900012345 -key abcdefghijk -package com.batman.demo -version 2.3.1
# bugly 官方命令
shell = "java -jar /Users/jishu/bin/buglySymboliOS.jar -i " + dsymFile + " -u" + " -id " + buglyId + " -key " + buglykey + " -package " + packagename + " -version " + vesion
os.system(shell)
print("上传bugly符号表成功")
