#-*-coding:utf8-*-

class node:
    def __init__(self, item = None, count = 0, parent = None):
        self.parent = parent
        self.children = []
        self.item = item
        self.count = count

    def equalsto(self, inNode):
        if inNode.item == self.item:
            return True
        else:
            return False
