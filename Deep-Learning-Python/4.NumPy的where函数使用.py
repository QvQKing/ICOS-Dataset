import numpy as np

# print('where函数的使用')
# x = numpy.arange(8)
# print(numpy.where(x > 3))
# x = numpy.array([1, 3, 2, 4])
# print(numpy.where(x > 3))
# x = numpy.arange(16).reshape(4,4)
# print(numpy.where(x > 3))
#
# cond = numpy.array([True, False, True, False])
# x = numpy.where(cond, 1, -1)  # true时返回前一个，false返回后一个
# print(x)
# cond = numpy.array([1, 2, 3, 4])
# x = numpy.where(cond > 2, 1, -1)
# print(x)
# y1 = numpy.array([1, 2, 3, 4])
# y2 = numpy.array([-1, -2, -3, -4])
# x = numpy.where(cond > 2, y1, y2)  # 长度须匹配!!
# print(x)  # [1,2,-3,-4]

# print('where函数的嵌套使用')
# y1 = numpy.array([-1, -2, -3, -4, -5, -6])
# y2 = numpy.array([1, 2, 3, 4, 5, 6])
# y3 = numpy.zeros(6)
# cond = numpy.array([1, 2, 3, 4, 5, 6])
# x = numpy.where(cond > 5, y3, numpy.where(cond > 2, y1, y2))#[1,2,-3,-4,-5,-6]
# print(x.dtype)  # [ 1.  2. -3. -4. -5.  0.]
# print(y3.dtype)
# print('ndarray的唯一化和集合运算')
# x = numpy.array([[6, 1, 2], [6, 1, 3], [1, 5, 2]])
# print(numpy.unique(x))  # [1,2,3,5,6]
# y = numpy.array([1, 6, 5])
# print(numpy.in1d(x, y))  # 比对x是否出现y中的元素，出现则输出true，无则false
# print(numpy.setdiff1d(x, y))  # 挑出x中y没有的元素
# print(numpy.intersect1d(x, y))  # 挑出x中y有的元素



'''作业：创建一个1-8的一维数组，把一维数组重塑成三维数组，把数组转置成
[[[1 3]
  [5 7]]

 [[2 4]
  [6 8]]]
  这种形式
之后筛选出其中大于5的元素的三维坐标'''
x=np.arange(1,9)
x=x.reshape(2,2,2)
x=x.transpose(2,0,1,)
print(x)
y=np.where(x>5)
print(y)