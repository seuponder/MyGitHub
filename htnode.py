#-*-coding:utf8-*-

#头表node

class  htnode:
    def __init__(self, item = None, count = 0):
        self.item = item
        self.count = count
        self.children = []
