#-*-coding:utf8-*-

from node import *

class fptree:
    def __init__(self):
        self.root = node('root', -1)
        self.headTable = []

    '''
    根据transactions产生FPtree
    items排好降序的列表
    transactions是每一项排好序的
    '''
    def buildFPtree(self, items, transactions):
        #建立头表
        for item in items:
            htnodeTmp = node(item[0], item[1][0])
            self.headTable.append(htnodeTmp)

        #建树
        for tran in transactions:
            count = 0
            tranRoot = node()
            parentNode = node()
            for item in tran:
                if count == 0:
                    nodeTmp = node(item, 1)
                    tranRoot = nodeTmp
                    count = 1
                else:
                    nodeTmp = node(item, 1)
                    nodeTmp.parent = parentNode
                    parentNode.children.append(nodeTmp)
                parentNode = nodeTmp
            self.insertTran(tranRoot, self.root)

    '''
    根据路径列表产生CFPtree
    items排好降序的列表
    '''
    def buildCFPTree(self, items, routeList):
        #建立头表
        for item in items:
            htnodeTmp = node(item[0], item[1])
            self.headTable.append(htnodeTmp)

        #建树
        for routeNode in routeList:
            self.insertTran(routeNode, self.root)
            
    '''
    根据头表节点返回相应的路径
    '''
    def cpb4(self, htNode):
        routeList = []
        if htNode.children:
            for nodeTmp in htNode.children:
                treeNode = nodeTmp
                childNode = node()
                currentNode = node()
                flag = 0
                while treeNode.parent.count != -1:
                    if flag == 0:
                        currentNode = node(treeNode.parent.item, treeNode.count)
                        treeNode = treeNode.parent
                        flag = 1
                    else:
                        childNode = currentNode
                        currentNode = node(treeNode.parent.item, currentNode.count)
                        childNode.parent = currentNode
                        currentNode.children.append(childNode)
                        #根据路径向上搜索
                        treeNode = treeNode.parent
                routeList.append(currentNode)
        return routeList
                    
        

    '''
    将transaction链表插入到fptree
    tranRoot为新的transaction的根节点
    rootNode为子树根节点
    '''
    def insertTran(self, tranRoot, rootNode):
        flag = 0
        if rootNode.children:
            for nodeTmp in rootNode.children:
                if nodeTmp.equalsto(tranRoot):
                    nodeTmp.count = nodeTmp.count + tranRoot.count
                    flag = 1
                    if tranRoot.children:#还有儿子的话继续
                        self.insertTran(tranRoot.children[0], nodeTmp)
                    break
        if flag == 0:
            rootNode.children.append(tranRoot)
            tranRoot.parent = rootNode
            #在头表中加入相应的项
            self.insertht(tranRoot)

    '''
    将相应的节点插入头表
    '''
    def insertht(self, nodeRoot):
        flag = 0
        for nodeht in self.headTable:
            if nodeht.equalsto(nodeRoot):
                nodeht.children.append(nodeRoot)
                flag = 1
                if nodeRoot.children:#还有儿子的话继续
                    self.insertht(nodeRoot.children[0])
        if flag == 0:
            print("在头表中没找到相应的item,请检查代码！")

    '''
    遍历整个fptree
    '''
    def traversalTree(self, treeRoot):
        file = open("E:\Data Mining\Code\\fpTree.txt", "a", encoding='utf-8')
        if treeRoot.parent== None:
            file.write('%s==>%s   '%(treeRoot.item,treeRoot.count))
        else:
            file.write('(%s)%s==>%s   '%(treeRoot.parent.item, treeRoot.item,treeRoot.count))
        file.close()
        if treeRoot.children:
            for subTreeRoot in treeRoot.children:
                self.traversalTree(subTreeRoot)
        else:
            file = open("E:\Data Mining\Code\\fpTree.txt", "a", encoding='utf-8')
            file.write('\n')
            file.close()

    '''
    遍历头表
    '''
    def traversalHT(self):
        file = open("E:\Data Mining\Code\\fpTree.txt", "a", encoding='utf-8')
        for nodeTmp in self.headTable:
            file.write('(头表表项)%s==>%s   '%(nodeTmp.item,nodeTmp.count))
            for nodeTreeTmp in nodeTmp.children:
                file.write('%s==>%s   '%(nodeTreeTmp.item,nodeTreeTmp.count))
            file.write('\n')
        
