# Python语法糖

## 语法糖说明
```buildoutcfg
语法糖（Syntactic sugar）：
    计算机语言中特殊的某种语法
    这种语法对语言的功能并没有影响
    对于程序员有更好的易用性
    能够增加程序的可读性
```
简而言之，语法糖就是程序语言中提供[**`奇技淫巧`**]的一种手段和方式而已。
通过这类方式编写出来的代码，即好看又好用,好似糖一般的语法。固美其名曰：**语法糖**

## 一个简单的例子
假设：有2个数字，现需要从中得到最大的那个数字。如何实现？
``` python
b = 2 
c = 3

if b > c:
    a = b
else:
    a = c
```
其实还有更多的其它实现方式：
``` python
a = max(b, c)
a = c > b and c or b
a = c if c > b else b
a = [b, c][c > b]
```
这些都是可以实现我们需求的方法，殊途同归。但是它们在易用性、简洁性、可读性、性能等方面的表现都不一样。那么问题来了！
> 哪个才是我们所说的语法糖呢？


## 一些常见的语法糖
``` python
a = b = 2; c = 3
b, c = c, b
a < c < b < 5
'1' * 100
[1,2,3,4] + [5,6,7,8]
```
可以看到这些语法，在其它语言里通常不会出现的。但是在Python中却神奇的被支持了，所以这些都是当之无愧的Python语法糖。

### 切片操作
像列表这类可以支持**`切片`**操作的对象，则是我最初喜欢Python的一个非常重要的原因。
```python
l = [1, 2, 3, 4, 5]
l[2]
l[:3]
l[3:]
l[2:4]
l[:-1]
l[:]
l[::2]
```
## with语法糖
with语法糖实现的是一个上下文管理器，它主要的特点就是帮助我们自动管理上下文的衔接。即在需要的时候传给我们，不需要的时候自动关闭上下文对象。
需要注意的是：使用with语法糖是有条件的。即其后跟的对象必须要实现__enter__和__exit__这2个魔法属性。具体使用的例子如下：

``` python
with open('example_2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
```

## else语法糖
Python中提供一类else的语法，它可以在原有语法基础之上，支持更多一种情况的选择。
主要有for-else，while-else，try-else。

### for else
```python
for i in range(1):
    print(i)
    break
else:
    print('for end')
```

### while else
```python
i = 1
while i:
    print(i)
    i -= 1
    break
else:
    print('while end')
```

### try else
```python
try:
    1 / 1
except Exception as e:
    print('except occured')
else:
    print('it is fine')
finally:
    print('i am finally')
```

## 函数相关语法糖
Python中函数我们都非常的熟悉，而在函数的使用上却有着与其它语言不同的选择。

### 动态参数
```python
def example_dynamic_args(*args, **kwargs):
    '''动态参数'''
    print(args)
    print(kwargs)
```
这个函数的参数与函数相比，其参数会有些不同之处。因为它们在接收参数时使用了不同方式。
```python
example_dynamic_args(1,'2', True, name='xiaowu', age=18)
l = [1,'2',False]
d = {'name': 'xiaoming', age: '16'}
example_dynamic_args(*l, **d)
```

### 匿名函数
匿名函数在很多的语言中都存在，通常在临时需要一个函数的场景下使用。
```python
lambda x: x * 2
```
Python中使用lambda表达式来实现匿名函数，观察上面的lambda表达式。其特点如下：
- > 可以接受参数
- > 函数体只有一个表达式
- > 无需显式的return语句
- > 整个表达式在一个语法行内实现

值得注意的是，lambda表达式除了一些语法上的限制之外；其它函数该有的特性它都有。比如：支持动态参数。下面是一个使用lambda表示的场景：
```python
in_dict = {'a': 10, 'b': 2, 'c': 3}
print('in_dict:', in_dict)
out_dict = sorted(in_dict.items(), key=lambda x: x[1])
print('out_dict', out_dict)
```

## 推导表达式
推导表达式是Python中常见的语法糖，在很多的数据处理场景中，我们可能会使用的到。
最常见的就是列表推导表达式，可以用来过滤、处理列表中的子项并输出一个新的列表。除此之外还有几个推导式也是非常好用的。

### 列表推导表达式
```python
in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]
print('array before:', in_list)
array = [i for i in in_list if i % 2 != 0] # 列表推导表达式
print('array after:', array)
```

### 生成器推导表达式
```python
in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]
print('array before:', in_list)
array = (i for i in in_list if i % 2 != 0) # 生成器推导表达式
print('array after:', array)
```

### 集合推导表达式
```python
in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]
print('array before:', in_list)
array = {i for i in in_list if i % 2 != 0} # 集合推导表达式
print('array after:', array)
```

### 字典推导表达式
```python
in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]
print('array before:', in_list)
array = {i: i * 2 for i in in_list if i % 2 != 0}  # 字典推导表达式
print('array after:', array)
```

不同推导式在语法使用上基本一致，只是在返回对象的类型上有所差别。

## yield表达式
yield语法也是Python中比较有特点的语法糖，可以说是特有的。虽然其它语言有实现类似机制的功能。
yield是Python中实现**`协程(coroutine)`**的一个重要基础。
```python
def example_generator(in_list):
    '''生成器'''
    for i in in_list:
        yield i * 2
```

## 装饰器
重要的往往在最后面，装饰器是学习Python绕不过去的坎。就像学习Java要理解面向对象和设计模式一样。
学习Python，你就应该要掌握好闭包、生成器、装饰器等相关知识。而对于编写高并发程序时则要掌握协程相关知识。
```python
def example_decorator(func):
    '''装饰器'''
    def inner():
        func()

    return inner
```

# 更多学习
- [Python装饰器详解][1]
- [Python多线程GIL][2]
- [Python魔法属性][0]
- [Python语法糖][3]

[0]:https://blog.csdn.net/five3/
[1]:https://blog.csdn.net/five3/article/details/83447467
[2]:https://blog.csdn.net/five3/article/details/78563365
[3]:https://blog.csdn.net/five3/article/details/83474633
