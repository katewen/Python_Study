# 错误处理和异常
try:
    x = int(input("请输入一个数字："))
except ValueError:
    print("请输入数字")

try:
    y = int(input("输入数字："))
except ValueError:
    print("请输入数字")
else:
    print("输入正确")

try:
    z = int(input("请输入数字："))
except ValueError:
    print("输入有误")
else:
    print("输入正确执行")
finally:
    print("判断异常结束执行")

# 正则表达式
import re
# pattern 正则表达式 str 匹配的字符串 flags 标志位 返回匹配对象 完全匹配
re.match("www","www.baidu.com",flags=0)
# 扫描整个字符串并返回第一个成功的匹配
re.search("www","www.baidu.com")
# 替换 repl : 替换的字符串，也可为一个函数 count替换次数 默认0 全部替换 flags 匹配模式
re.sub("www","hhh","www.baidu.com",0,1)
# 编译一个表达式 供match和search使用
pattern = re.compile(r'\d+')
pattern.match("12333323",2,5)
# 返回匹配字符串列表
re.findall("www","wwww.baidu.com.wwwerki")
# 返回匹配字符串迭代器类型
re.finditer("www","www.www.www")
# 照能够匹配的子串将字符串分割后返回列表 maxsplit 分割次数，默认0无限制
re.split("www","www.erik.erik.ww.www")