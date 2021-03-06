# 打包framework

import os
import subprocess

def packageProject(projectname):
    # 打包archive
    archiveSimulator = "xcodebuild archive "+ "-workspace ADSuyiDev.xcworkspace"\
                       + " -scheme " + projectname\
                       + " -configuration Release " \
                       + "-destination \'generic/platform=iOS Simulator\' " \
                       + "-archivePath \'"+"archives/"+projectname+".framework-iphonesimulator.xcarchive\' SKIP_INSTALL=NO"
    archiveiPoneos = "xcodebuild archive "+"-workspace ADSuyiDev.xcworkspace" \
                       + " -scheme " + projectname\
                       + " -configuration Release " \
                       + "-destination \'generic/platform=iOS\' " \
                       + "-archivePath \'"+"archives/"+projectname+".framework-iphones.xcarchive\' SKIP_INSTALL=NO"

    outPutXcframework = "xcodebuild -create-xcframework "\
                         + "-framework \'archives/"+projectname+".framework-iphones.xcarchive/Products/Library/Frameworks/"+projectname +".framework\' "\
                         +"-framework \'archives/"+projectname+".framework-iphonesimulator.xcarchive/Products/Library/Frameworks/"+projectname +".framework\' "\
                         +"-output " +"release/"+projectname+ ".xcframework"

    os.system(archiveSimulator)
    os.system(archiveiPoneos)
    # 移除打包框架中不需要的文件
    os.system(
        "rm -rf archives/" + projectname + ".framework-" + "iphones.xcarchive/Products/Library/Frameworks/" + projectname + ".framework/_CodeSignature")
    os.system(
        "rm -rf archives/" + projectname + ".framework-" + "iphones.xcarchive/Products/Library/Frameworks/" + projectname + ".framework/Modules")
    os.system(
        "rm -rf archives/" + projectname + ".framework-" + "iphones.xcarchive/Products/Library/Frameworks/" + projectname + ".framework/Info.plist")
    os.system(
        "rm -rf archives/" + projectname + ".framework-" + "iphones.xcarchive/Products/Library/Frameworks/" + projectname + ".framework/PrivateHeaders")
    os.system(
        "rm -rf archives/" + projectname + ".framework-" + "iphones.xcarchive/Products/Library/Frameworks/" + projectname + ".framework/_CodeSignature")
    os.system(
        "rm -rf archives/" + projectname + ".framework-" + "iphones.xcarchive/Products/Library/Frameworks/" + projectname + ".framework/*.bundle")
    os.system(
        "rm -rf archives/" + projectname + ".framework-" + "iphonesimulator.xcarchive/Products/Library/Frameworks/" + projectname + ".framework/_CodeSignature")
    os.system(
        "rm -rf archives/" + projectname + ".framework-" + "iphonesimulator.xcarchive/Products/Library/Frameworks/" + projectname + ".framework/Modules")
    os.system(
        "rm -rf archives/" + projectname + ".framework-" + "iphonesimulator.xcarchive/Products/Library/Frameworks/" + projectname + ".framework/Info.plist")
    os.system(
        "rm -rf archives/" + projectname + ".framework-" + "iphonesimulator.xcarchive/Products/Library/Frameworks/" + projectname + ".framework/PrivateHeaders")
    os.system(
        "rm -rf archives/" + projectname + ".framework-" + "iphonesimulator.xcarchive/Products/Library/Frameworks/" + projectname + ".framework/_CodeSignature")
    os.system(
        "rm -rf archives/" + projectname + ".framework-" + "iphonesimulator.xcarchive/Products/Library/Frameworks/" + projectname + ".framework/*.bundle")
    os.system(outPutXcframework)

# 判断是否存在存储路径 并清空上次打包 批量打包只需清除一次
os.chdir("/Users/jishu/Desktop/ADSuyiDev")
if not os.path.exists("archives/"):
    os.makedirs("archives/")
archivesFiles = os.listdir("archives/")
for file in archivesFiles:
    os.system("rm -rf archives/"+file)
if not os.path.exists("release/"):
    os.makedirs("release/")
releaseFiles = os.listdir("release/")
for file in releaseFiles:
    os.system("rm -rf release/"+file)
packageProject("ADSuyiSDK")
packageProject("ADSuyiNetWork")

