
###################################################
#
#   STACK Data Structure
#
###################################################


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    
   
    def Display(self):
        if(self.head == None):
            print("Stack is empty")
        else:
            temp = self.head
            
            while (temp != None):
                print("------")
                print("|",temp.data,"|")
                temp = temp.next
            print("------")

    
    def PUSH(self,data):
        #create the new node first:

        newn = Node(data)

        if(self.head == None):
            self.head = newn
        else:
            newn.next = self.head
            self.head = newn


# delete and return top element
    def POP(self):
        PopElm = 0

        if(self.head == None):
            print("Stack is empty")
        else:
            PopElm = self.head.data
            self.head = self.head.next

        return PopElm
            







def main():

   stk = Stack()

   stk.PUSH(50)
   stk.PUSH(40)
   stk.PUSH(30)
   stk.PUSH(20)
   stk.PUSH(10)

   print("Stack :")
   stk.Display()

   elm = stk.POP()

   print("POP element from stack: {}".format(elm))
   print()

   print("stack after POP the element:")
   stk.Display()

   stk.PUSH(10)
   print("Stack after PUSH the element:")
   stk.Display()


if __name__=='__main__':
    main()