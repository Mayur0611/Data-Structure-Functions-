
###################################################
#
#   Doubly Linear Linked List
#
###################################################


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None



class DoublyLL:
    def __init__(self):
        self.head = None


    def Display(self):
        if(self.head == None):
            print("LinkedList is Empty--------!")
        else:
            temp = self.head
            
            while(temp != None):
                print("|",end="")
                print(temp.data,"|<=>",end="")
                temp = temp.next
            print()

    
    def Count(self):
        if(self.head == None):
            print("Linked List is Empty--------------!")

        else:
            temp = self.head
            iCount = 0

            while(temp != None):
                iCount = iCount + 1
                temp = temp.next
            return iCount
        





    def InsertFirst(self,data):
        newn = Node(data)

        if(self.head == None):
            self.head = newn
        else:
            newn.next = self.head
            self.head.prev = newn
            self.head = newn

    def InsertLast(self,data):
        newn = Node(data)

        if(self.head == None):
            self.head = newn
        else:
            if(self.head == None):
                self.head = newn
            else:
                temp = self.head

                while(temp.next  != None):
                    temp = temp.next
                temp.next = newn
                newn.prev = temp
                    

    def DeleteFirst(self):
        if(self.head == None):
            print("LinkedList is empty---------!")
        elif(self.head.next == None):
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def DeleteLast(self):
        if(self.head == None):
            print("LinkedList is empty---------!")
        elif(self.head.next == None):
            self.head = None
        else:
            temp = self.head

            while(temp.next.next != None ):
                temp = temp.next
            temp.next = None

    
    def InsertAtPos(self,data,ipos):
        newn = Node(data)
        Tcount = self.Count()

        if(ipos == 1):
            self.InsertFirst(data)
        elif(ipos == Tcount + 1):
            self.InsertLast(data)
        else:
            temp = self.head

            for i in range(1,ipos -1):
                temp = temp.next
            newn.next = temp.next
            newn.prev = temp
            temp.next = newn

    def DeleteAtPos(self,ipos):
        Tcount = self.Count()

      

        
        if(ipos == 1):
            self.DeleteFirst()
        elif(ipos == Tcount):
            self.DeleteLast()
        else:
            temp = self.head

            for i in range(1,ipos - 1):
                temp = temp.next
            temp.next = temp.next.next
            temp.next.prev = temp


            

                

def main():

    DLL = DoublyLL()

    DLL.InsertFirst(30)
    DLL.InsertFirst(20)
    DLL.InsertFirst(10)


    DLL.InsertLast(40)
    DLL.InsertLast(50)
    DLL.InsertLast(60)

    
    DLL.Display()
    print("Total Count of Element in LinkedList:{}".format(DLL.Count()))
    print()

    
   

    DLL.InsertAtPos(10.5,2)
    DLL.InsertAtPos(20.5,4)
    DLL.InsertAtPos(30.5,6)
    DLL.InsertAtPos(40.5,8)
    DLL.InsertAtPos(50.5,10)
    DLL.InsertAtPos(60.5,12)

    DLL.Display()
    print("Total Count of Element in LinkedList:{}".format(DLL.Count()))
    print()

    DLL.DeleteAtPos(1)
    DLL.DeleteAtPos(2)
    DLL.DeleteAtPos(3)
    DLL.DeleteAtPos(4)
    DLL.DeleteAtPos(5)
    DLL.DeleteAtPos(6)
    
    DLL.Display()
    print("Total Count of Element in LinkedList:{}".format(DLL.Count()))
    print()


    DLL.DeleteFirst()
    DLL.Display()
    print("Total Count of Element in LinkedList:{}".format(DLL.Count()))
    print()

    DLL.DeleteLast()
    DLL.Display()
    print("Total Count of Element in LinkedList:{}".format(DLL.Count()))
    print()



if __name__=='__main__':
    main()