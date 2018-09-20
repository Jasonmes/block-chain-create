#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

"""
新的区块依赖工作量证明算法（PoW）来构造。
PoW的目标是找出一个符合特定条件的数字，这个数字很难计算出来，但容易验证。
这就是工作量证明的核心思想。
"""

"""
假设一个整数 x 乘以另一个整数 y 的积的 Hash 值必须以 0 结尾，
即 hash(x * y) = ac23dc…0。设变量 x = 5，求 y 的值？用Python实现如下：
"""

from hashlib import sha256
x = 5
y = 0  # ye未知
"""

"""
while sha256(f'{x * y}'.encode()).hexdigest()[-1] != '0':
    y += 1
    print(f'The solution is y = {y}')

"""
hashlib是涉及安全散列和消息摘要，提供多个不同的加密算法接口，
如SHA1、SHA224、SHA256、SHA384、SHA512、MD5等
常用属性

hashlib.algorithms 
列出所有加密算法

h.digest_size 
产生的散列字节大小。

h.block_size 
哈希内部块的大小

常用方法

hash.new([arg]) 
创建指定加密模式的hash对象

hash.update(arg) 
更新哈希对象以字符串参数。如果同一个hash对象重复调用该方法，m.update(a); m.update(b) 等价于 m.update(a+b)

hash.digest() 
返回摘要，作为二进制数据字符串值。

hash.hexdigest() 
返回摘要，作为十六进制数据字符串值

hash.copy() 
复制


"""