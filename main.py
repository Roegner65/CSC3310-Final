from skiplist import skiplist
import random
import time

MAXLVL = 4


prob = .75

lst = skiplist(MAXLVL, prob)

inp = input()
while inp != "q":
    if inp == "i":
        toBeInserted = input()
        lst.insertElement(int(toBeInserted))
    elif inp == "s":
        toBeSearched = input()
        lst.searchElement(int(toBeSearched))
    elif inp == "d":
        toBeDeleted = input()
        lst.deleteElement(int(toBeDeleted))
    lst.displayList()
    inp = input()
    

lst = skiplist(20, 0.75)

list = list(range(1, 50000))

for i in list:
    lst.insertElement(i)

start = time.time()
for element in list:
    if element == 25000:
        break
stop = time.time()

print("Regular list find:", stop - start)

start = time.time()
lst.searchElement(25000)
stop = time.time()

print("Skip List find:", stop - start)

# lst.insertElement(35)
# lst.insertElement(3)
# lst.insertElement(6)
# lst.insertElement(7)
# lst.insertElement(9)
# lst.insertElement(12)
# lst.insertElement(19)

# lst.insertElement(17)

# lst.insertElement(26)
# lst.insertElement(21)
# lst.insertElement(25)
# lst.displayList()

# lst.searchElement(19)
# lst.searchElement(25)
# lst.searchElement(9)
# lst.searchElement(5)
# lst.searchElement(55)

# lst.deleteElement(25)
# lst.displayList()

# lst.deleteElement(7)
# lst.displayList()

# lst.deleteElement(3)
# lst.displayList()

# lst.deleteElement(17)
# lst.displayList()