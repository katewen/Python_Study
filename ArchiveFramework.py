# 打包framework

import os
import subprocess

def packageProject(projectname):
    # 判断是否存在存储路径 并清空上次打包
    os.chdir("/Users/erik/Desktop/SuyiSDK/ADSuyiCode/adsuyibaidu/Example")
    if not os.path.exists("../archives/"):
        os.makedirs("../archives/")
    archivesFiles = os.listdir("../archives/")
    for file in archivesFiles:
        os.remove("../archives/"+file)
    if not os.path.exists("../release/"):
        os.makedirs("../release/")
    releaseFiles = os.listdir("../release/")
    for file in releaseFiles:
        os.remove("../release/"+file)
    # os.chdir("/Users/erik/Desktop/SuyiSDK/ADSuyiCode/adsuyibu")
    # 打包archive
    archiveSimulator = "xcodebuild archive "+ " -workspace ADSuyiBaidu.xcworkspace"\
                       + " -scheme " + projectname+"-Example"\
                       + " -configuration Release " \
                       + "-destination \'generic/platform=iOS Simulator\' " \
                       + "-archivePath \'"+"../archives/"+projectname+".framework-iphonesimulator.xcarchive\' SKIP_INSTALL=NO"
    archiveiPoneos = "xcodebuild archive -project "+projectname+".xcodeproj" \
                       + " -scheme " + projectname\
                       + " -configuration Release " \
                       + "-destination \'generic/platform=iOS\' " \
                       + "-archivePath \'"+"./archives/"+projectname+".framework-iphones.xcarchive\' SKIP_INSTALL=NO"

    outPutXcframework = "xcodebuild -create-xcframework "\
                         + "-framework \'./archives/"+projectname+".framework-iphones.xcarchive/Products/Library/Frameworks/"+projectname +".framework\' "\
                         +"-framework \'./archives/"+projectname+".framework-iphonesimulator.xcarchive/Products/Library/Frameworks/"+projectname +".framework\' "\
                         +"-output " +"./release/"+projectname+ ".xcframework"
    os.system(archiveSimulator)
    # os.system(archiveiPoneos)
    # os.system(outPutXcframework)

packageProject("ADSuyiBaidu")