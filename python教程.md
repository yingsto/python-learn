# python教程

## Python简介
Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。
Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。

- Python 是一种解释型语言： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
- Python 是交互式语言： 这意味着，您可以在一个 Python 提示符 >>> 后直接执行代码。
- Python 是面向对象语言: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。
- Python 是初学者的语言：Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

Python 特点

- 1.易于学习：Python有相对较少的关键字，结构简单，和一个明确定义的语法，学习起来更加简单。
- 2.易于阅读：Python代码定义的更清晰。
- 3.易于维护：Python的成功在于它的源代码是相当容易维护的。
- 4.一个广泛的标准库：Python的最大的优势之一是丰富的库，跨平台的，在UNIX，Windows和Macintosh兼容很好。
- 5.互动模式：互动模式的支持，您可以从终端输入执行代码并获得结果的语言，互动的测试和调试代码片断。
- 6.可移植：基于其开放源代码的特性，Python已经被移植（也就是使其工作）到许多平台。
- 7.可扩展：如果你需要一段运行很快的关键代码，或者是想要编写一些不愿开放的算法，你可以使用C或C++完成那部分程序，然后从你的Python程序中调用。
- 8.数据库：Python提供所有主要的商业数据库的接口。
- 9.GUI编程：Python支持GUI可以创建和移植到许多系统调用。
- 10.可嵌入: 你可以将Python嵌入到C/C++程序，让你的程序的用户获得"脚本化"的能力。
- 11.胶水语言：用来连接其他语言编写的软件组件或模块

python不能直接访问硬件，也不能编译为本地代码运行。
### python安装
[https://www.runoob.com/python3/python3-install.html](https://www.runoob.com/python3/python3-install.html)

- 源码地址：[https://www.python.org/downloads/source/](https://www.python.org/downloads/source/)
- 选择合适的源码压缩包进行安装
```
tar -zxvf Python-3.6.1.tgz
cd Python-3.6.1
./configure --prefix=/home/nizhou.zn/bin/
make && make install
python3 -V
```

- 环境变量设置：PATH=xxx
- python环境变量：
  - PYTHONPATH：PYTHONPATH是Python搜索路径，默认我们import的模块都会从PYTHONPATH里面寻找。
  - PYTHONSTARTUP：Python启动后，先寻找PYTHONSTARTUP环境变量，然后执行此变量指定的文件中的代码。
  - PYTHONCASEOK：加入PYTHONCASEOK的环境变量, 就会使python导入模块的时候不区分大小写.
  - PYTHONHOME：另一种模块搜索路径。它通常内嵌于的PYTHONSTARTUP或PYTHONPATH目录中，使得两个模块库更容易切换。
### python运行

- 交互式解释器
  - python命令行参数
    - -d 在解析是显示调试信息
    - -O 生成优化代码.pyo文件
    - -S 启动是不引入查找python路径的位置
    - -V 输出python版本好
    - -c cmd 执行python脚本，并将运行结果作用cmd字符串
    - file 在给定的python文件执行python脚本
- 命令行脚本
- 集成开发环境（IDE)：pycharm
### python3基础语法

- 编码
  - 默认情况下，python3源码文件以UTF-8 coding编码，所有字符串都是unicode(16位)字符串，也可以为源码文件指定不同的编码。
```
# -*- coding: cp-1252 -*-
或
# coding=utf-8
```

- 标识符
  - 第一个字符必须是字母表中字母或下划线 _ 。
  - 标识符的其他的部分由字母、数字和下划线组成。
  - 标识符对大小写敏感。
  - 在Python 3中，可以用中文作为变量名，非ASCII标识符也是允许的了。
- python保留字
```
import keyword
keyword.kwlist
```

- 注释：
  - 单行：#
  - 多行：'''和"""
- 行与缩进
  - python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
  - 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
- 多行语句：
  - 反斜杠(\)
  - 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
- 数字类型：int，bool，float，complex(1+2j)
- 字符串：
  - python中单引号和双引号使用完全相同。
  - 使用三引号('''或""")可以指定一个多行字符串。
  - 转义符 '\'
  - 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。 如 r"this is a line with \n" 则\n会显示，并不是换行。
  - 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
  - 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
  - Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
  - Python中的字符串不能改变。
  - Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
  - 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
- 空行：
  - 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
  - 空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
  - 记住：空行也是程序代码的一部分。
- 等待用户输入:input()
- 同一行显示多条语句：使用分号(;)分隔
- 多个语句构成代码组
- print输出
  - print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""；print(x, end="")
- import与import from
```
import somemodule
from somemodule import somefunction
from somemodule import firstfunc, secondfunc
form somemodule import *
```

- python命令行参数：python -h
## 第一部分 基础
### 1.1.基本数据类型

- python中的变量不需要声明，每个变量在使用前都必须赋值，变量赋值后才会被创建；
- 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。在python中变量没有类型
- 多个变量赋值：a = b = c = 1
- 标准数据类型：number，string，list，tuple，set，dictionary
  - 不可变的：number，string，tuple
  - 可变：list，set，dictionary
#### 数字（number）

- int，float，bool，complex
  - python3不再区分整数和长整数，都可以是长整数
  - 不同进制：二进制：0b或者0B前缀，八进制0o或者0O前缀，16进制0x或者0X前缀
    - 可以用16进制和8进制表示整数：number = 0xa0f； number =0o37；
  - python只支持双精度浮点类型
  - 不同表示：小数表示，科学计数法；33.6； 3.36e1
  - 布尔类型：True和False
- 内置type()函数可以用来查询变量所指的对象类型
- 可以用isinstance来判断
- type与isinstance区别
  - type()不会认为子类是一种父类类型。
  - isinstance()会认为子类是一种父类类型。
- 数值运算
  - 数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
    - // 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
  - 在混合计算时，Python会把整型转换成为浮点数；
  - Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型；
  - 在交互模式中，最后被输出的表达式结果被赋值给变量 _；
- 数学函数： [reference](https://www.runoob.com/python3/python3-number.html)
  - abs(x), ceil(x), exp(x), fabs(x), floor(x), log(x), log10(x), max(x1,x2,...), min(x1,x2,...), modf(x), pow(x,y), round(x [,n]) sqrt(x)
- 随机函数
  - choice(seq)，randrange([start,] stop [,step]), random(), seed([x]), shuffle(list), uniform(x,y)
- 三角函数
- 数学常量
#### 字符串（string)

- Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
- 字符串截取方法：变量[头下标:尾下标]
- 加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，与之结合的数字为复制的次数。
- Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r；
- 另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。
- 注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
- python中的字符采用unicode编码\u0048 -> H
- 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
- python字符串格式化
  - Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
  - 在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
  - 格式化符号控制符：%c/s/d/u/o/x/X/f/e/E/g/G/p <[reference](https://www.runoob.com/python3/python3-string.html)>
  - 控制符复位占位符索引或占位符后面，之间用冒号隔开。例如{1:d}表示索引1的占位符格式参数是10进制
  - 格式化字符串的函数：str.format()
```
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
```

- python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符;
- f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法；
  - f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去；
- 字符串内建函数
  - 字符串查找str.find(sub[, start[, end]])
| 序号 | 方法及描述 |
| :--- | :--- |
| 1 | [capitalize()](https://www.runoob.com/python3/python3-string-capitalize.html)
将字符串的第一个字符转换为大写 |
| 2 | [center(width, fillchar)](https://www.runoob.com/python3/python3-string-center.html)返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。 |
| 3 | [count(str, beg= 0,end=len(string))](https://www.runoob.com/python3/python3-string-count.html)返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数 |
| 4 | [bytes.decode(encoding="utf-8", errors="strict")](https://www.runoob.com/python3/python3-string-decode.html)Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。 |
| 5 | [encode(encoding='UTF-8',errors='strict')](https://www.runoob.com/python3/python3-string-encode.html)以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace' |
| 6 | [endswith(suffix, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-endswith.html)
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False. |
| 7 | [expandtabs(tabsize=8)](https://www.runoob.com/python3/python3-string-expandtabs.html)把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。 |
| 8 | [find(str, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-find.html)检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1 |
| 9 | [index(str, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-index.html)跟find()方法一样，只不过如果str不在字符串中会报一个异常. |
| 10 | [isalnum()](https://www.runoob.com/python3/python3-string-isalnum.html)如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False |
| 11 | [isalpha()](https://www.runoob.com/python3/python3-string-isalpha.html)如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False |
| 12 | [isdigit()](https://www.runoob.com/python3/python3-string-isdigit.html)如果字符串只包含数字则返回 True 否则返回 False.. |
| 13 | [islower()](https://www.runoob.com/python3/python3-string-islower.html)如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False |
| 14 | [isnumeric()](https://www.runoob.com/python3/python3-string-isnumeric.html)如果字符串中只包含数字字符，则返回 True，否则返回 False |
| 15 | [isspace()](https://www.runoob.com/python3/python3-string-isspace.html)如果字符串中只包含空白，则返回 True，否则返回 False. |
| 16 | [istitle()](https://www.runoob.com/python3/python3-string-istitle.html)如果字符串是标题化的(见 title())则返回 True，否则返回 False |
| 17 | [isupper()](https://www.runoob.com/python3/python3-string-isupper.html)如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False |
| 18 | [join(seq)](https://www.runoob.com/python3/python3-string-join.html)以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串 |
| 19 | [len(string)](https://www.runoob.com/python3/python3-string-len.html)返回字符串长度 |
| 20 | [ljust(width[, fillchar])](https://www.runoob.com/python3/python3-string-ljust.html)返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。 |
| 21 | [lower()](https://www.runoob.com/python3/python3-string-lower.html)转换字符串中所有大写字符为小写. |
| 22 | [lstrip()](https://www.runoob.com/python3/python3-string-lstrip.html)截掉字符串左边的空格或指定字符。 |
| 23 | [maketrans()](https://www.runoob.com/python3/python3-string-maketrans.html)创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。 |
| 24 | [max(str)](https://www.runoob.com/python3/python3-string-max.html)返回字符串 str 中最大的字母。 |
| 25 | [min(str)](https://www.runoob.com/python3/python3-string-min.html)返回字符串 str 中最小的字母。 |
| 26 | [replace(old, new [, max])](https://www.runoob.com/python3/python3-string-replace.html)把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。 |
| 27 | [rfind(str, beg=0,end=len(string))](https://www.runoob.com/python3/python3-string-rfind.html)类似于 find()函数，不过是从右边开始查找. |
| 28 | [rindex( str, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-rindex.html)类似于 index()，不过是从右边开始. |
| 29 | [rjust(width,[, fillchar])](https://www.runoob.com/python3/python3-string-rjust.html)返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串 |
| 30 | [rstrip()](https://www.runoob.com/python3/python3-string-rstrip.html)删除字符串字符串末尾的空格. |
| 31 | [split(str="", num=string.count(str))](https://www.runoob.com/python3/python3-string-split.html)num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串 |
| 32 | [splitlines([keepends])](https://www.runoob.com/python3/python3-string-splitlines.html)按照行('\\r', '\\r\\n', \\n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。 |
| 33 | [startswith(substr, beg=0,end=len(string))](https://www.runoob.com/python3/python3-string-startswith.html)检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。 |
| 34 | [strip([chars])](https://www.runoob.com/python3/python3-string-strip.html)在字符串上执行 lstrip()和 rstrip() |
| 35 | [swapcase()](https://www.runoob.com/python3/python3-string-swapcase.html)将字符串中大写转换为小写，小写转换为大写 |
| 36 | [title()](https://www.runoob.com/python3/python3-string-title.html)返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle()) |
| 37 | [translate(table, deletechars="")](https://www.runoob.com/python3/python3-string-translate.html)根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中 |
| 38 | [upper()](https://www.runoob.com/python3/python3-string-upper.html)转换字符串中的小写字母为大写 |
| 39 | [zfill (width)](https://www.runoob.com/python3/python3-string-zfill.html)返回长度为 width 的字符串，原字符串右对齐，前面填充0 |
| 40 | [isdecimal()](https://www.runoob.com/python3/python3-string-isdecimal.html)检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。 |

#### 数组结构

- 序列、集合和元组
- 元组：有序，不可以修改
- 列表：有序，可修改
- 集合：无序，可修改
- 字典
#### 列表（list）

- List（列表） 是 Python 中使用最频繁的数据类型。列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。列表是写在方括号 [] 之间、用逗号分隔开的元素列表。和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
- 列表截取方法：变量[头下标:尾下标]；
- 加号 + 是列表连接运算符，星号 * 是重复操作；
- 与Python字符串不一样的是，列表中的元素是可以改变的；
- list函数：len(), max(), min(), list(seq)
- List内置了有很多方法，例如 append()、pop() 等等
| 序号 | 方法 |
| :--- | :--- |
| 1 | [list.append(obj)](https://www.runoob.com/python3/python3-att-list-append.html) 在列表末尾添加新的对象 |
| 2 | [list.count(obj)](https://www.runoob.com/python3/python3-att-list-count.html) 统计某个元素在列表中出现的次数 |
| 3 | [list.extend(seq)](https://www.runoob.com/python3/python3-att-list-extend.html) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） |
| 4 | [list.index(obj)](https://www.runoob.com/python3/python3-att-list-index.html) 从列表中找出某个值第一个匹配项的索引位置 |
| 5 | [list.insert(index, obj)](https://www.runoob.com/python3/python3-att-list-insert.html) 将对象插入列表 |
| 6 | [list.pop([index=-1])](https://www.runoob.com/python3/python3-att-list-pop.html) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
| 7 | [list.remove(obj)](https://www.runoob.com/python3/python3-att-list-remove.html) 移除列表中某个值的第一个匹配项 |
| 8 | [list.reverse()](https://www.runoob.com/python3/python3-att-list-reverse.html) 反向列表中元素 |
| 9 | [list.sort( key=None, reverse=False)](https://www.runoob.com/python3/python3-att-list-sort.html) 对原列表进行排序 |
| 10 | [list.clear()](https://www.runoob.com/python3/python3-att-list-clear.html) 清空列表 |
| 11 | [list.copy()](https://www.runoob.com/python3/python3-att-list-copy.html) 复制列表 |

- 将列表当作堆栈使用
  - append()
  - pop()
- 将列表当作队列使用
  - 在队列第一加入元素和取出元素，效率不高；
- 推导式：数据结构作为输入，经过过滤、计算等处理，最后输出另一种数据结构；
- 列表推导式：
```
语法结构：
n_list = [x**2 for x in range(10) if x % 2 == 0]
           |       |       |          |
       输出表达式 元素变量 输入序列    条件语句
```

  - 提供了从序列创建列表的简单途径
  - 条件语句可以省略，也可以有多个；
  - 每个列表推导式都在 for 之后跟一个表达式，然后有零到多个for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
```
>>> vec = [2, 4, 6]
>>> [3*x for x in vec]
[6, 12, 18]
>>> [3*x for x in vec if x > 3]
[12, 18]
>>> [3*x for x in vec if x < 2]
[]
>>> vec1 = [2, 4, 6]
>>> vec2 = [4, 3, -9]
>>> [x*y for x in vec1 for y in vec2]
[8, 6, -18, 16, 12, -36, 24, 18, -54]
>>> [x+y for x in vec1 for y in vec2]
[6, 5, -7, 8, 7, -5, 10, 9, -3]
>>> [vec1[i]*vec2[i] for i in range(len(vec1))]
[8, 12, -54]
```

- 嵌套列表解析
```
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
#### 元组（tuple）

- 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开；
- 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
- 元组中的元素类型也可以不相同；
- 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取；
- 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表
- 元组内置函数：len(), min(), max(), tuple(iterable)
#### 集合（set）

- 集合（set）是由一个或数个形态各异的大小整体组成的，是一个无序的不重复元素序列，构成集合的事物或对象称作元素或是成员。
- 基本功能是进行成员关系测试和删除重复元素。
- 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
- 集合基本操作：
  - 添加元素：s.add(x)，s.update(x)；x可以是多个
  - 删除元素：s.remove(x)，s.discard(x), s.pop()
  - 计算集合元素个数：len(s)
  - 清空：s.clear()
  - 判断元素是否存在：x in s
- 内置方法
| 方法 | 描述 |
| :--- | :--- |
| [add()](https://www.runoob.com/python3/ref-set-add.html) | 为集合添加元素 |
| [clear()](https://www.runoob.com/python3/ref-set-clear.html) | 移除集合中的所有元素 |
| [copy()](https://www.runoob.com/python3/ref-set-copy.html) | 拷贝一个集合 |
| [difference()](https://www.runoob.com/python3/ref-set-difference.html) | 返回多个集合的差集 |
| [difference_update()](https://www.runoob.com/python3/ref-set-difference_update.html) | 移除集合中的元素，该元素在指定的集合也存在。 |
| [discard()](https://www.runoob.com/python3/ref-set-discard.html) | 删除集合中指定的元素 |
| [intersection()](https://www.runoob.com/python3/ref-set-intersection.html) | 返回集合的交集 |
| [intersection_update()](https://www.runoob.com/python3/ref-set-intersection_update.html) | 返回集合的交集。 |
| [isdisjoint()](https://www.runoob.com/python3/ref-set-isdisjoint.html) | 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。 |
| [issubset()](https://www.runoob.com/python3/ref-set-issubset.html) | 判断指定集合是否为该方法参数集合的子集。 |
| [issuperset()](https://www.runoob.com/python3/ref-set-issuperset.html) | 判断该方法的参数集合是否为指定集合的子集 |
| [pop()](https://www.runoob.com/python3/ref-set-pop.html) | 随机移除元素 |
| [remove()](https://www.runoob.com/python3/ref-set-remove.html) | 移除指定元素 |
| [symmetric_difference()](https://www.runoob.com/python3/ref-set-symmetric_difference.html) | 返回两个集合中不重复的元素集合。 |
| [symmetric_difference_update()](https://www.runoob.com/python3/ref-set-symmetric_difference_update.html) | 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。 |
| [union()](https://www.runoob.com/python3/ref-set-union.html) | 返回两个集合的并集 |
| [update()](https://www.runoob.com/python3/ref-set-update.html) | 给集合添加元素 |

#### 字典（dictionary）

- 字典（dictionary）是Python中另一个非常有用的内置数据类型。列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取;
- 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合；
- 键(key)必须使用不可变类型；
- 在同一个字典中，键(key)必须是唯一的；
- 构造函数 dict() 可以直接从键值对序列中构建字典；
  - 接收不同的输入格式
- 访问字典里的值：dict[key]
- 修改字典：向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对；
- 删除字典元素：
  - 显示删除一个字典用del命令, del dict[key]
  - dict_name.clear()
- 字典的内置函数：len(dict), str(dict), type()
- 字典类型也有一些内置方法，例如clear()、keys()、values()；
| 序号 | 函数及描述 |
| :--- | :--- |
| 1 | [radiansdict.clear()](https://www.runoob.com/python3/python3-att-dictionary-clear.html) 删除字典内所有元素 |
| 2 | [radiansdict.copy()](https://www.runoob.com/python3/python3-att-dictionary-copy.html) 返回一个字典的浅复制 |
| 3 | [radiansdict.fromkeys()](https://www.runoob.com/python3/python3-att-dictionary-fromkeys.html) 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值 |
| 4 | [radiansdict.get(key, default=None)](https://www.runoob.com/python3/python3-att-dictionary-get.html) 返回指定键的值，如果值不在字典中返回default值 |
| 5 | [key in dict](https://www.runoob.com/python3/python3-att-dictionary-in.html) 如果键在字典dict里返回true，否则返回false |
| 6 | [radiansdict.items()](https://www.runoob.com/python3/python3-att-dictionary-items.html) 以列表返回可遍历的(键, 值) 元组数组 |
| 7 | [radiansdict.keys()](https://www.runoob.com/python3/python3-att-dictionary-keys.html) 返回一个迭代器，可以使用 list() 来转换为列表 |
| 8 | [radiansdict.setdefault(key, default=None)](https://www.runoob.com/python3/python3-att-dictionary-setdefault.html) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default |
| 9 | [radiansdict.update(dict2)](https://www.runoob.com/python3/python3-att-dictionary-update.html) 把字典dict2的键/值对更新到dict里 |
| 10 | [radiansdict.values()](https://www.runoob.com/python3/python3-att-dictionary-values.html) 返回一个迭代器，可以使用 list() 来转换为列表 |
| 11 | [pop(key[,default])](https://www.runoob.com/python3/python3-att-dictionary-pop.html) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。 |
| 12 | [popitem()](https://www.runoob.com/python3/python3-att-dictionary-popitem.html) 随机返回并删除字典中的最后一对键和值。 |

#### 数据类型转换
| 函数 | 描述 |
| :--- | :--- |
| [int(x [,base])](https://www.runoob.com/python3/python-func-int.html) | 将x转换为一个整数 |
| [float(x)](https://www.runoob.com/python3/python-func-float.html) | 将x转换到一个浮点数 |
| [complex(real [,imag])](https://www.runoob.com/python3/python-func-complex.html) | 创建一个复数 |
| [str(x)](https://www.runoob.com/python3/python-func-str.html) | 将对象 x 转换为字符串 |
| [repr(x)](https://www.runoob.com/python3/python-func-repr.html) | 将对象 x 转换为表达式字符串 |
| [eval(str)](https://www.runoob.com/python3/python-func-eval.html) | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| [tuple(s)](https://www.runoob.com/python3/python3-func-tuple.html) | 将序列 s 转换为一个元组 |
| [list(s)](https://www.runoob.com/python3/python3-att-list-list.html) | 将序列 s 转换为一个列表 |
| [set(s)](https://www.runoob.com/python3/python-func-set.html) | 转换为可变集合 |
| [dict(d)](https://www.runoob.com/python3/python-func-dict.html) | 创建一个字典。d 必须是一个 (key, value)元组序列。 |
| [frozenset(s)](https://www.runoob.com/python3/python-func-frozenset.html) | 转换为不可变集合 |
| [chr(x)](https://www.runoob.com/python3/python-func-chr.html) | 将一个整数转换为一个字符 |
| [ord(x)](https://www.runoob.com/python3/python-func-ord.html) | 将一个字符转换为它的整数值 |
| [hex(x)](https://www.runoob.com/python3/python-func-hex.html) | 将一个整数转换为一个十六进制字符串 |
| [oct(x)](https://www.runoob.com/python3/python-func-oct.html) | 将一个整数转换为一个八进制字符串 |

#### 遍历技巧

- 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来；
- 在序列遍历时，索引位置和对应值可以使用 enumerate() ；
- 同时遍历两个或更多的序列，可以使用 zip() 组合；
- 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
- 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值；
```
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)

>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)

>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))

>>> for i in reversed(range(1, 10, 2)):
...     print(i)

>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
```
### 1.2.运算符
#### 算术运算符

- +， -， *，/，%，**， //
#### 比较（关系）运算符

- ==, !=, >, <, >=, <=
#### 赋值运算符

- =, +=, *=, ...
- :=，海象运算符，可在表达式内部为变量赋值。Python3.8 版本新增运算符。
#### 逻辑运算符

- and, or, not
#### 位运算符

- &, |, ^, ~, <<, >>
#### 成员运算符

- in, not in
#### 身份运算符

- is, is 是判断两个标识符是不是引用自一个对象，x is y等效id(x) == id(y), id()函数用于获取对象内存地址
- is not
#### 运算符优先级

- [reference](https://www.runoob.com/python3/python3-basic-operators.html)
### 1.3.语句
#### 条件控制

- if语句
```
if xx：
	xx
elif xx：
	xx
else：
	xx
```
#### 条件表达式
表达式1 if 条件 else 表达式2：条件真为表达式1，否则为表达式2
#### 循环语句

- for
  - rang()函数
- while
- break：跳出循环
- continue：跳出本次循环的该轮
- pass：不做任何事，一般用作占位语句
```
for var in <sequence>:
	xx
else:
	xx
 
while xx:
	xx
else:
	xx
```
#### 输入输出
[https://www.runoob.com/python3/python3-inputoutput.html](https://www.runoob.com/python3/python3-inputoutput.html)

- python输出
  - 有2两种输出值的方式：表达式语句和print()函数，第3种是使用文件对象的write()，标准输出文件可以用sys.stdout引用
  - 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
  - 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
    - str()： 函数返回一个用户易读的表达形式。
    - repr()： 产生一个解释器易读的表达形式。
- 读取键盘输入：input()
- 读写文件：open(filename, mode)
  - f.read(): 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
  - f.readline()：会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
  - f.readlines()：返回该文件中包含的所有行。
  - f.write(): f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
  - f.tell(): 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
  - f.seek(): 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
  - f.close()
| 模式 | 描述 |
| :--- | :--- |
| r | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| rb | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。 |
| r+ | 打开一个文件用于读写。文件指针将会放在文件的开头。 |
| rb+ | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 |
| w | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| w+ | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+ | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| a | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+ | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+ | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |




| 模式 | r | r+ | w | w+ | a | a+ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 读 | + | + |  | + |  | + |
| 写 |  | + | + | + | + | + |
| 创建 |  |  | + | + | + | + |
| 覆盖 |  |  | + | + |  |  |
| 指针在开始 | + | + | + | + |  |  |
| 指针在结尾 |  |  |  |  | + | + |

- pickle模块
  - python的pickle模块实现了基本的数据序列和反序列化。
  - 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
  - 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
  - pickle.dump(obj, file, [,protocol])
```
import pprint, pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
```
### 1.4.迭代器与生成器
#### 迭代器

- 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
- 迭代器是一个可以记住遍历的位置的对象。
- 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
- 迭代器有两个基本的方法：iter() 和 next()。
- 字符串，列表或元组对象都可用于创建迭代器。
```
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
#for遍历
for x in it:
    print (x, end=" ")
#next()函数
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()
```

- 创建一个迭代器：把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
```
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
 
for x in myiter:
  print(x)
```
#### 生成器

- 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
- 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
- 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
- 调用一个生成器函数，返回的是一个迭代器对象。
```
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
```
### 1.5.函数
python函数很灵活，在模块中、但在类之外的定义，即函数，其作用域是当前模块；在别的函数中定义，即嵌套函数；在类中定义，即方法。
#### 定义函数

- 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
- 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号起始，并且缩进。
- return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
```
def 函数名 (参数列表):
	函数体
```
#### 函数调用

- 参数传递
  - 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
  - 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响；
  - python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
- 参数
  - 必须参数：必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
  - 关键字参数：关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
  - 默认参数：调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值；
  - 不定长参数：可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。
    - 加了星号 ***** 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
    - 还有一种就是参数带两个星号 ****，**加了两个星号 ****** 的参数会以字典的形式导入。
    - 如果*单独出现，后面参数必须用关键字传入；
```
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
def functionname([formal_args,] **var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]

例子：
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
# 调用printinfo 函数
printinfo( 70, 60, 50 )

# 可写函数说明
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)
```
#### 返回值

- 多返回值函数
  - 使用元组返回多个值；
- return语句
  - return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
#### 函数变量作用域

- 全局和局部
#### 匿名函数

- python 使用 lambda 来创建匿名函数。
- 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
  - lambda 只是一个表达式，函数体比 def 简单很多。
  - lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
  - lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
  - 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
```
lambda [arg1 [,arg2,.....argn]]:expression
例子：
sum = lambda arg1, arg2: arg1 + arg2
```
### 1.6.模块
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
#### 模块导入
import语句

- 当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
- 搜索路径是一个解释器会先进行搜索的所有目录的列表。搜索路径被存储在sys模块中的path变量。可以在脚本中修改sys.path来引入一些不在搜索路径中的模块。

from … import 语句

- Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间

from … import * 语句

- 把一个模块的所有内容全都导入到当前的命名空间也是可行的。
#### __name__属性

- 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
- 说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。
```
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
```
#### dir()函数

- 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回。
#### 标准模块

- Python 本身带着一些标准的模块库；
- 有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统级调用也没问题。
#### 包

- 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
- 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
- 就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。
- 这样不同的作者都可以提供 NumPy 模块，或者是 Python 图形库。
- 不妨假设你想设计一套统一处理声音文件和数据的模块（或者称之为一个"包"）。
- 在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
- 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
- 最简单情况是放一个空file：__init__.py.当然这个文件中也可以包含一些初始化代码或者为 __all__变量赋值。用户可以每次只导入一个包里面的特定模块;
### 1.7.OS文件/目录方法

- os 模块提供了非常丰富的方法用来处理文件和目录。

[https://www.runoob.com/python3/python3-os-file-methods.html](https://www.runoob.com/python3/python3-os-file-methods.html)
### 1.8.错误和异常
python有两种错误容易辨认：语法错误和异常
python assert断言用于判断一个表达式，在表达式条件为false的时候会触发异常。
![image.png](https://intranetproxy.alipay.com/skylark/lark/0/2020/png/45340/1590131445312-653dabc1-3d6f-4d57-b115-3c0f3af71e89.png#align=left&display=inline&height=112&margin=%5Bobject%20Object%5D&name=image.png&originHeight=224&originWidth=610&size=82936&status=done&style=none&width=305)
#### 异常处理

- try/except：异常捕捉可以使用try/except语句
  - 工作方式
    - 首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。
    - 如果没有异常发生，忽略 except 子句，try 子句执行后结束。
    - 如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
    - 如果一个异常没有与任何的 excep 匹配，那么这个异常将会传递给上层的 try 中。
  - 一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行；
  - 处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常；
  - 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组；
```
try:
	执行代码
except：
	发送异常是执行的代码
例子：
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
```

- try/except...else：
  - try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。else 子句将在 try 子句没有发生任何异常的时候执行。
- try-finally语句
  - try-finally 语句无论是否发生异常都将执行最后的代码。
```
try:
	执行代码
except：
	发送异常是执行的代码
else:
	没有异常是执行的代码
finally：
	不管有没有异常都会执行的代码
```

- 释放资源：try-except语句会占用一些资源，如打开文件，网络连接等，这些资源不能通过python的垃圾回收期回收，需要程序员释放，可以使用finally代码块或者with as自动资源管理
#### 抛出异常

- python使用raise语句抛出一个指定的异常。raise [Exception [, args [, traceback]]]
  - raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
  - 如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
```
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
```
#### 用户自定义异常

- 可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承。
### 1.9.面向对象
####  简介

- 类：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
- 方法：类中定义的函数
- 类变量：类变量在整个实例化对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
- 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
- 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
- 局部变量：定义在方法中的变量，只作用于当前实例的类。
- 实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
- 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
- 实例化：创建一个类的实例，类的具体对象。
- 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。
Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
对象可以包含任意数量和类型的数据。
#### 类的定义

- class classname：xxx
- 类实例化后，可以使用其属性，通过类名访问其属性
#### 类对象

- 类对象支持两种操作：实例化和属性引用；
- 属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name；
- 类对象创建后，类命名空间中所有的命名都是有效属性名；
- 一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用；
- self代表类的实例，而非类；
- 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self；
#### 类的方法

- 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
#### 继承

- class DerivedClassName(BaseClassName1): 
- 多继承
  - class DerivedClassName(Base1, Base2, Base3):
  - 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索即方法在子类中未找到时，从左到右查找父类中是否包含方法。
- 方法重写
  - 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法；
- 子类继承父类构造函数：
  - 如果在子类中需要父类的构造方法就需要显式地调用父类的构造方法，或者不重写父类的构造方法。
  - 子类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__。
  - 如果重写了__init__ 时，要继承父类的构造方法，可以使用 super 关键字：
```
super(子类，self).__init__(参数1，参数2，....)
//另外一种经典方法
父类名称.__init__(self,参数1，参数2，...)
```
#### 类属性和方法

- 类的私有属性：
  - __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
- 类的方法：
  - 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
  - self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。
- 类的是有方法：
  - __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。
- 类的专有方法：
  - __init__ : 构造函数，在生成对象时调用
  - __del__ : 析构函数，释放对象时使用
  - __repr__ : 打印，转换
  - __setitem__ : 按照索引赋值
  - __getitem__: 按照索引获取值
  - __len__: 获得长度
  - __cmp__: 比较运算
  - __call__: 函数调用
  - __add__: 加运算
  - __sub__: 减运算
  - __mul__: 乘运算
  - __truediv__: 除运算
  - __mod__: 求余运算
  - __pow__: 乘方
- 运算符重载
  - Python同样支持运算符重载，我们可以对类的专有方法进行重载；
### 1.10.命名空间和作用域
#### 命名空间

- 一般有3中命令空间
  - 内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
  - 全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
  - 局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）
- 命名空间查找顺序：局部->全局-》内置
- 命名空间的生命周期：
  - 命名空间的生命周期取决于对象的作用域，如果对象执行完成，则该命名空间的生命周期就结束。因此，我们无法从外部命名空间访问内部命名空间的对象。
#### 作用域

- 作用域就是一个 Python 程序可以直接访问命名空间的正文区域。
- Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
- 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
  - L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
  - E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
  - G（Global）：当前脚本的最外层，比如当前模块的全局变量。
  - B（Built-in）： 包含了内建的变量/关键字等，最后被搜索；
- 内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量
```
import builtins
dir(builtins)
```

- Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问。
- 全局变量和局部变量
- global和nonlocal关键字：
  - 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字。
  - 修改全局变量用global声明；
  - 要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字
### 1.11.标准库概览

- 操作系统接口：os，
  - 建议使用import os，不用from os import *，会导致内置的函数的冲突；
- 文件通配：glob
- 命令行参数：sys.argv
- 错误输出重定向和程序终止：
  - sys.stdin/stdout/stderr,
  - sys.exit()
- 字符串正则匹配：re
- 数学：math
- 访问互联网：urllib
- 日期和时间：datetime
- 数据压缩：zlib，gzip，bz2，zipfile以及tarfile
- 性能度量：timeit
- 测试模块：
  - doctest
  - unittest
- logging日志模块：python的内置模块 <[reference](https://www.cnblogs.com/yyds/p/6901864.html)>
  - 日志级别：debug、info、warning、error、critical
  - 日志信息格式化
  - 日志重定位
  - 使用配置文件
```
import logging
logging.basicConfig(level=logging.ERROR)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

logger = logging.getLogger(__name__)
logger.debug("debug")
```
### 1.12. 实例case
[https://www.runoob.com/python3/python3-examples.html](https://www.runoob.com/python3/python3-examples.html)
## 第二部分 高级
### 2.1.正则表达式
[https://www.runoob.com/python3/python3-reg-expressions.html](https://www.runoob.com/python3/python3-reg-expressions.html)
#### 正则表达式字符串

- 元字符：用来藐视其他字符的特殊字符
| 字符 | 描述 |
| :--- | :--- |
| \\ | 转义符，表示转义 |
| . | 表示任意一个字符 |
| + | 表示重复一次或多次 |
| * | 表示重复零次或多次 |
| ？ | 表示重复零次或一次 |
| &#124; | 选择符合，表示"或关系" |
| { } | 定义量词 |
| [ ] | 定义字符类 |
| ( ) | 定义分组 |
| ^ | 可以表示取反，或匹配一行的开始 |
| $ | 匹配一行的结束 |

- 字符转义
- 在正则表达式中本身包含和反斜杆等特殊字符，推荐使用python中原始字符串表达式r'xxx'
#### 字符类

- 正则表达式可以使用字符类，一个字符类定义一组字符，其中任一字符出现在输入字符串中即匹配成功。注意每次匹配只能匹配字符类的一个字符。[ ]
- 预定义字符类
| 实例 | 描述 |
| :--- | :--- |
| . | 匹配任意一个字符 |
| \\ | 匹配反斜杆\\字符 |
| \n | 匹配换行 |
| \r | 匹配回车 |
| \f | 匹配一个换页符 |
| \t | 匹配一个水平制表符 |
| \v | 匹配一个垂直制表符 |
| \s | 匹配一个空格符 |
| \S | 等价于[^\s] |
| \d | 匹配一个数字 |
| \D | 等价于[^\d] |
| \w | 匹配任何语言的单词字符 |
| \W | 等价于[^\w] |

#### 量词
| 实例 | 描述 |
| :--- | :--- |
| ? | 出现零次或一次 |
| * | 出现零次或多次 |
| + | 出现一次或多次 |
| {n} | 出现n次 |
| {n,m} | 至少出现n次但不超过m次 |
| {n,} | 至少出现n次 |

- 贪婪量词和懒惰量词：默认是贪婪，尽可能多匹配，如果要用懒惰量词，后面加上'?'
#### 分组

- 一对小括号中，分组或者子表达式
- 分组使用
- 分组命名
- 反向引用分组
  - p = r'<([\w]+)>.*</\1>'
- 非捕获分组
#### re模块
### 2.2.Python CGI编程
CGI 目前由NCSA维护，NCSA定义CGI如下：
CGI(Common Gateway Interface),通用网关接口,它是一段程序,运行在服务器上如：HTTP服务器，提供同客户端HTML页面的接口。
### 2.3.函数式编程
#### 三大基础函数

- 过滤：filter(function, iterable)
- 映射：map(function, iterable)
- 聚合：reduce(function, iterable[, initializer])
```
users = ['Tony', 'Tom', 'Ben', 'Alex']
users_filter = filter(lambda u: u.startswitch('T'), users)
print(list(users_filter))
users_map = map(lambda u: u.lower(), users)
print(list(users_map))
from functools import reduce
a = (1, 2, 3, 4)
a_reduce = reduce(lambda acc, i: acc + i, a, 2) #12
```




Reference：
1.廖雪峰python教程：[https://www.liaoxuefeng.com/wiki/1016959663602400](https://www.liaoxuefeng.com/wiki/1016959663602400)
2.菜鸟教程python3教程：[https://www.runoob.com/python3/python3-tutorial.html](https://www.runoob.com/python3/python3-tutorial.html)
3.Python 官网：[https://www.python.org/](https://www.python.org/)
4.Python文档下载地址：[https://www.python.org/doc/](https://www.python.org/doc/)
5.Python标准库：[https://docs.python.org/3/library/index.html](https://docs.python.org/3/library/index.html)
6.Python HOWTODO：[https://docs.python.org/3/howto/index.html](https://docs.python.org/3/howto/index.html)
7.Python教程：[https://docs.python.org/3/tutorial/index.html](https://docs.python.org/3/tutorial/index.html)
8.PEP规范：[https://www.python.org/dev/peps/](https://www.python.org/dev/peps/)
