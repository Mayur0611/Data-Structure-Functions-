###########################################
# SinglyCircular linkedlist
############################################


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SinglyCircularLL:
    def __init__(self):
        self.head = None
        self.tail = None


    def Display(self):
        if(self.head == None and self.tail == None):
            print("Linked List is empty")
            return
        else:
            temp = self.head

            print("|",end="")

            print(temp.data,end="")
            temp = temp.next
        

            while(temp != self.tail.next):
                print("|",temp.data,end="")
                temp = temp.next

            print("|",end="")
            print()


    def Count(self):
        if(self.head == None and self.tail == None):
            print("Linked List is empty")
            return
        else:
            iCnt = 1

            temp = self.head
            temp = temp.next
        
            while(temp != self.tail.next):
                iCnt = iCnt + 1
                temp = temp.next

        return iCnt

            

    def InsertFirst(self,data):
        newn = Node(data)

        if(self.head == None and self.tail == None):
            self.head = newn
            self.tail = newn

            self.tail.next = self.head

        else:
            newn.next = self.head
            self.head = newn 

            self.tail.next = self.head

    def InsertLast(self,data):
        newn = Node(data)

        if(self.head == None and self.tail == None):
            self.head = newn
            self.tail = newn

            self.tail.next = self.head
        else:

            newn.next = self.head
            self.tail.next = newn
            self.tail = newn

    def DeleteFirst(self):
        if(self.head == None and self.tail == None):
            print("LinkedList is empty")
        elif(self.head == self.tail):
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def DeleteLast(self):
        if(self.head == None and self.tail == None):
            print("LinkedList is empty")
        elif(self.head == self.tail):
            self.head = None
            self.tail = None
        else:
            temp = self.head

            while(temp.next != self.tail):
                temp = temp.next

            self.tail = temp
            temp.next = self.head

    def InsertAtPos(self,data,ipos):

        iCount = self.Count()

        if(ipos == 1):
            self.InsertFirst(data)
        elif(ipos == iCount + 1):
            self.InsertLast(data)
        else:
            temp = self.head
            newn = Node(data)

            for i in range(1, ipos-1):
                temp = temp.next
            newn.next = temp.next
            temp.next = newn

    def DeleteAtPos(self,ipos):
        iCount = self.Count()

        if(ipos == 1):
            self.DeleteFirst()
        elif(ipos == iCount):
            self.DeleteLast()
        else:
            temp = self.head

            for i in range(1, ipos-1):
                temp = temp.next
            temp.next = temp.next.next
                


    

def main():

    SCLL  = SinglyCircularLL()

    SCLL.InsertFirst(40)
    SCLL.InsertFirst(30)
    SCLL.InsertFirst(20)
    SCLL.InsertFirst(10)

    SCLL.Display()
    count = SCLL.Count()
    print("Totle elements in LinkedList:{}".format(count))

    SCLL.InsertLast(50)
    SCLL.InsertLast(60)
    SCLL.InsertLast(70)
    SCLL.InsertLast(80)

    
    SCLL.Display()
    count = SCLL.Count()
    print("Totle elements in LinkedList:{}".format(count))


    SCLL.InsertAtPos(100,4)
    SCLL.Display()
    count = SCLL.Count()
    print("Totle elements in LinkedList:{}".format(count))

    SCLL.DeleteAtPos(4)
    SCLL.Display()
    count = SCLL.Count()
    print("Totle elements in LinkedList:{}".format(count))


    SCLL.DeleteFirst()
    SCLL.Display()
    count = SCLL.Count()
    print("Totle elements in LinkedList:{}".format(count))

    SCLL.DeleteLast()
    SCLL.Display()
    count = SCLL.Count()
    print("Totle elements in LinkedList:{}".format(count))



if __name__=='__main__':
    main()