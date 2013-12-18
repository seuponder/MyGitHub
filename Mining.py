#-*-coding:utf8-*-

from fptree import *
from dataPrep import cpbStatistic
#FP数mining函数

def Mining(FPTree, fpthreshold):
    FPSet = []
    if not FPTree.headTable:
        return FPSet
    
    for htNode in FPTree.headTable[::-1]:
        routeList = FPTree.cpb4(htNode)
        if routeList:#确保路径列表有效
            (citems, prunedRList) = cpbStatistic(routeList, fpthreshold)
            if prunedRList:#剪枝后有效
                cFPTree = fptree()
                cFPTree.buildCFPTree(citems, prunedRList)
                CFPSet = Mining(cFPTree, fpthreshold)
                for ftran in CFPSet:
                    ftran[0].append(htNode.item)
                    FPSet.append(ftran)
        FPSet.append([[htNode.item], htNode.count])
    return FPSet
