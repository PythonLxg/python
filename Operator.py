# -*- coding utf-8 -*-
# C:\Users\lxg\Documents\Python\Practice
"""
Author:李小根
Time:2018/10/5
"""
"""
算数运算符
+,-,*,/,//,%,**
"""

print(1 + 2)    # 加法运算符
print('3' + '4')    # 加法运算符重载
print([1, 2] + [3, 4])  # 加法运算符重载

print(4 - 12)   # 减号运算符

print(2 * 3)    # 乘法运算符

print(5 / 2)    # 除法运算符

print(2 ** 3)   # 幂运算符

print(5 // 2)   # 整除运算符
print(5.2 // 2)     # 取整数部分

print(5 % 2)    # 求模运算符，求余运算符

# //，%应用场景
num = 6
row = num // 4
col = num % 4
"""
赋值运算符
"""
a = 1
b, c = 2, 3
q = w = e = 5
"""
符合运算符
+=,-=,*=,/=,//=,**=,%=
"""
number = 10
number += 1
print(number)
"""
比较运算符
>,<,==,!=,>=,<=,is
"""
result = 10 > 2
print(result)

# 链状比较运算符
print(1 < num < 10)

a = [1]
b = [1]
print(id(a), id(b))
print(a == b)   # 比较值是否相等
print(a is b)   # 比较唯一标志是否相等

"""
逻辑运算符
not,and,or
"""
# not 非，取反
# and 与，并且    and的两边必须都是真，最终才会是真
# or 或者    or两边只要有一边是真，那么最终才会是真
# 非零即真，非空即真
print(0 and True)
print(1 or 3)
print(1 and 3)
print(0 or False or 6)