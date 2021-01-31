import os
import subprocess

# 执行shell命令的三种方式
# 1、os.system("") 返回结果 0 执行成功
# shell1 = os.system("python3 --version")
# print(shell1)
# 2、os.popen("") 返回结果需要调用read或readline来读取
# shell2 = os.popen("python3 --version")
# print(shell2.read())
# print(shell2.readline())
# 3、subprocess.getoutput("") 返回结果为元组 状态码+命令输出
shell3 = subprocess.getoutput("python3 --version")
print(shell3)
shell4 = subprocess.getstatusoutput("python3 --help")
print("状态码："+str(shell4[0]))
print("执行输出:"+shell4[1])

