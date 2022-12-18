import sys
sys.path.insert(0, 'C:\\Users\\prate\\OneDrive\\Desktop\\python_tu\\Algo')

from Queues import Queue_linked

class BinaryTree:
    def __init__(self, rootNode = None) -> None:
        self.rootNode = rootNode
        self.leftnode = None
        self.rightnode = None

newBT = BinaryTree("Drinks")
hot = BinaryTree("Hot")
cold = BinaryTree("cold")
newBT.rightnode = hot
newBT.leftnode = cold
fanta = BinaryTree("fanta")
cola = BinaryTree("cola")
cold.rightnode = fanta
cold.leftnode = cola

def preOrderTreversal(node, ind):
    if node == None:
        return
    else:
        print(f"{node.rootNode} ({ind if ind else 'root'})")
        preOrderTreversal(node.leftnode, "left")
        preOrderTreversal(node.rightnode, "right")

def InOrderTreversal(node, ind):
    if node == None:
        return
    else:
        InOrderTreversal(node.leftnode, "left")
        print(f"{node.rootNode}-->{ind if ind else 'root'}")
        InOrderTreversal(node.rightnode, "right")

def PostOrderTreversal(node, ind):
    if node == None:
        return
    else:
        PostOrderTreversal(node.leftnode, "left")
        PostOrderTreversal(node.rightnode, "right")
        print(f"{node.rootNode}-->{ind if ind else 'root'}")

def LevelOrderTraversal(node):
    if node == None:
        return
    else:
        customeQueue = Queue_linked.Queue()
        customeQueue.enqueue(node)
        while not (customeQueue.isEmpty):
            root = customeQueue.dequeue
            print(root.rootNode)
            if root.leftnode is not None:
                customeQueue.enqueue(root.leftnode)
            if root.rightnode is not None:
                customeQueue.enqueue(root.rightnode)

def searchInBT(node , search_node):
    if node == None:
        return
    else:
        customeQueue = Queue_linked.Queue()
        customeQueue.enqueue(node)
        while not (customeQueue.isEmpty):
            root = customeQueue.dequeue
            if root.value.rootNode == search_node:
                return "Success"

            if root.value.leftnode is not None:
                customeQueue.enqueue(root.value.leftnode)
            if root.value.rightnode is not None:
                customeQueue.enqueue(root.value.rightnode)
        return "There is no node"

def insertIntoBT(node, newNode):
    if node == None:
        rootnode = BinaryTree(newNode)
        return
    else:
        customeQue = Queue_linked.Queue()
        customeQue.enqueue(node)

        while not (customeQue.isEmpty):
            root = customeQue.dequeue
            if root.leftnode is not None:
                customeQue.enqueue(root.leftnode)
            else:
                root.leftnode = newNode
                return f"Successfully Inserted inserted left side at {root.rootNode}"
            
            if root.rightnode is not None:
                customeQue.enqueue(root.rightnode)
            else:
                root.rightnode = newNode
                return f"Successfully Inserted inserted right side at {root.rootNode}"

Tea = BinaryTree("Tea")
Coffee = BinaryTree("Coffee")
print(insertIntoBT(newBT, Tea))
print(insertIntoBT(newBT, Coffee))

# LevelOrderTraversal(newBT)

def getDepestNode(node):
    if node == None:
        return
    else:
        customQueue = Queue_linked.Queue()
        customQueue.enqueue(node)

        while not customQueue.isEmpty:
            root = customQueue.dequeue

            if root.leftnode is not None:
                customQueue.enqueue(root.leftnode)

            if root.rightnode is not None:
                customQueue.enqueue(root.rightnode)
        
        return root

def deleteDepestNode(rootnode, dnode):
    if rootnode == None:
        return
    else:
        customQueue = Queue_linked.Queue()
        customQueue.enqueue(rootnode)
        while not customQueue.isEmpty:
            root = customQueue.dequeue
            if root.rootNode == dnode:
                root.rootNode = None
                return
            
            if root.leftnode:
                if root.leftnode == dnode:
                    root.leftnode = None
                    return
                else:
                    customQueue.enqueue(root.leftnode)

            if root.rightnode:
                if root.rightnode == dnode:
                    root.rightnode = None
                    return
                else:
                    customQueue.enqueue(root.rightnode)

def deleteNodeFromBT(rootnode, deletnode):
    if rootnode ==None:
        return "Binary tree is Empty"
    else:
        customQue = Queue_linked.Queue()
        customQue.enqueue(rootnode)

        while not customQue.isEmpty:
            root = customQue.dequeue
            if root.rootNode == deletnode:
                deepest = getDepestNode(rootnode)
                root.rootNode = deepest.rootNode
                deleteDepestNode(rootnode, deepest)
                return f"Successfully deleted {deletnode}"

            if root.leftnode:
                customQue.enqueue(root.leftnode)
            if root.rightnode:
                customQue.enqueue(root.rightnode)

        return f"There is no node like {deletnode}"
            


#print(deleteNodeFromBT(newBT, "Tea"))
#LevelOrderTraversal(newBT)

preOrderTreversal(newBT,"")