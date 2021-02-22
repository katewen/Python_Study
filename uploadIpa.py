
#自动打包上传ipa
import os
import subprocess
import sys

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

os.system(cleanShell)
os.system(archiveShell)
os.system(exportShell)
os.system("open "+archivePath)
# subprocess.getoutput(cleanShell)
# subprocess.getoutput(archiveShell)
# subprocess.getoutput(exportShell)

isUpload = input("打包IPA完成，是否上传App Store Connect:")
if isUpload == "yes":
    username = input("请输入Apple Id：")
    appPw = input("请输入App专用密码非AppID密码：")
    # 上传ipa
    uploadIpa = "xcrun altool --upload-app -f " + archivePath + "/" + projectName + ".ipa" + " -u " + username + " -p "+appPw
    os.system(uploadIpa)
else:
    sys.exit(0)

