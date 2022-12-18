class BinaryTreeList:
    def __init__(self, size) -> None:
        self.btSize = size * [None]
        self.lastUsedIndex = 0
        self.maxsize = size

    def __str__(self) -> str:
        return "->".join([i for i in self.btSize if i])

    def insertIntoBT(self, value):
        if self.lastUsedIndex + 1 == self.maxsize:
            return "Tree is full"
        else:
            self.btSize[self.lastUsedIndex + 1 ] = value
            self.lastUsedIndex += 1

    def searchTree(self, value):
        for i in range(1,len(self.btSize)):
            if self.btSize[i] == value:
                return "success"
        return "There is no value"

    def preOrederTraversal(self, Index = 1):
        if Index > self.lastUsedIndex:
            return
        else:
            print(self.btSize[Index])
            self.preOrederTraversal(Index*2)
            self.preOrederTraversal(Index*2 + 1)

    def inOrederTraversal(self, Index = 1):
        if Index > self.lastUsedIndex:
            return
        else:
            self.preOrederTraversal(Index*2)
            print(self.btSize[Index])
            self.preOrederTraversal(Index*2 + 1)

    def postOrederTraversal(self, Index = 1):
        if Index > self.lastUsedIndex:
            return
        else:
            self.preOrederTraversal(Index*2)
            self.preOrederTraversal(Index*2 + 1)
            print(self.btSize[Index])

    def levelOrderTraversal(self, Index=1):
        for i in range(1, len(self.btSize)):
            print(self.btSize[i])

binaryTree = BinaryTreeList(8)
binaryTree.insertIntoBT("Drinks")
binaryTree.insertIntoBT("Cold")
binaryTree.insertIntoBT("Hot")
binaryTree.insertIntoBT("Tea")
binaryTree.insertIntoBT("Coffe")

print(binaryTree.searchTree("Cold"))
binaryTree.preOrederTraversal()