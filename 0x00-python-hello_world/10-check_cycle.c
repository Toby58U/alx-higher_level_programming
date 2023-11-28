#include "lists.h"

/**
 * check_cycle - check for loop in LL
 * @list: head of linked list
 *
 * Description - check for loops in LL
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *list)
{
    listint_t *tortoise = list, *hare = list;

    while (tortoise != NULL && hare != NULL && hare->next != NULL)
    {
        tortoise = tortoise->next;      /* Move at a slower pace */
        hare = hare->next->next;       /* Move at a faster pace */

        if (tortoise == hare)
            return 1;  /* Cycle detected */
    }

    return 0;  /* No cycle detected */
}
