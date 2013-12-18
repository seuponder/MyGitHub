#-*-coding:utf8-*-

'''
预处理数据,输出
items=[(item, [tf, weight]), (),...]
transactions=[[],[]...]
'''

def dataPrep(filePath, fpthreshold):
    #统计文件中每个标签词频
    items = {}
    transactions = []
    sortedTransactions = []

    file = open(filePath, "r", encoding = 'utf-8')
    for line in file:
        tagList = line.split("####")
        tran = []
        for tagStr in tagList[1:]:
            tag = tagStr.split("::::")
            tran.append(tag[1])
            if tag[1] not in items:
                items[tag[1]] = [1, int(tag[2])]
            else:
                items[tag[1]][0] = items[tag[1]][0] + 1
        transactions.append(tran)
    file.close()


    #for  tran in transactions:
    #    print(tran)
    
    #按照tf降序
    itemsR = sorted(items.items(), key = lambda result:result[1][0], reverse = True) #返回的是列表
    

    #删除阀值以下的item
    fitemsList = []
    fitemsDic = {}
    for item in itemsR:
        if item[1][0] > fpthreshold:
            fitemsList.append(item)
            fitemsDic[item[0]] = item[1]
        else:
            break #由于itemsR是排过序的，所以出现小于门限值的后面一定也小雨门限
            

    #items =dict(map(lambda item: (item[0], item[1]), itemsR))#转字典
    #排序transcactions
    for tran in transactions:
        tranTmp = []
        for item in tran:
            if item in fitemsDic:
                tranTmp.append(item)
        if tranTmp:#不为空
            dic = {}
            for item in tranTmp:
                dic[item] = fitemsDic[item]
            tran = sorted(dic.items(), key = lambda result:result[1][0], reverse = True) #返回的是列表

            sortedTran = []
            for item in tran:
                sortedTran.append(item[0])
            sortedTransactions.append(sortedTran)
    filePath = "E:\Data Mining\Code\\trans.txt"
    file = open(filePath, "w", encoding = 'utf-8')
    for  tran in sortedTransactions:
        file.write("%s\n"%tran)
    file.close()
    
    return (fitemsList,sortedTransactions)
'''
    for item in fitemsList:
        print("%s  %s"%(item[0], item[1]))
    
    filePath = "E:\Data Mining\Code\\trans.txt"
    file = open(filePath, "w", encoding = 'utf-8')
    for  tran in sortedTransactions:
        file.write("%s\n"%tran)
    file.close()
'''
    
    
#dataPrep("E:\Data Mining\Code\data_tag\\1047227947_0.txt", 10)


'''
输入：路径列表
输出：剪枝之后的路径的列表,排过序的items列表
items=[(item, tf), ...]
'''
def cpbStatistic(routeList, fpthreshold):
    items = []
    itemsDic = {}
    for rootNode in routeList:
        tmpNode = rootNode
        if tmpNode.item not in itemsDic:
            itemsDic[tmpNode.item] = tmpNode.count
        else:
            itemsDic[tmpNode.item] = itemsDic[tmpNode.item] + tmpNode.count
        while tmpNode.children:
            tmpNode = tmpNode.children[0]
            if tmpNode.item not in itemsDic:
                itemsDic[tmpNode.item] = tmpNode.count
            else:
                itemsDic[tmpNode.item] = itemsDic[tmpNode.item] + tmpNode.count

    #排序
    items = sorted(itemsDic.items(), key = lambda result:result[1], reverse = True) #返回的是列表

    #剪枝item
    fitemsList = []#返回
    fitemsDic = {}
    #items = [item for item in items if item[1] > fpthreshold]
    for item in items:
        if item[1] > fpthreshold:
            fitemsList.append(item)
            fitemsDic[item[0]] = item[1]
        else:
            break

    #剪枝路径上的节点
    prunedRouteList = routeList
    for rootNode in prunedRouteList[:]:#注意需要添加中括号
        traNode = rootNode
        flag = 0
        while traNode.children:
            flag = 1
            if traNode.item not in fitemsDic:
                #判断第一个节点
                if not traNode.parent:
                    ind = prunedRouteList.index(traNode)
                    traNode.children[0].parent = None
                    prunedRouteList[ind] = traNode.children[0]
                else:
                    traNode.parent.children[0] = traNode.children[0]
                    traNode.children[0].parent = traNode.parent
            traNode = traNode.children[0]

        #处理最后一个节点
        if flag == 0:#路径上只有一个节点
            if traNode.item not in fitemsDic:
                prunedRouteList.remove(rootNode)
        else:#路径上有多个节点
            #是根节点
            if not traNode.parent:
                if traNode.item not in fitemsDic:
                    prunedRouteList.remove(traNode)
            else:
                if traNode.item not in fitemsDic:
                    traNode.parent.children =  []
    return fitemsList,prunedRouteList
            
                    
            
    
