'''
----------------------------------
#Developed by                     |
@user: Dennis Masaya              |
#id: 201503413                    |
#e-mail: dennismasaya@gmail.com   |
----------------------------------
This example demonstrates how to build a Linked List,
we only need 2 classes: 1)Node and 2)LinkedList, our
node class only has a constructor that assigns the value
to the attribute @id of the node and the link to the next
node. Our LinkedList class has 2 methods (more can be
easily implemented) 2.1)add() and 2.2)print_list(), which
are self explanatory, finally to put our linked list to the
test, we instanciate it, we add a couple of values and
finally print it.
'''

class Node:
    #Remember that we do not need to declare our class attributes
    #in Python, only assign those attributes through our constructor
    def __init__(self, id): #constructor of class Node
        self.id = id  #assign the value sent as a parameter to our class atribute
        self.next = None #assign the pointer link to None (null)


class LinkedList:
    def __init__(self): #constructor of class LinkedList
        self.head = None #start our list empty, hence our head is None (null)

    #ADD method
    def add(self,node):
        if self.head is None: #verify if our LinkedList is empty
            self.head = node # if is empty assign the first node to our head
        else:
            temp = self.head
            while temp.next is not None: #iterate through our list until-
                temp = temp.next         #-we reach the end of it
            temp.next = node #assign the pointer link of the last -
                             #-element to our new element
    #PRINT method
    def print_list(self):
        if self.head is None: #verify if our LinkedList is empty
            print('The list is empty') #print a warning
        else:
            temp = self.head
            while temp.next is not None: #iterate our list printing each element-
                print(temp.id,end='')    #-as we go
                print('->',end='')
                temp = temp.next
            print(temp.id) #print the las element in order to avoid [1->2->3->]-
                           #-the last link pointing tu None (null)

list = LinkedList() #create a new LinkedList
list.add(Node(1)) #add element 1
list.add(Node(2)) #add element 2
list.add(Node(3)) #add element 3
list.print_list() #print the list
