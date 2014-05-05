#! /usr/bin/env python
# encoding: UTF-8

# Copyright 2014 陈睿超<linuxer.sheep.0x@gmail.com>
# 本作品采用知识共享 署名-相同方式共享 4.0 国际 许可协议进行许可。
# 访问 http://creativecommons.org/licenses/by-sa/4.0/deed.zh 查看该许可协议。





# ==================== Introduction ====================
# 我是注释~~~
# Python等不少语言使用'#'作为注释的起始字符

exit()      # 执行exit()就可以立刻退出
            # 交互式模式下可以直接敲EOF，更方便。
            # 通常Ctrl-D表示EOF（但是这只是通常）

# 常识: “通常”不意味着“总是”、“最好”不意味着“必须”、……。下文中这类东西不再强调。

# 看到文件开头第一行了吗？这行直接背下来就行了。有兴趣的话可以阅读有关SHEBANG的
# 资料和有关exec(2)的资料。总之所有的Python代码开头最好都有这行。如果你的代码
# 中有任何非ASCII字符（例如中文）的话，第二行也是必需的。
#! /usr/bin/env python
# encoding: UTF-8

# 嫌无聊的话，我另外提供了一个实用例子，见bilibili.py。你可以直接运行它，看看
# 效果。





# ==================== I've got a calc! ====================
                            # To get you going, try these:
1+2*3-4
182739823 & 0xff            # 位运算
10/3                        # 整除
10.0/3                      # 浮点除法
10.0//3                     # 浮点数也可以整除哦

                            # Yeah! The good old C way... really?
# 1==2 || 3<4               # SyntaxError: invalid syntax
1==2 or 3<4                 # 应该使用and, or, not

2**10
2**3**2                     # 等同于 2**(3**2)

33**33                      # 自带高精~~~


# ==================== Cheap cheatsheet ====================
print 'Hello, yyb!'
myname = raw_input()            # getline
print 'Hello, ' + myname

date = '2014-02-31'
time = '13:00'
print date + ' ' + time         # 注意Python 2的print是保留字而不是函数。
                                # 这个坑爹的特性在Python 3中被纠正过来了。

a, b = 1, 2                     # 平行赋值
a, b = b, a                     # 相当于C/C++的swap(a,b)

if a > b:                       # 不少语句都以:结束，初学时容易忘记
    print 'you win!'

def mymin(a, b):                # 嗯，来点函数
    if a < b:                   # 如你所见, Python没有大括号，也没有begin-end
        return a                # 这种简洁的通过缩进划分语句块的方法被称为
    else:                       # off-side rule
        return b

def shortmin(a, b):             # Python没有 a ? b : c 这种写法
    return a if a < b else b    # 因此使用 b if a else c （其实我很想吐槽...）

cnt = 0
while cnt < 5:
    cnt += 1                    # Python是没有++和--的
    print cnt
                                # 咦？没有反应？请再输入一个空行。
                                # 因为Python依赖缩进来确定语句块，所以
                                # 需要一个空行来告诉它“这段已经结束了”
                                # （当然，这个规定仅适用于交互式模式）

                                # 我们最喜欢的for语句
for i in ['Koyomi', 'Karen', 'Tsukihi']:
    print 'Araragi ' + i

                                # 要枚举一串数字，可以使用range
for i in range(0, 5):           # range是左闭右开的
    print i+1                   # 有兴趣的话可以试一下range(0, 10, 3)

def no_response():              # 语句块中至少要有一句话，怎么办？
    pass                        # pass可以拿来充数。这个语句什么都不做，只是
                                # 占位置而已

if no_response(): pass          # 若语句块中只有一句话的话，可以写在同一行


# ==================== Gotchas ====================
expression = input()            # try "1+2" and... wat.
print "result:", expression     # print多个值的时候，Python会用空格把它们隔开






# ==================== Literals ====================
'foo'
"foo"

"He said: \"y~~y~~b~~~~\""  # Ruby等语言的程序员可能会感到吃惊:
'foo\'bar"baz'              # Python中单双引号没什么大区别。
r"NO line feed!\n"          # 或许你想要的是这个（r表示raw）

"""foo""" or '''foo'''
u"Our beloved Unicode"

True
False
None


# ==================== 常用类型 ====================
# 几乎所有语言都有这么几种类型: number, string, list, map, boolean

                                # 你可以使用type(v)来查询对象的类型
type(1)                         # int
type(.3)                        # float (.3这种写法在C中也可以用哦)
type('foo')                     # str
type(True)                      # bool
type(type(1))                   # type -> 这是一个对象哦
type(2**1000)                   # long -> 哈，这是高精度整数的类型

float(3)                        # 强转（实际上是调用了构造器）
zero = float()                  # 没错，这就是新建对象的方法
print zero


                                # 数字真没劲，来看看字符串吧

loli = 'Shinobu'                # is用于判断两个变量/字面量是否是同一个对象
'Shinobu' is loli               # True! LOL
'Shinobu' is 'Shinobu'          # Python中任何字符串只存在一份拷贝



# 这就是Python中的“数组”了。
harem = ['Hitagi', 'Mayoi']
harem.append('Shinobu')         # 追加一个元素
harem += ['Karen', 'Tsukihi']   # 追加一整串

print "My harem: ", harem       # 哇，好难看
                                # 这样就好多了（其实我很想吐槽join的用法）
print "My harem:", ', '.join(harem)

len(harem)                      # 总共有这么多个元素

                                # in用于判断一个对象是否属于另一个对象
                                # 别跟 for ... in 搞混了哦
'Hitagi' in harem               # sure it's True
'Meme' in harem                 # Yoooooooooooo

                                # 好玩的来了
                                # Python的列表是0-based的
                                # 负数表示从后往前数（-1表示最后一个）
harem[3]    # 'Karen'
harem[-1]   # 'Tsukihi'
                                # 这个叫slicing。老样子，左闭右开区间。
                                # 顺便打下广告，Ruby的slicing真是超好用
harem[3:5]  # ['Karen', 'Tsukihi']

                                # 可以省略起点或终点，自行脑补吧
harem[:2]   # ['Hitagi', 'Mayoi']
harem[3:]   # ['Karen', 'Tsukihi']

harem[:]                        # deep copy一份（这是一个常用的技巧）

harem[4:-1] # ['Karen']


[i**2 for i in range(0,10)]     # 这叫list comprehension。很方便吧？
                                # 不过不要滥用哦
nums = list(range(0,10))        # 简单一点的工作用类型转换就可以了
                                # 看，比list comprehension清爽多了吧？

harem += nums                   # list中可以同时存储不同类型的对象
del harem[-1]                   # harem中混进了奇怪的东西...
del harem[-5:-2]                # 用del删掉它们
harem[-6:] = []                 # 或者也可以replace成空列表



# ==================== 模型 ====================
# Python是一门动态类型语言。变量的类型是不固定的。
a = 1
a = 'ssssss'
a = True

# 动态类型不等于弱类型。试试看这个:
7 < '6'         # True

# 不了解原理的话，很多东西会非常难以理解。在Python、Ruby等动态语言中，“变量”和
# “对象”是不同的概念。Python中的变量是没有值的。变量本身只是一个引用，引用了一
# 个内存中的对象。所以 a = 'ssssss' 的时候，我们只不过是让a这个变量去引用一个
# string对象而已。习惯了这种思维方式之后，很多问题都不是问题了。就算你有一个3MB
# 的数组也可以放心地赋值给一堆变量，因为变量赋值仅仅是修改引用，并没有复制任何
# 对象。（当然，这里我们略过了一些细节，例如数字的存储）

# 回顾一下list的使用:
a = [1]
b = a
a.append(2)             # 现在b是[1, 2]
print b                 # a和b引用的是同一个对象。a.append(2)的时候修改的是对象
                        # 而不是变量的值。
a += [3, 4]             # 现在b是[1, 2, 3, 4]
print b                 # 说明在Python中，+=是修改对象而不是修改变量
                        # 也就是说， a += b 和 a = a + b 是不一样的

a = []                  # 来点好玩的
b = [a]
a.append(b)             # 遍历类似这样的列表的时候千万要小心哦
print a

# ==================== 继续玩列表 ====================
h = harem               # ['Hitagi', 'Mayoi', 'Shinobu', 'Karen', 'Tsukihi']
h.sort()
print h                 # ['Hitagi', 'Karen', 'Mayoi', 'Shinobu', 'Tsukihi']
print harem             # 糟了，连harem也改掉了。只好重来一遍了
                        # 现在你知道为什么要用 harem[:] 了吧？

harem = ['Hitagi', 'Mayoi', 'Shinobu', 'Karen', 'Tsukihi']
h = harem[:]            # 这回我们学乖了
h.sort()
print harem             # 这回没有把旧的数据改掉

                        # 其实还有更简单的方法
h = sorted(harem)       # sorted不会修改harem的内容

h = harem[:].sort()     # 要注意哦，这种写法是错误的。sort的返回值是None。
                        # 对于Ruby程序员来说，实在是很反直觉。不过或许Python
                        # 这么设计也有它的道理吧。

g = harem[0]            # 'Hitagi'
g[2:]                   # 'tagi'
# g[2:]='ragana'        # 咦？报错了？这是因为Python的字符串是不可修改的

g = g[:2] + 'ragana'    # 虽然字符串对象是不可修改的，但是我们可以引用一个新的
                        # 字符串

g.split('i')            # ['H', 'tag', '']
' abc x 123   '.split() # ['abc', 'x', '123']


# TODO dict
# TODO bytes tuple















harem2 = set(harem)             # To be fair, we use an unordered set,
                                # so that nobody comes first.







# TODO The damn help()
# TODO docstring
# TODO dir(foo), foo.__doc__
# TODO class
#           class suite中发生的事情（new context、bind names in the context）
#           instantiate时发生了什么（创建新对象，类似Ruby的OpenStruct、Lua的
#                                    table或Javascript的object）
#           method（foo.bar()相当于MyClass.bar(foo)）
#                   说白了，Python中的class完全就是语法糖。本质上Python更接近
#                   prototype-based语言（与Javascript对比一下即可看出）。
#           继承、etc

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

# TODO import (from as)  math

# TODO pip? pydoc
# TODO pdb pycompile
# TODO Scons
