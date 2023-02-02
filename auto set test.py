str1='''# test {}
# {}
try:
    if <test here>:
        print("{}: "+bcolors.BOLD+bcolors.OKGREEN+"PASS"+bcolors.ENDC)
    else:
        print("{}: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)
except:
    print("{}: "+bcolors.BOLD+bcolors.FAIL+"FAIL"+bcolors.ENDC)

'''

go='''
len->长度
type->型类
super->超级
str->字符串
range->范围
object->对象
map->地图
list->列表
int->数字
float->小数
dict->字典
bytes->字节
bool->abc
True->真
False->假
Ellipsis->省略
None->空
tuple->元组
zip->打包
bytearray->字节数组
'''

color='''class bcolors:
    HEADER = '\\033[95m'
    OKBLUE = '\\033[94m'
    OKCYAN = '\\033[96m'
    OKGREEN = '\\033[92m'
    WARNING = '\\033[93m'
    FAIL = '\\033[91m'
    ENDC = '\\033[0m'
    BOLD = '\\033[1m'
    UNDERLINE = '\\033[4m
'''

def func(string:str):
    if string=='':
        return
    return string.split('->')

tmpout = list(map(func,go.split('\n')))
output=''#color
for i in tmpout:
    if i == None:continue
    before,after = i
    output+= str1.format(before,after,before,before,before)
with open("output.txt", "w") as f:
    f.write(output)