# 自动进行pod导入

import os
import subprocess

noPodfile = "No `Podfile'"
complete = "Pod installation complete!"
notFind = "CocoaPods could not find compatible versions for pod"
updateFail = "couldn't be downloaded"

projectPath = input("请输入项目路径:")
# 切换到输入工作目录
os.chdir(projectPath)
# 执行pod intall
podShell = subprocess.getstatusoutput("pod install")
# 读取pod install命令输出
installRead = podShell[1]
# 判断是否pod成功多种情况
# 1、是否创建了podfile文件
if noPodfile in installRead:
    print("该路径下无podfile文件，请创建")
else:
    # 2、是否没找到库文件 执行pod repo update
    if notFind in installRead:
        againInput = 1
        while againInput == 1:
            print("执行pod repo update")
            updateShell = subprocess.getstatusoutput("pod repo update")
            updateRead = updateShell[1]
            print(updateRead)
            # 更新失败
            if updateFail in updateRead:
                print("pod repo update 执行失败")
                againInput = input("是否重试(0、取消 1、重试)：")
                continue
            # 更新成功
            else:
                againInput = 0
                print("执行pod install")
                podShell = subprocess.getstatusoutput("pod install")
    # pod install 是否成功
    if complete in podShell[1]:
        print("pod install成功")
    else:
        print("pod install失败，未知错误，详情查看输出")
        print(podShell[1])