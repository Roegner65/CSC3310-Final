import random

class Node:

    forward = []
    
    def __init__ (self, key, level):
        self.key = key

        for c in range(level + 1):
            self.forward.append(None)
        


class skiplist:

    def skiplist (self, maxLevel, P):
        self.maxLevel = maxLevel
        self.P = P
        self.level = 0
        self.head = Node(-1, maxLevel)

    def randomLevel(self):
        r = random.random()
        lvl = 0
        while (r < self.P and lvl < self.maxLevel):
            lvl += 1
            r = random.random()
        return lvl

    def createNode(self, key, level):
        n = Node(key, level)
        return n

    def insertElement(self, key):
        current = self.head
        update = []

        for i in range(self.level, 0, -1):
            while (current.forward[i] != None and current.forward[i].key < key):
                current = current.forward[i]
            update[i] = current
        

        current = current.forward[0]

        if current == None or current.key != key: 
            rlevel = self.randomLevel()

            if (rlevel > self.level):

                for i in range(self.level + 1, rlevel+1):
                    update[i] = self.head
                
                self.level = rlevel
            

            n = self.createNode(key, rlevel)

            for i in range(rlevel + 1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n
            print("Successfully Inserted key " + key + "\n")


    def searchElement(self, key):
        current = self.head
        print("\n---------------------\n")
        for i in range(self.level, -1, -1):
            while (current.forward[i] != None and current.forward[i].key < key):
                current = current.forward[i]

        if (current.forward[0] == None):
            print("Not Found")
            return

        current = current.forward[0]

        if (current.key == key):
            print("Found key: " + key)
        else:
            print("Not Found")
        
    



