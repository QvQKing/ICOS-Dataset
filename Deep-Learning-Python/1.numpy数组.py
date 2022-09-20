import numpy

print('使用列表生成一维数组')
data = [1.2, 2, 3.1, 4, 5, 6]
x = numpy.array(data)
print(x)  # 打印数组
print(x.dtype)  # 打印数组元素的类型
print(x[0], x[3])

print('使用列表生成二维数组')
data = [[1, 2], [3, 4], [5, 6], [7, 8]]
x = numpy.array(data)
print(data)
print(x)  # 打印数组
print(data)
print(x.ndim)  # 打印数组的维度
print(x.shape)  # 打印数组各个维度的长度。shape是一个元组

print('使用zero/ones/empty创建数组:根据shape来创建')
x = numpy.zeros(6)  # 创建一维长度为6的，元素都是0一维数组
print(x)
x = numpy.zeros((2, 3))  # 创建一维长度为2，二维长度为3的二维0数组
print(x)
x = numpy.ones((2, 3))  # 创建一维长度为2，二维长度为3的二维1数组
print(x)
x = numpy.empty((3, 3))  # 创建一维长度为2，二维长度为3,未初始化的二维数组
print(x)
#
print('使用arange生成连续元素')
print(numpy.arange(7))  # [0,1,2,3,4,5] 开区间
print(numpy.arange(0, 6, 3))  # [0, 2, 4]

# 对角线上为1，其余全为零
print('创建一个3*3正方形的矩阵')
print(numpy.eye(3))

print('数组的元素重复操作')
x = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(x)
print(x.repeat(3))  # 按元素重复
print(x.repeat(2, axis=0))  # 按行重复
print(x.repeat(2, axis=1))  # 按列重复
print(x.repeat(2, axis=2))
x = numpy.array([[1, 2], [3, 4]])
print(numpy.tile(x, 3))  # tile瓦片：[1 2 1 2]
print(numpy.tile(x, (3, 1)))  # 指定从低维到高维依次复制的次数。
# [[1 2 1 2][1 2 1 2]]
