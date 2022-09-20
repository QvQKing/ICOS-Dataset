import numpy

# print('ndarray数组重塑')
# x = numpy.arange(0, 6)  # [0 1 2 3 4 5]
# print(x)  # [0 1 2 3 4 5]
# print(x.reshape(2, 3))  # [[0 1 2][3 4 5]]
# print(x.reshape(3, 2).reshape(2, 3))  # [[0 1][2 3][4 5]]前边分的无效，以后边得为准
#
# x = x.reshape(2, 3)
# a = x.flatten()
# print(a)  # [0 1 2 3 4 5]
# a[0] = -1  # flatten返回的是拷贝
# print(x)  # [[0 1 2][3 4 5]]
# b = x.ravel()
# print(b)  # [0 1 2 3 4 5]
# b[0] = -1  # ravel返回的是视图（引用）
# print(x)  # [[-1 1 2][3 4 5]]
#
# print("维度大小自动推导")
# arr = numpy.arange(15)
# print(arr.reshape(5, -1))  # 最后一位为-1可以自动推导

print('ndarray数组的转置和轴对换')
k = numpy.arange(9)  # [0,1,....8]
m = k.reshape(3, -1)  # 改变数组的shape复制生成2维的，每个维度长度为3的数组
print(k)  # [0 1 2 3 4 5 6 7 8]
print(m)  # [[0 1 2] [3 4 5] [6 7 8]]
# 转置(矩阵)数组：T属性 : mT[x][y] = m[y][x]
print(m.T)  # [[0 3 6] [1 4 7] [2 5 8]]
# 计算矩阵的乘法
print(numpy.dot(m, m.T))  # numpy.dot点乘
# 高维数组的轴对象
k = numpy.arange(8).reshape(2, 2, 2)
print(k)  # [[[0 1],[2 3]],[[4 5],[6 7]]]
print(k[0][1][0])

# 轴变换 transpose 参数:由轴编号组成的元组
m = k.transpose(1, 0, 2)  # m[y][x][z] = k[x][y][z]
print(m)  # [[[0 1],[4 5]],[[2 3],[6 7]]]
print(m[0][1][0])
# 轴交换 swapaxes (axes：轴)，参数:一对轴编号
m = k.swapaxes(1, 0)  # 将第一个轴和第二个轴交换 m[y][x][z] = k[x][y][z]
print(m)  # [[[0 1],[4 5]],[[2 3],[6 7]]]
print(m[0][1][0])
# 使用轴交换进行数组矩阵转置
m = numpy.arange(9).reshape(3, 3)
print(m)  # [[0 1 2] [3 4 5] [6 7 8]]
print(m.swapaxes(1, 0))  # [[0 3 6] [1 4 7] [2 5 8]]
