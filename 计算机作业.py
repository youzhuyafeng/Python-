# 上楼梯递归问题
def step(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return step(x-1)+step(x-2)


print(step(5))
# 相反数
def reverse_num(x):
    if x > 0:
        return -abs(x)
    elif x < 0:
        return abs(x)
    else:
        return 0


print(reverse_num(-1))
print(divmod(10, 3))
print(max(1, 2, 34, 5))
print(min(1, 3, 5, 6, 8))
print(pow(3, 5))
print(round(102.29371, 2))
a = '3'
print(int(a))
print(float(a))
print(list(a))
b = 'nankai.edu.cn'
c = reversed(b)
blank_str = ''
for i in c:
    blank_str += i
print(blank_str)
num_list = [2, 4, 6, 8, 1, 9, 0, 5]
print(sorted(num_list))
print(type(a))
print(type(c))
print(type(num_list))
print(len(num_list))

import math
print(math.ceil(2.45))
print(math.floor(2.45))
print(math.gcd(144, 162))
print(math.sqrt(28))

import random
random_num = random.randint(1, 100)
print(random_num)


from turtle import *
pensize(5)
color('yellow', 'red')
screensize(bg='black')
begin_fill()
for i in range(5):
    fd(100)
    left(72)
    fd(100)
    right(144)
end_fill()









