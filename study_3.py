# os模块 文件目录操作
import os
import sys

# 文件路径
filePath = "/Users/erik/Desktop/python.txt"
#鉴权 文件是否存在
os.access(filePath,mode=os.F_OK)
# 文件是否可写入
os.access(filePath,mode=os.W_OK)
# 文件是否可读
os.access(filePath,mode=os.R_OK)
# 文件是否可执行
os.access(filePath,mode=os.X_OK)
# 查看当前目录
os.getcwd()
# 改变路径到filepath
os.chdir(filePath)
# 返回指定路径下的文件和目录名
os.listdir("/Users/erik/Desktop/")
# 删除一个文件
os.remove(filePath)
# 生成多级目录
os.makedirs()
# 创建一级目录
os.mkdir(filePath)
# 显示当前绝对路径
os.path.abspath()
# 链接目录和文件名 返回path/filename
os.path.join("path","filename")
# 将path分割成路径明和文件名
os.path.split(filePath)
# 返回当前父目录
os.path.dirname(filePath)
# 返回该路径下最后一个目录或者文件 如果路径以/结尾返回空值
os.path.basename(filePath)
# 判断路径是否是文件
os.path.isfile(filePath)
# 判断是否一个目录
os.path.isdir(filePath)
# 检测文件目录是否存在
os.path.exists(filePath)
# 执行命令 会阻塞进程 只返回命令执行结果 0成功
os.system("")
# 执行命令 不会阻塞 可以返回运行过程
os.popen("")