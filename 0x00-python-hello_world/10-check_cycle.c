#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * check_cycle - Check if a singly linked list has a cycle
 * @list: Pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
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

/* Example usage */
int main(void)
{
	listint_t *head = NULL;
	listint_t *node1, *node2, *node3;

	node1 = malloc(sizeof(listint_t));
	node2 = malloc(sizeof(listint_t));
	node3 = malloc(sizeof(listint_t));

	if (node1 && node2 && node3)
	{
		node1->n = 1;
		node2->n = 2;
		node3->n = 3;

		node1->next = node2;
		node2->next = node3;
		node3->next = node1;  /* Cycle: node3 points back to node1 */

		head = node1;

		/* Check for a cycle */
		if (check_cycle(head))
			printf("Linked list has a cycle\n");
		else
			printf("Linked list does not have a cycle\n");

		/* Clean up: free allocated memory */
		free(node1);
		free(node2);
		free(node3);
	}

	return 0;
}

