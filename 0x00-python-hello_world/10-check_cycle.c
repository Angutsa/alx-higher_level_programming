#include "lists.h"
#include <stddef.h>
#include <stdio.h>

/**
  * check_cycle - checks if a singly linked list has a cycle in it
  * @list: singly linked list to check
  * Return: 0 if there is no cycle or 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *node = list;

	do {
		if (node == NULL)
			return (0);

		node = node->next;
	} while (node != list);

	return (1);
}
