import pandas as pd
import numpy as np
import re
data = [['小明', 16.3456, 80], ['小孩', 18.2381, 90], ['小红', 23.4201, 100]]
dataframe = pd.DataFrame(data=data)
dataframe.columns = ['姓名', '年龄', '学历']
dataframe.index = ['1', '2', '3']
print(dataframe)
print(dataframe.round({'年龄': 2}))
dataframe.loc[['1', '2'], ['年龄', '学历']] = [[16, 1], [18, 2]]
df1 = dataframe[['年龄', '学历']].sum(skipna=True)
df1.name = '平均分'
print(df1)
print(dataframe._append(df1))
df12 = dataframe.drop(dataframe.columns[0], axis=1)
print(df12)
print(dataframe.columns[0])
dataframe.ffill()
df = dataframe.set_index(dataframe['姓名'], inplace=True, )
print(df)
print(format(200, '#^10'))
a = '{:.2%}'.format(10000)
print(a)
print(type(a))
"""
df = pd.read_excel("D:\python.learning\my_test_package\pandas测试.xlsx")
# print(df)
df1 = df['产品'].value_counts().index[0]
print(df1)
print(type(df1))
func = lambda x: x.value_counts().index[0]
df2 = df.groupby('姓名').agg({'产品': [func], '价格': [sum]})
print(df2)
"""




'''
url = 'https://www.espn.com/nba/salaries'
df = pd.DataFrame()
df = df._append(pd.read_html(url, header=0))
print(df)
df.to_csv('nba收入.csv', index=False)
'''

data_new = pd.read_excel('D:\八爪鱼\检索-中国知网.xlsx', header=0)
df = pd.DataFrame()
df = df._append(data_new)
print(df.info())
df_new = df[df['题名'].notnull()]
df_new.loc[:, '下载'] = df_new['下载'].fillna(0)
df_new.to_csv('知网-数据清洗后.csv', index=None)

a = np.array([1, 2, 3])
b = a.astype(dtype='float')
x = np.asarray(a, dtype=float)
print(x)
print(b)


x = [[1, 2, 3], [4, 5, 6]]
y = [[7, 8, 9], [10, 11, 12]]
c = np.array([x, y])
print(c)
d = np.array(x)
e = d.reshape((3, 2)).copy()
print(e)
e[0][0] = 2
print(e)
print(d)
# void类型数据表面是元组可用list或tuple转换

dt = np.dtype([('x', 'O'), ('y', 'f')])
print(np.dtype(np.int8))

print(dt[0])
print(dt['x'])
f = np.array([[('小明', 100)], [('小红', 90)]], dtype=dt)
print(f)
print(f[0].dtype)
print(type(f['x']))

df = pd.read_csv(r"D:\python.learning\my_test_package\楼中楼评论.csv")
a = df['楼中楼评论']
n = []
for i in a:
    pattern = re.compile("(.*>:?)?(.[^<]*)(<.*>)?")
    # 第一组为超链接的标签头，第三组为标签尾，第二组为评论信息
    search_str = pattern.search(i).group(2)
    n.append(search_str)
print(n)