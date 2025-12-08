from linkedlist import LinkedList

class skiplist:
    class Node:
        data = 0.0
        pointers = []

        def Node(self, data):
            self.data = data
        
        def addChild(self, index):
            self.pointers.append(index)


    
    underlying_list = LinkedList()
    
    def skiplist(self):
        pass

    def addNode(self, data):
        pass



