class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()


myList = LinkedList()
myList.addNode(5)
myList.addNode(15)
myList.addNode(25)
myList.addNode(35)
myList.addNode(45)

print("Tüm Liste : ")
myList.printNode()
print("Liste Değeri : ")
print(myList.getSize())
orta = (myList.getSize() / 2 - (0.5))
nNode = Node(None, myList.head)
nNode.head = myList.head
for i in range(int(orta)):
    nNode.nextNode = nNode.nextNode.nextNode

print("Liste Ortasındaki Değer : ")
print(nNode.nextNode.getData())