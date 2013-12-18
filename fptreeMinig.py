#-*-coding:utf8-*-

from fptree import *
from node import *
from dataPrep import dataPrep
from Mining import Mining

#fptree-mining

filePath = "E:\Data Mining\Code\data_tag\\1047227947_0.txt"#1047227947_0
fpthreshold = 20
#数据预处理
(fitemsList,sortedTransactions) = dataPrep(filePath, fpthreshold)


items=[('chips', [7,7]),('eggs', [7,7]),('bread', [7,7]),('milk', [6,6]),('beer',[4,4]),('popcorn', [2,2]),('butter', [2,2])]
sample=[
    ['eggs','bread','chips','milk'],
    ['eggs','chips','beer','popcorn'],
    ['eggs','bread','chips'],
    ['eggs','bread','chips','milk','beer','popcorn'],
    ['bread','milk','beer'],
    ['eggs','bread','beer'],
    ['bread','chips','milk'],
    ['eggs','bread','chips','milk','butter'],
    ['eggs','chips','milk','butter']
]

#生成fptree
fpTree = fptree()
fpTree.buildFPtree(fitemsList,sortedTransactions)
FPSet = Mining(fpTree, fpthreshold)

#输出频繁集
file = open("E:\Data Mining\Code\\FPSet.txt", "w", encoding='utf-8')
for fpTran in FPSet:
    #print(fpTran)
    file.write("%s===%s\n"%(fpTran[0], fpTran[1]))
    #file.write("%s===\n"%fpTran)
file.close()
'''
fpTree.traversalTree(fpTree.root)#输出树

#输出头表
file = open("E:\Data Mining\Code\\fpTree.txt", "a", encoding='utf-8')
file.write('\n\n\n\n')
file.close()
fpTree.traversalHT()
'''
