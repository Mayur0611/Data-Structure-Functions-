
###################################################
#
#   Doubly Circular Linked List
#
###################################################


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLL:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def Display(self):
        if(self.head == None and self.tail == None):
            print("LinkedList is Empty----!")
        else:
            temp = self.head
            print("|",temp.data,"|",end="")
            temp = temp.next
            while(temp != self.tail.next):
                print(temp.data,"|",end="")
                temp = temp.next
            print()

    def Count(self):

        icount = 0

        if(self.head == None and self.tail == None):
            return 0
        else:
            temp = self.head
            icount = icount + 1
            
            temp = temp.next
            while(temp != self.tail.next):
                icount = icount + 1
                temp = temp.next

            return icount

    
            


    


    def InsertFirst(self,data):
        newn = Node(data)

        if(self.head == None and self.tail == None):
            self.head = newn
            self.tail = newn

            

        else:

            newn.next = self.head
            self.head.prev = newn
            self.head = newn

        self.head.prev = self.tail
        self.tail.next = self.head

    def InsertLast(self,data):
        newn = Node(data)

        if(self.head == None and self.tail == None):
            self.head = newn
            self.tail = newn

          

        else:
           self.tail.next = newn
           newn.prev = self.tail
           self.tail = newn

        self.head.prev = self.tail
        self.tail.next = self.head

    def DeleteFirst(self):
        
        if(self.head == None and self.tail == None):
            print("There is no element present in linkedlist")
    
        elif(self.head == self.tail):
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = self.tail

    def DeleteLast(self):
        if(self.head == None and self.tail == None):
            print("There is no element present in linkedlist")
    
        elif(self.head == self.tail):
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.prev
            self.tail.next = self.head

    def InsertAtPos(self,data,ipos):
        iCount = self.Count()

        if(ipos == 1):
            self.InsertFirst(data)
        elif(ipos == iCount + 1):
            self.InsertLast(data)
        else:
            newn = Node(data)
            temp = self.head

            for i in range(1,ipos - 1):
                temp = temp.next
            newn.next = temp.next
            temp.next.prev = newn
            newn.prev = temp
            temp.next = newn


    def DeleteAtPos(self,ipos):
        iCount = self.Count()

        if(ipos == 1):
            self.DeleteFirst()
        elif(ipos == iCount):
            self.DeleteLast()
        else:
            temp = self.head

            for i in range(1,ipos - 1):
                temp = temp.next
            
            temp.next = temp.next.next
            temp.next.prev = temp



    




            
            


        



       

def main():

    DCLL = DoublyCircularLL()

    DCLL.InsertFirst(50)
    DCLL.InsertFirst(40)
    DCLL.InsertFirst(30)
    DCLL.InsertFirst(20)
    DCLL.InsertFirst(10)

    DCLL.InsertLast(60)
    DCLL.InsertLast(70)
    DCLL.InsertLast(80)
    DCLL.InsertLast(90)
    DCLL.InsertLast(100)

    DCLL.Display()
    print("Totle element in LinkedList:{}".format(DCLL.Count()))
    print()

    
    
    DCLL.InsertAtPos(101,3)
    DCLL.Display()
    print("Totle element in LinkedList:{}".format(DCLL.Count()))
    print()

    DCLL.DeleteAtPos(3)
    DCLL.Display()
    print("Totle element in LinkedList:{}".format(DCLL.Count()))
    print()

    

    DCLL.DeleteFirst()
    DCLL.Display()
    print("Totle element in LinkedList:{}".format(DCLL.Count()))
    print()

    DCLL.DeleteLast()
    print("Totle element in LinkedList:{}".format(DCLL.Count()))
    DCLL.Display()


    
if __name__=='__main__':
    main()