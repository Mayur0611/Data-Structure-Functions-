// Functions for Singly Circular LinkedList:

#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
};

typedef struct node NODE;
typedef struct node* PNODE;
typedef struct node** PPNODE;

// Display Element
void Display(PNODE head, PNODE tail)
{
    if(head == NULL && tail == NULL)
    {
        printf("Linked List is empty\n");
        return;
    }
    
    printf("Elements of LinkedList are : \n");

    do
    {
        printf("| %d | -> ",head->data);
        head = head -> next;
    }while(head != tail -> next);

    printf("\n");
}

// Count Elements
int Count(PNODE head, PNODE tail)
{
    int iCount = 0;

    if(head == NULL && tail == NULL)
    {
        return 0;
    }

    do
    {
        iCount++;
        head = head -> next;
    }while(head != tail -> next);

    return iCount;
}

// Insert element at 1st position
void InsertFirst(PPNODE head, PPNODE tail, int no)
{
    PNODE newn = NULL;

    newn = (PNODE)malloc(sizeof(NODE));
    newn->data = no;
    newn->next = NULL;

    if((*head == NULL) && (*tail == NULL))    // LL is empty
    {
        *head = newn;
        *tail = newn;
    }
    else
    {
        newn->next = *head;
        *head = newn;
    }
    (*tail) -> next = *head;
}

// Insert element at last position
void InsertLast(PPNODE head, PPNODE tail, int no)
{
    PNODE newn = NULL;

    newn = (PNODE)malloc(sizeof(NODE));
    newn->data = no;
    newn->next = NULL;

    if((*head == NULL) && (*tail == NULL))    // LL is empty
    {
        *head = newn;
        *tail = newn;
    }
    else
    {
        (*tail)->next = newn;
        *tail = newn;
    }
    (*tail) -> next = *head;
}

//  Insert element at particular(user given) position
void InsertAtPos(PPNODE head, PPNODE tail, int no, int ipos)
{
    int iCount = 0;
    int i = 0;

    PNODE newn = NULL;
    PNODE temp = NULL;

    iCount = Count(*head, *tail);

    if(ipos < 1 || ipos > iCount+1)
    {
        printf("Invalid position \n");
        return;
    }

    if(ipos == 1)
    {
        InsertFirst(head, tail, no);
    }
    else if(ipos == iCount+1)
    {
        InsertLast(head,tail,no);
    }
    else
    {
        newn = (PNODE)malloc(sizeof(NODE));
        newn->data = no;
        newn->next = NULL;

        temp = *head;

        for(i = 1; i < ipos-1; i++)
        {
            temp = temp -> next;
        }

        newn->next = temp->next;
        temp->next = newn;
    }
}

// Delete first element
void DeleteFirst(PPNODE head, PPNODE tail)  // with temp
{
    PNODE temp = NULL;
    if((*head == NULL) && (*tail == NULL))
    {
        return;
    }
    else if(*head == *tail)
    {
        free(*head);
        *head = NULL;
        *tail = NULL;
    }
    else
    {
        temp = *head;

        *head = (*head) -> next;
        free(temp);
        (*tail)->next = *head;
    }
}


// Delete last element
void DeleteLast(PPNODE head, PPNODE tail)
{
    PNODE temp = NULL;

    if((*head == NULL) && (*tail == NULL))
    {
        return;
    }
    else if(*head == *tail)
    {
        free(*head);
        *head = NULL;
        *tail = NULL;
    }
    else
    {
        temp = *head;

        while(temp->next != *tail)
        {
            temp = temp -> next;
        }

        free(temp->next);
        *tail = temp;
        (*tail)->next = *head;
    }
}

// Delete element at particular position
void DeleteAtPos(PPNODE head, PPNODE tail,int ipos)
{
    int iCount = 0;
    int i = 0;

    PNODE temp = NULL;
    PNODE target = NULL;

    iCount = Count(*head, *tail);

    if(ipos < 1 || ipos > iCount)
    {
        printf("Invalid position \n");
        return;
    }

    if(ipos == 1)
    {
        DeleteFirst(head, tail);
    }
    else if(ipos == iCount)
    {
        DeleteLast(head,tail);
    }
    else
    {
        temp = *head;

        for(i = 1; i < ipos-1; i++)
        {
            temp = temp -> next;
        }

        target = temp->next;

        temp->next = target->next;
        free(target);
    }
}
