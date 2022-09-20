import numpy as np

import matplotlib.pyplot as plt
import re

with open(r'D:\py学习\xml_anno\000000.xml', 'r') as f:
    txt = f.read()
labels=re.findall(r'= (.*) AP', txt)
t = re.findall(r'\[.*\]', txt)
for i in range(len(t)):
    t[i] = t[i].replace('[', '')
    t[i] = t[i].replace(']', '')
    t[i] = t[i].replace('\'', '')
    t[i] = t[i].split(',')
    t[i] = [float(j) for j in t[i]]
fig, ax = plt.subplots()  # 创建图实例
i=0
while i<len(t):
    labels[int(i / 2)]=labels[int(i/2)][0].upper()+labels[int(i/2)][1:]
    ax.plot(t[i+1], t[i],
            label=labels[int(i/2)],
            )
    i+=2
ax.set_xlabel('recall') #设置x轴名称 x label
plt.xticks(np.linspace(0, 20,10))
plt.yticks(np.linspace(0, 20,10))

ax.set_ylabel('precision')
plt.legend(ncol=2)
plt.show()
