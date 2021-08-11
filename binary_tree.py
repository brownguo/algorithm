
class BTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # 前序遍历, 父, 左, 右
    def preorder(self):
        if self.data is not None:
            print(self.data, end=" ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    # 中序遍历, 左, 父, 右
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        if self.data is not None:
            print(self.data, end=" ")
        if self.right is not None:
            self.right.inorder()

    # 后序 左,右,中
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.data is not None:
            print(self.data, end=" ")


if __name__ == '__main__':

    l = BTree(5)
    l.left = BTree(1)
    l.right = BTree(3)

    r = BTree(6)
    r.left = BTree(2)
    r.right = BTree(4)

    t = BTree(11)
    t.left = l
    t.right = r
    t.postorder()
