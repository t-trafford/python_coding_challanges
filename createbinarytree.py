

class BinaryTree(object):

    def __init__(self,rootobj):
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None

    def insertLeftChild(self, newobj):

       if self.leftchild == None:
           self.leftchild = newobj
       else:
           t = BinaryTree(newobj)
           t.leftchild = self.leftchild
           self.leftchild = t

    def insertRightChild(self, newobj):

        if self.rightchild == None:
            self.rightchild = newobj
        else:
            t = BinaryTree(newobj)
            t.rightchild = self.rightchild
            self.rightchild = t

    def setRootval(self,newroot):
        self.key = newroot

    def getRootval(self):
        return self.key

    def getLeftChild(self):
        return self.leftchild

    def getRightChild(self):
        return self.rightchild

    def preorder(self):
        print(self.key)
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()
