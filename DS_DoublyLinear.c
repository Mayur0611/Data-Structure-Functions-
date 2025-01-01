// Functions for Doubly Linear LinkedList:

#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
    struct node *prev;
};

typedef struct node NODE;
typedef struct node* PNODE;
typedef struct node** PPNODE;


// Display Element
void Display(PNODE head)
{
    printf("Elements of the LinkedList are : \n");

    printf("NULL <=> ");
    while(head != NULL)
    {
        printf("| %d | <=> ",head->data);
        head = head->next;  
    }
    printf("NULL\n");

}


// Count Elements
int Count(PNODE head)
{
    int iCount = 0;

    while(head != NULL)
    {
        iCount++;
        head = head -> next;
    }
    return iCount;
}

// Insert element at 1st position
void InsertFirst(PPNODE head,  int no)
{
    PNODE newn = NULL;

    newn = (PNODE)malloc(sizeof(NODE));
    newn->data = no;
    newn->next = NULL;
    newn->prev = NULL;

    if(*head == NULL)
    {
        *head = newn;
    }
    else
    {
        newn->next = *head;
        (*head)->prev = newn;
        *head = newn;
    }
}

// Insert element at last position
void InsertLast(PPNODE head,  int no)
{
    PNODE newn = NULL;
    PNODE temp = NULL;

    newn = (PNODE)malloc(sizeof(NODE));
    newn->data = no;
    newn->next = NULL;
    newn->prev = NULL;

    if(*head == NULL)
    {
        *head = newn;
    }
    else
    {
        temp = *head;

        while(temp->next != NULL)
        {
            temp = temp -> next;
        }

        temp->next = newn;
        newn->prev = temp;
    }
}

//  Insert element at particular(user given) position
void InsertAtPos(PPNODE head,  int no, int ipos)
{
    int CountNode = 0;
    int i = 0;

    PNODE temp = NULL;
    PNODE newn = NULL;

    CountNode = Count(*head);

    if((ipos < 1) || (ipos > CountNode + 1))
    {
        printf("Invalid Position\n");
        return;
    }

    if(ipos == 1)
    {
        InsertFirst(head,no);
    }
    else if(ipos == CountNode + 1)
    {
        InsertLast(head,no);
    }
    else
    {
        newn = (PNODE)malloc(sizeof(NODE));

        newn->data = no;
        newn->next = NULL;
        newn->prev = NULL;

        temp = *head;

        for(i = 1; i < ipos -1; i++)
        {
            temp = temp -> next;
        }

        newn->next = temp->next;    
        temp->next->prev = newn;   
        temp->next = newn;         
        newn->prev = temp;         
    }
}

// Delete first element
void DeleteFirst(PPNODE head)
{
    if(*head == NULL)   
    {
        return;
    }
    else if((*head)->next == NULL)  
    {
        free(*head);
        *head = NULL;
    }
    else    // case3
    {
        *head = (*head) -> next;
        free((*head)->prev);        
        (*head)->prev = NULL;         
    }
}


// Delete last element
void DeleteLast(PPNODE head)
{
    PNODE temp = NULL;

    if(*head == NULL)   // case1 
    {
        return;
    }
    else if((*head)->next == NULL)  // case2
    {
        free(*head);
        *head = NULL;
    }
    else    // case3
    {
        temp = *head;

        while(temp->next->next != NULL)
        {
            temp = temp -> next;
        }

        free(temp->next);
        temp->next = NULL;
    }
}

// Delete element at particular position
void DeleteAtPos(PPNODE head, int ipos)
{
    int CountNode = 0;
    int i = 0;

    PNODE temp = NULL;
    PNODE target = NULL;

    CountNode = Count(*head);

    if((ipos < 1) || (ipos > CountNode))
    {
        printf("Invalid Position\n");
        return;
    }

    if(ipos == 1)
    {
        DeleteFirst(head);
    }
    else if(ipos == CountNode)
    {
        DeleteLast(head);
    }
    else
    {
        temp = *head;

        for(i =1; i < ipos - 1; i++)
        {
            temp = temp -> next;
        }

        target = temp->next;

        temp->next = target -> next;    
        free(target);                    
    }   
}
