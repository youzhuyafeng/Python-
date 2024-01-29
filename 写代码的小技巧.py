# 不确定对方是否传参时，可以先设定一个空的数据类型利用if特性进行判断是否传了这个参数
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


# 利用pop函数特性对列表进行循环，但注意这样数据源会消失，酌情使用。同样可以全切片创建列表副本进行避免
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 寻找最大值：先假设第一个最大，接着循环数组遇到更大的覆盖掉原来值，冒泡排序效率太低。











