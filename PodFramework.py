# 打包framework

import os
def packageProject(projectname):
    filePath = "/Users/jishu/Desktop/SuyiSDK/ADSuyiCode/"
    for files in os.listdir(filePath):
        # 判断当前是否是一个目录 且遍历文件夹内名称一致文件夹 切换工作目录
        if os.path.isdir(filePath+files) and (files.lower() == projectname.lower()):
            print("当前files="+files)
            # 切换工作目录至匹配目录中
            os.chdir(filePath+files)
            break
        else:
            print("当前files=下一个"+files)
            continue
    # 推送到私有库
    pushPrivateShell = "pod repo push http://121.41.108.203/adsuyi_code/adsuyicode_private.git " + projectname + ".podspec --verbose --allow-warnings"
    # 打包
    archiveShell = "pod package "+projectname+".podspec "+"--spec-sources=http://121.41.108.203/adsuyi_code/adsuyicode_private.git,https://github.com/CocoaPods/Specs.git --no-mangle --exclude-deps"
    # 如果是主SDK依赖库 需要先推送到私有库 避免打包失败
    if projectname == "ADSuyiNetWork" or projectname == "ADSuyiLocationManager"\
        or projectname == "ADMobGenDeviceInfo" or projectname == "ADSuyiKit"\
        or projectname == "ADSuyiSDK":
        os.system(pushPrivateShell)
    os.system(archiveShell)
# 先打包kit 无其他依赖库 并上传私有库
packageProject("ADSuyiKit")
# packageProject("ADSuyiLocationManager")
# packageProject("ADSuyiNetwork")
# packageProject("ADMobGenDeviceInfo")
# packageProject("ADSuyiSDK")