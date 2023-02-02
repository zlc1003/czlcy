class bcolors:
    HEADER = '\033[91m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# test print
try:
    输出(f"print: {bcolors.BOLD}{bcolors.OKGREEN}PASS{bcolors.ENDC}")
except:
    print(f"print: {bcolors.BOLD}{bcolors.FAIL}FAIL{bcolors.ENDC}")


# test max
try:
    if 最大([1,2,3,4,5,6,7,8,9,0,11,12,13,141,51]) == 141:
        print(f"max: {bcolors.BOLD}{bcolors.OKGREEN}PASS{bcolors.ENDC}")
    else:
        print(f"max: {bcolors.BOLD}{bcolors.FAIL}FAIL{bcolors.ENDC}")
except:
    print(f"max: {bcolors.BOLD}{bcolors.FAIL}FAIL{bcolors.ENDC}")

# test max
try:
    if 最小([1,2,3,4,5,6,7,8,9,0,11,12,13,141,51,-102]) == -102:
        print(f"min: {bcolors.BOLD}{bcolors.OKGREEN}PASS{bcolors.ENDC}")
    else:
        print(f"min: {bcolors.BOLD}{bcolors.FAIL}FAIL{bcolors.ENDC}")
except:
    print(f"min: {bcolors.BOLD}{bcolors.FAIL}FAIL{bcolors.ENDC}")

try:
    if 最小([1,2,3,4,5,6,7,8,9,0,11,12,13,141,51,-102]) == -102:
        print(f"min: {bcolors.BOLD}{bcolors.OKGREEN}PASS{bcolors.ENDC}")
    else:
        print(f"min: {bcolors.BOLD}{bcolors.FAIL}FAIL{bcolors.ENDC}")
except:
    print(f"min: {bcolors.BOLD}{bcolors.FAIL}FAIL{bcolors.ENDC}")

# test next
# 下一个 | 下个
try:
    abc=iter([1,2,3])
    下个(abc)
    if 下个(abc)==2 and 下一个(abc)==3:
        print("next: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("next: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("next: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test iter
# 重复
try:
    abc=重复([1,2,3])
    next(abc)
    if next(abc)==2:
        print("iter: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("iter: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("iter: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test eval
# 计算
try:
    if 计算("1+1")==2:
        print("eval: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("eval: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("eval: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test exec
# 运行
try:
    运行("def foo():return 'ok'")
    if foo() == "ok":
        print("exec: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
        del foo
    else:
        print("exec: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("exec: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test any
# 任何
try:
    if 任何([True, False, False]) == True:
        print("any: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("any: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("any: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test bin
# 二进制
try:
    if 二进制(64)=='0b1000000':
        print("bin: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("bin: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("bin: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test abs
# 绝对值
try:
    if 绝对值(-98) == 98 == 绝对值(98):
        print("abs: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("abs: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("abs: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test chr
# ascii码
try:
    if ascii码(97) == "a":
        print("chr: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("chr: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("chr: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test input
# 输入
try:
    if str(输入) == '<built-in function 输入>':
        print("input: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("input: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("input: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test len
# 长度
try:
    if 长度("12345678")==8:
        print("len: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("len: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("len: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test type
# 型类
try:
    if 型类("123")==str:
        print("type: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("type: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("type: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test super
# 超级
print("super: "+bcolors.BOLD+"\033[47m"+"SKIP"+bcolors.ENDC)

# test str
# 字符串
try:
    if 字符串(123)=="123":
        print("str: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("str: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("str: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test range
# 范围
try:
    if list(范围(3))==[0,1,2]:
        print("range: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("range: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("range: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test object
# 对象
try:
    if str(对象)=="<class 'object'>":
        print("object: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("object: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("object: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test map
# 地图
try:
    if list(地图(int,["1","2","2345"])) == [1,2,2345]:
        print("map: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("map: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("map: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test list
# 列表
try:
    if 列表("123")==['1', '2', '3']:
        print("list: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("list: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("list: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test int
# 数字
try:
    if (数字("123")+1)==124:
        print("int: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("int: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("int: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test float
# 小数
try:
    if (小数("12.3")+1.1)==13.4:
        print("float: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("float: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("float: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test dict
# 字典
try:
    if 字典() == {}:
        print("dict: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("dict: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("dict: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test bytes
# 字节
try:
    if 字节 == bytes:
        print("bytes: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("bytes: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("bytes: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test bool
# 布尔值
try:
    if 布尔值 == bool:
        print("bool: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("bool: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("bool: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test True
# 真
try:
    if 真:
        print("True: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("True: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("True: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test False
# 假
try:
    if not 假:
        print("False: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("False: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("False: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test Ellipsis
# 省略
try:
    if 省略 == Ellipsis:
        print("Ellipsis: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("Ellipsis: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("Ellipsis: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test None
# 空
try:
    if 空 == None:
        print("None: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("None: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("None: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test tuple
# 元组
try:
    if 元组(list("12345")) == ("1","2","3","4","5"):
        print("tuple: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("tuple: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("tuple: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test zip
# 打包
try:
    if list(打包((1,2),(3,4))) == [(1,3),(2,4)]:
        print("zip: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("zip: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("zip: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

# test bytearray
# 字节数组
try:
    if 字节数组 == bytearray:
        print("bytearray: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("bytearray: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("bytearray: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

