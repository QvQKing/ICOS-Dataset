import pandas

df = pandas.read_csv('nba.csv')
print(df)
print()

# #查看数据（列在前，行在后）
# print(df['Name'][3:6])
# print(df[['Name','Salary']][3:6])
# print()
#查看数据（行在前，列在后）
# print(df.loc[3:6][['Name','Salary']])
# print(df.loc[[1,4,8,8,6]][['Name','Salary']])
# print()
# #按条件查找数据
# print(df[df['Salary']>10000000])
# print(df.loc[df['Salary']>10000000])

# # 添加数据
# df['yuexin'] = df['Salary']/12
df.loc['aaa']=df.loc[0]
# print(df)
# for i,item in enumerate(df):
#     print(item)
#     for j,jtem in enumerate(df[item]):
#         print(jtem,end=' ')
#     print()

# 修改数据
# df.loc[1,'Name']='aaa'
# df['Name'][0]='bbb'
# print(df)

# 删除数据
# df.drop(labels=None, axis=0,
#         index=None, columns=None,
#         level=None, inplace=False,
#         errors='raise')
# 1.labels:要删除的列或者行，如果要删除多个，传入列表
# 2.axis:轴的方向，0为行，1为列，默认为0
# 3.index:指定的一行或多行
# 4.columns:指定的一列或多列
# 5.level:索引层级，将删除此层级
# 6.inplace:布尔值，是否生效
# 7.errors:ignore或raise，默认为raise，如果为ignore，则容忍错误，仅删除现有标签
# df.drop(index=[3,6],inplace=True)
# df=df.drop(labels='Number',axis=1)
# df.drop(columns=['College','aaa'],inplace=True,errors='ignore')
# df=df.drop(0)
print(df)
df.to_csv('nba2.csv',index=False)
