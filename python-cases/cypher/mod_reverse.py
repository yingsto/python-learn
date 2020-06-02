# coding=utf-8

'''

欧几里得算法和扩展欧几里得算法的实现
gcd和ex_gcd

模逆计算是欧几里得算法的具体应用
mod_reverse

参考lark：
https://yuque.antfin-inc.com/nizhou.zn/ff29is/sgwgqh

'''

#gcd(a, b) = gcd(b, a % b)
#递归实现
def gcd_0(a, b):
    if b == 0:
        return a
    else:
        r = gcd_0(b, a % b)
        return r

#循环实现
def gcd_1(a, b): # a > b
    while b != 0:
        a, b = b, a % b
    return a

x = 1
y = 0
#递归实现
def ex_gcd_0(a, b):
    global x
    global y
    if b == 0:
        x = 1
        y = 0
        return a
    r = ex_gcd_0(b, a % b)
    t = y
    y = x - (a // b) * y
    x = t
    return r

#循环实现
def ex_gcd_1(a, b):
    global x
    global y
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        #xi = xi-2 - qi * xi-1
        #yi = yi-2 - qi * yi-1
        x1, y1, x0, y0 = x0 - q * x1, y0 - q * y1, x1, y1
        #print("(%d %d %d %d)" %(x1, y1, x0, y0))
    x = x0
    y = y0
    return a

def mod_reverse_0(a, n):
    if gcd_0(n, a) != 1:
        return None
    for x in range(1, n):
        if (a * x) % n == 1:
            return x

def mod_reverse_1(a, n):
    global y
    if gcd_0(n, a) != 1:
        return None
    ex_gcd_0(n, a)
    return y % n

def mod_reverse_2(a, n):
    if gcd_0(n, a) != 1:
        return None
    ex_gcd_1(n, a)
    return y % n

def mod_reverse_3(a, p):
    t = a ** (p - 2)
    return t % p

if __name__ == '__main__':
    a = 2
    n = 13
    print("x = %d" %(mod_reverse_0(a, n)))
    print("x = %d" %(mod_reverse_1(a, n)))
    print("x = %d" %(mod_reverse_2(a, n)))

    #n是素数时可以采用
    print("x = %d" %(mod_reverse_3(a, n)))