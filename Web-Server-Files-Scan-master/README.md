### 主要用此项目练习使用python3的argparse模块和threading模块

### 由于经常碰到bak、swp、git、ds_store等文件泄露漏洞，于是添加了一些字典可以扫描出来是否存在这些漏洞；可以扩充字典来提升扫描性能

使用方法(usage)

    python scan.py [-h] [-u U] [-n N]
    
---

以下内容同步到了博客：http://www.gtfly.top/2019/02/24/python-服务器目录扫描工具/#more

### argparse模块

argparse库是python标准库中用来处理命令行参数的库


以下代码均保存在a.py文件中

---

### 创建解析器

第一个程序

``` python    
import argparse

# 创建ArgumentParser对象
# 该对象将包含将命令行解析为python数据类型所需的所有信息
parser = argparse.ArgumentParser(description='This is a test', epilog='It is end')

# 解析参数
parser.parse_args()    
```

打开cmd，执行：

	python a.py -h

输出：

	usage: a.py [-h]
	
	This is a test
	
	optional arguments:
	  -h, --help  show this help message and exit
	
	It is end


argparse.ArgumentParser（）方法参数：

- prog=None  程序名，若想更改usage后出现的a.py，可使用此参数

- description=None  help时显示的开始文字

- epilog=None  help时显示的结尾文字

- parents=[]  若与其他参数的一些内容一样，可以继承

- formatter_class=argparse.HelpFormatter  自定义帮助信息的格式

- prefix_chars='-'  命令的前缀，默认是‘-'

- fromfile_prefix_chars=None  命令行参数从文件中读取

- argument_default=None  设置一个全局的选项缺省值，一般每个选项单独设置

- conflict_handler='error'  定义两个add_argument中添加的选项名字发生冲突时怎么处理，默认处理是抛出异常

- add_help=True  是否增加-h/--help选项，默认是True

### 添加参数

- 位置参数(positional arguments):默认，程序根据参数出现的位置确定
- 可选参数(optional arguments):程序已提前定义好的参数，不一定需要

ArgumentParser通过调用add_argument()方法来填充有关程序参数的信息；parse_args()调用时会存储和使用此信息；parse_args()运行时，会用'-'来判断是否为可选参数

---

添加位置参数

``` python     
import argparse

parser = argparse.ArgumentParser(description='Output what you input')

# 添加了位置参数Output
parser.add_argument('Output')
args = parser.parse_args()
print(args.Output)     
```

打开cmd，输入

	python a.py 2333

输出

	2333

---

添加可选参数

可以通过一个'-'来指定短参数，如-h；还可通过'--'来指定的长参数，如--help；可同时指定短、长参数

``` python    
import argparse

parser = argparse.ArgumentParser(description='Output what you input')

# 添加了可选参数Output
parser.add_argument('-Output', '--Output')
args = parser.parse_args()
print(args.Output)    
```

打开cmd，输入

	python a.py -h

输出
	
	usage: a.py [-h] [-Output OUTPUT]
	
	Output what you input
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -Output OUTPUT, --Output OUTPUT

则接着输入

	python a.py -Output 2333

输出

	2333

而输入

	python a.py 2333

会输出报错信息
	
	usage: a.py [-h] [-Output OUTPUT]
	a.py: error: unrecognized arguments: 2333

原因是没有添加位置参数

---

add_argument()参数信息：

- action：此参数不存在时默认值为store，存储参数的值，其他值：
	- store_const: 值存放在const中
	- store_true(store_false): 值存为true(false)
	- append: 存为列表
	- append_const: 存为列表，会根据const关键参数进行添加
	- count: 统计参数出现的次数
	- help: help信息
	- version: 版本信息
- nargs: 参数的数量
	- *: 任意多个
	- +: 一个或更多
	- ?: 首先从命令行获得参数，若没有从const获得，然后从default获得
- const: 保存一个常量
- default: 如果命令行中没有出现这个参数，则使用的默认值
- type: 参数类型；默认的参数类型为str
- required: 是否必选
- dest: 自定义属性名称
- metavar: 参数的名字，在显示帮助信息时显示
- choices: 可供选择的值；值为列表或迭代器


---

计算范围内数字的平方

``` python    
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-square', '--square', type=int, choices=range(2, 4), help='Input X and Output X^2')
args = parser.parse_args()
print(args.square**2)   
```

打开cmd，输入

	python a.py -square 1

输出报错信息

    usage: a.py [-h] [-square {2,3}]
    a.py: error: argument -square/--square: invalid choice: 1 (choose from 2, 3)

原因是参数没有在range(2,4)，即[2,3]的范围

输入

	python a.py -square 3

输出

	9

---

功能： 默认将数字从大到小排序；使用参数可以求数字列最大值、最小值

``` python       
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('sorts', type=int, nargs='+', help='sort the number from big to small')
parser.add_argument('-max', '--max', action='store_true', default=sorted,
                    help='calculate the max number')
parser.add_argument('-min', '--min', action='store_true',
                    help='calculate the minimal number')
args = parser.parse_args()

if args.max == 1:
    print(max(args.sorts))
elif args.min == 1:
    print(min(args.sorts))
else:
    print(sorted(args.sorts, reverse=True))      
```
