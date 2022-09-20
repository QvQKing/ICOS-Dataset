import os
import glob
import shutil

from PIL import Image
import random
import matplotlib.pyplot as plt
from lxml import etree

your_voc_path =r'D:\py学习\xml_anno\000000.xml'

threshold = 100  # 图片数量阈值，选取图片数量大于350的类别
threshold_cls = 15  # 类别阈值，选取最多的前15类数据


def maxk(arraylist, k):  # 返回最大的前k个数据的索引，k为类别阈值
    maxlist = []
    maxlist_id = [i for i in range(0,k)]
    m = [maxlist, maxlist_id]
    for i in maxlist_id:
        maxlist.append(arraylist[i])
    for i in range(k, len(arraylist)):  # 对目标数组之后的数字
        if arraylist[i] > min(maxlist):
            mm = maxlist.index(min(maxlist))
            del m[0][mm]
            del m[1][mm]
            m[0].append(arraylist[i])
            m[1].append(i)
    return maxlist_id


labels = ['road roller', 'bar deposits', 'piece deposits', 'brick', 'earth vehicles', 'tower', 'digger', 'bulldozer',
          'drill', 'crane', 'concrete truck', 'mixer', 'concrete simple house', 'simple house', 'green cover',
          'black cover', 'blue enclosure', 'grey enclosure', 'color enclosure', 'building', 'groove', 'big building',
          'building frame', 'scaffold', 'vehicle', 'grave mound', 'garbage', 'crushed stones', 'bricks', 'greenhouse',
          'site shanty', 'woodpile', 'fuel tank', 'big truck', 'car', 'boxcar', 'small truck', 'van car',
          'watering car', 'tutu', 'crane closed', 'Agricultural Tricycles', 'bus', 'pickup', 'large cement pipes',
          'middle cement pipes', 'small cement pipes', 'thin steel pipe', 'crude steel pipe', 'big stell pipe', 'slab',
          'U-steel', 'road leveling machine']
print('根据阈值计算筛选后的类别')
path = your_voc_path + 'VOCdevkit/VOC2007/Annotations/'
listdir = os.listdir(path)
count = [0 for i in range(53)]  # 每个类别的图片数
for file in listdir:
    with open(path + file, "r",encoding='utf-8') as f:
        text = f.read()
    text = etree.fromstring(text)
    name = text.xpath('/annotation/object/name/text()')
    if name[0] not in ['tutu', 'car', 'garbage', 'van car', 'Agricultural Tricycles', 'pickup','groove','watering car','bus']:
        count[int(labels.index(name[0]))] += 1
new_labels = []  # 筛选后的类别标签
new_cls = []  # 筛选后的类别编号
new_counts=[] #筛选后每类的数量s
# 根据类别阈值筛选
# kmax_list = maxk(count, threshold_cls)
# for i in kmax_list:
#     new_cls.append(i)
#     new_labels.append(labels[i])
#     new_counts.append(count[i])
# 根据图片数量阈值筛选
for index, i in enumerate(count):
    if int(i) > threshold:
        new_cls.append(index)
        new_labels.append(labels[index])
        new_counts.append(count[index])
        print(labels[index])

plt.pie(new_counts,labels=new_labels,autopct='%.0f%%',pctdistance=0.8,
        # colors=['lightgrey' if i%2==0 else 'grey' for i in range(len(new_counts))]
        )
plt.savefig('{}类饼状图.png'.format(len(new_cls)), dpi=300, format='png', bbox_inches='tight')
plt.show()
fig, ax = plt.subplots()
y = [i for i in range(len(new_counts))]
plt.barh(y=y,width=new_counts,tick_label=new_labels,
         # color='black'
         )
for i, v in enumerate(new_counts):
    ax.text(v, i-0.2, str(v),
            # color='black',
            fontweight='bold')
plt.savefig('{}类柱状图.png'.format(len(new_cls)), dpi=300, format='png', bbox_inches='tight')
plt.show()



