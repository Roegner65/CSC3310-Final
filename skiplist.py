import random

class Node:
    
    def __init__ (self, key, level):
        self.key = key
        self.forward = []

        for c in range(level + 1):
            self.forward.append(None)

        print(self.forward)
        print(self)


class skiplist:

    def __init__ (self, maxLevel, P):
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

        for i in range(self.level, -1, -1):
            while (current.forward[i] != None and current.forward[i].key < key and current.forward[i] != self):
                current = current.forward[i]

            update.append(current)
        

        current = current.forward[0]

        if current == None or current.key != key: 
            rlevel = self.randomLevel()

            if (rlevel > self.level):

                for i in range(self.level + 1, rlevel+1):
                    update.append(self.head)
                
                self.level = rlevel
            

            n = self.createNode(key, rlevel)

            for i in range(rlevel + 1):
                n.forward.append(update[i].forward[i-1])
                update[i].forward[i] = n
            print("Successfully Inserted key " + str(key) + "\n")


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
            print("Found key: " + str(key))
        else:
            print("Not Found")

    def displayList(self):
        print("\n*****Skip List*****\n")
        string = ""
        for i in range(0, self.level+1):
            node = self.head.forward[i]
            string += ("Level " + str(i) + ": ")
            while (node != None):
                string += (str(node.key) + " ")
                node = node.forward[i]
            string += "\n"
        print(string)
        
    



