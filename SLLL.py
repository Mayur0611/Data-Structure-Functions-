###########################################
# Singly Linear linkedlist
############################################

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None


    def Display(self):
        if self.head == None:
            print("linkedList is empty")
        else:
            n = self.head
            while n != None:
                print(n.data,end=" ")
                n = n.next
        print()

    def Count(self):

        icnt = 0

        if self.head == None:
            print("linkedList is empty")
        else:
            n = self.head
            while (n != None):
                icnt += 1  
                n = n.next

        return icnt



    def Insert_First(self,data):
        #create the new node first:

        newn = Node(data)

        if (self.head == None):
            self.head = newn
        else:
            newn.next = self.head
            self.head = newn

    def Insert_Last(self,data):

        newn = Node(data)

   

        if(self.head == None):
            self.head = newn

        else:
                temp = self.head

                while (temp.next != None):
                    temp =  temp.next

                temp.next = newn


                
    def Delete_First(self):
        if(self.head == None):
            print("linkedlist is empty")
        elif(self.head.next == None):
            self.head = None
        else:
            self.head = self.head.next

    def Delete_Last(self):
        if(self.head == None):
            print("linkedlist is empty")
        elif(self.head.next == None):
            self.head = None
        else:
            temp = self.head

            while(temp.next.next != None):
                temp = temp.next
                
            temp.next = None

    def InsertAtPos(self,data,pos):

        
        iCount = self.Count()

        if(pos == 1):
            self.Insert_First(data)
        elif(pos == iCount + 1):
            self.Insert_Last(data)
        else:
            newn = Node(data)
            temp = self.head

            for i in range(1,pos-1):
                temp = temp.next
            newn.next = temp.next
            temp.next = newn


    def DeleteAtPos(self,pos):

        
        iCount = self.Count()

        if(pos == 1):
            self.Delete_First()
        elif(pos == iCount ):
            self.Delete_Last()
        else:

            temp = self.head

            for i in range(1,pos-1):
                temp = temp.next
            
            temp.next = temp.next.next
             


        
            
                

    

       
def main():

    LL = SinglyLL()
    LL.Insert_First(40)
    LL.Insert_First(30)
    LL.Insert_First(20)
    LL.Insert_First(10)

    

    LL.Display()
    count = LL.Count()
    print("Total Count of element:" , count)
    print()
  

    LL.Insert_Last(50)
    LL.Insert_Last(60)

    LL.Display()
    count = LL.Count()
    print("Total Count of element:" , count)
    print()

    #LL.Delete_First()
   # LL.Display()
    #count = LL.Count()
    #print("Total Count of element:" , count)
    #print()

   # LL.Delete_Last()
    #LL.Display()
    #count = LL.Count()
    #print("Total Count of element:" , count)

    LL.InsertAtPos(100,4)
    LL.Display()
    count = LL.Count()
    print("Total Count of element:" , count)

    LL.DeleteAtPos(6)
    LL.Display()
    count = LL.Count()
    print("Total Count of element:" , count)




 
        


if __name__=='__main__':
    main()
    