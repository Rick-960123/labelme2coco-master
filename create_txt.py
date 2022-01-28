# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random

trainval_percent = 0.8  # 验证集+训练集占总比例多少
train_percent = 0.7  # 训练数据集占验证集+训练集比例多少
jsonfilepath = 'labelme/total2020'
jsonfilepath = '整体测试图片'
txtsavepath = './'
total_xml = os.listdir(jsonfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

# ftrainval = open('./trainval2020.txt', 'w')
ftest = open('./test.txt', 'w')
# ftrain = open('./train2020.txt', 'w')
# fval = open('./val2020.txt', 'w')

for i in list:
    name = total_xml[i][:-5] + '\n'
    # if i in trainval:
    #     ftrainval.write(name)
    #     if i in train:
    #         ftrain.write(name)
    #     else:
    #         fval.write(name)
    # else:
    ftest.write(name)

# ftrainval.close()
# ftrain.close()
# fval.close()
ftest.close()