
#自动打包上传ipa 待完善
import os

projectPath = input("请输入项目绝对路径：")
projectName = input("请输入项目名称：")
archivePath = input("请输入archive和ipa文件导出路径：")
configPath = input("请输入配置文件路径：")
# clean
cleanShell = "xcodebuild clean -workspace "+projectPath + " -scheme " + projectName + " -configuration Release"
# archive
archiveShell = "xcodebuild clean -workspace "+projectPath + " -scheme " + projectName + " -archivePath " + archivePath + "/" + projectName + ".xcarchive"
# ipa 需要配置打包plist文件 选择 adhoc App store
exportShell = "xcodebuild -exportArchive -archivePath " + archivePath + "/" + projectName + ".xcarchive" + " -exportPath " + archivePath + " -exportOptionsPlist " + configPath
# 上传ipa

#上传bugly符号表



