//  Functions for singly Linked List(linear & Circular)

#include<iostream>
using namespace std;

struct node
{
    int data;
    struct node *next;
};

typedef struct node NODE;
typedef struct node* PNODE;

// Functions for Singly Linear LinkedList:
class SinglyLL
{
    public:
        PNODE head;
        int iCount;

        SinglyLL()
        {
            head = NULL;
            iCount = 0;
        }

        void Display()
        {
            PNODE temp = head;

            cout<<"Elements of LinkedList are : \n";

            while(temp != NULL)
            {
                cout<<"| "<<temp->data<<" | -> ";
                temp = temp -> next;
            }

            cout<<"NULL\n";
        }
        
        int Count()
        {
            return iCount;
        }

        void InsertFirst(int no)
        {
            PNODE newn = NULL;

            newn = new NODE;    
            newn->data = no;
            newn->next = NULL;

            if(head == NULL)
            {
                head = newn;
            }
            else
            {
                newn->next = head;
                head = newn;
            }
            iCount++;
        }

        void InsertLast(int no)
        {
            PNODE newn = NULL;
            PNODE temp = NULL;

            newn = new NODE;   
            newn->data = no;
            newn->next = NULL;

            if(head == NULL)
            {
                head = newn;
            }
            else
            {
                temp = head;

                while(temp -> next != NULL)
                {
                    temp = temp -> next;
                }

                temp->next = newn;
            }
            iCount++;
        }
        
        void InsertAtPos(int no , int ipos)
        {
            int i = 0;
            PNODE newn = NULL;
            PNODE temp = NULL;

            if((ipos < 1) || (ipos > iCount+1))
            {
                cout<<"Invalid position\n";
                return;
            }

            if(ipos == 1)
            {
                InsertFirst(no);
            }
            else if(ipos == iCount + 1)
            {
                InsertLast(no);
            }
            else
            {
                newn = new NODE;
                newn->data = no;
                newn->next = NULL;

                temp = head;

                for(i =1; i< ipos -1; i++)
                {
                    temp = temp->next;
                }

                newn->next = temp->next;
                temp->next = newn;

                iCount++;
            }
        }

        void DeleteFirst()
        {
            PNODE temp = NULL;

            if(head == NULL)
            {
                return;
            }
            else if(head->next == NULL)
            {
                delete head;
                head = NULL;
            }
            else
            {
                temp = head;

                head = head -> next;
                delete temp;
                
            }
            iCount--;
        }
        
        void DeleteLast()
        {
            PNODE temp = NULL;

            if(head == NULL)
            {
                return;
            }
            else if(head->next == NULL)
            {
                delete head;
                head = NULL;
            }
            else
            {
                temp = head;

                while(temp->next->next != NULL)
                {
                    temp = temp -> next;
                }

                delete temp->next;
                temp->next = NULL;
            }
            iCount--;
        }
        
        void DeleteAtPos(int ipos)
        {
            int i = 0;
            PNODE temp = NULL;
            PNODE target = NULL;

            if((ipos < 1) || (ipos > iCount))
            {
                cout<<"Invalid position\n";
                return;
            }

            if(ipos == 1)
            {
                DeleteFirst();
            }
            else if(ipos == iCount)
            {
                DeleteLast();
            }
            else
            {
                temp = head;

                for(i =1; i< ipos -1; i++)
                {
                    temp = temp->next;
                }

                target = temp->next;

                temp -> next = target->next;
                delete target;

                iCount--;
            }
        }        
};

// Functions for Singly circular LinkedList:
class SinglyCL
{
    public:
        PNODE head;
        PNODE tail;
        int iCount;

        SinglyCL()
        {
            head = NULL;
            tail = NULL;
            iCount = 0;
        }

        void Display()
        {
            PNODE temp = NULL;

            if(head == NULL & tail == NULL)
            {
                cout<<"LinkedList is empty";
                return;
            }

            temp = head;

            do
            {
                cout<<"|"<<temp->data<<"|->";
                temp = temp->next;
            }while(temp != tail->next);

            cout<<"\n";
        }

        int Count()
        {
            return iCount;
        }
        

        void InsertFirst(int no)
        {
            PNODE newn  = NULL;

            newn = new NODE;
            newn->data = no;
            newn->next = NULL;

            if(head == NULL && tail == NULL)
            {
                head = newn;
                tail = newn;
                tail->next = head;
            }
            else
            {
                newn->next = head;
                head = newn;
                tail->next = head;
            }
            iCount++;
        }
    
        void InsertLast(int no)
        {
            
            PNODE newn  = NULL;

            newn = new NODE;
            newn->data = no;
            newn->next = NULL;

            if(head == NULL && tail == NULL)
            {
                head = newn;
                tail = newn;
                tail->next = head;
            }
            else
            {
                tail->next = newn;
                tail = newn;
                tail->next = head;
            }
            iCount++;
        }

        void InsertAtPos(int no, int ipos)
        {
            int CountNode = 0;
            int iCnt = 0;

            PNODE temp = NULL;
            PNODE newn = NULL;

            CountNode = Count();

            if(ipos < 1 || ipos > CountNode + 1)
            {
                cout<<"Invalid Position";
                return;
            }

            if(ipos == 1)
            {
                InsertFirst(no);
            }
            else if(ipos == CountNode + 1)
            {
                InsertLast(no);
            }
            else
            {
                newn = new NODE;
                newn->data = no;
                newn->next = NULL;

                temp = head;

                for(iCnt = 1; iCnt < ipos - 1; iCnt++)
                {
                    temp = temp->next;
                }
                newn->next = temp->next;
                temp->next = newn;

                iCount++;
            }
        }

        void DeleteFirst()
        {
            PNODE  temp = NULL;

            if(head == NULL && tail == NULL)
            {
                return;
            }
            else if(head == tail)
            {
                delete head;
                head = NULL;
                tail = NULL;
            }
            else
            {
                temp = head;

                head = temp->next;
                tail->next = head;
                delete temp;

                iCount--;
            }
        }

        void DeleteLast()
        {
            PNODE  temp = NULL;

            if(head == NULL && tail == NULL)
            {
                return;
            }
            else if(head == tail)
            {
                delete head;
                head = NULL;
                tail = NULL;
            }
            else
            {
                temp = head;

                while(temp->next != tail)
                {
                    temp = temp->next;
                }
                delete temp->next;
                tail = temp;
                temp->next = head;   

                iCount--;
            }
        }
        
        void DeleteAtPos(int ipos)
        {
            int CountNode = 0;
            int iCnt = 0;

            PNODE temp = NULL;
            PNODE target= NULL;

            CountNode = Count();

            if(ipos < 1 || ipos > CountNode)
            {
                cout<<"Invalid Position";
                return;
            }

            if(ipos == 1)
            {
                DeleteFirst();
            }
            else if(ipos == CountNode )
            {
                DeleteLast();
            }
            else
            {
                temp = head;

                for(iCnt = 1; iCnt < ipos - 1; iCnt++)
                {
                    temp = temp->next;
                }
                target = temp->next;
                temp->next = target->next;
                delete target;
               
                iCount--;
            }
        }
};


int main()
{
    SinglyLL SLobj;
    SinglyCL SCobj;
     
}