from skiplist import skiplist

MAXLVL = 4


prob = .75

lst = skiplist(MAXLVL, prob)

lst.insertElement(35)
lst.insertElement(3)
lst.insertElement(6)
lst.insertElement(7)
lst.insertElement(9)
lst.insertElement(12)
lst.insertElement(19)

lst.insertElement(17)

lst.insertElement(26)
lst.insertElement(21)
lst.insertElement(25)
lst.displayList()

lst.searchElement(19)
lst.searchElement(25)
lst.searchElement(9)
lst.searchElement(5)
lst.searchElement(55)

lst.deleteElement(25)
lst.displayList()

lst.deleteElement(7)
lst.displayList()

lst.deleteElement(3)
lst.displayList()

lst.deleteElement(17)
lst.displayList()