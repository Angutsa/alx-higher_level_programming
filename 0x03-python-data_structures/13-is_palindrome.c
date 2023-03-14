#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: pointer to head node of the singly linked list
  * Return: 0 if not a palindrome and 1 if it's a palindrome. An empty list
  * is considered a palindrome
  */
int is_palindrome(listint_t **head)
{
	int size, i, *values = NULL;
	listint_t *node = *head;

	if (head == NULL || node == NULL)
		return (1);

	if ((*head)->next == NULL)
		return (0);

	for (size = 0; node != NULL; size++)
	{
		node = node->next;
	}

	node = *head;
	values = malloc(sizeof(int) * size);
	for (i = 0; node != NULL; i++)
	{
		*(values + i) = node->n;
		node = node->next;
	}

	size--;
	for (i = 0; i <= size / 2; i++)
	{
		if (*(values + i) != *(values + (size - i)))
		{
			free(values);
			return (0);
		}
	}

	free(values);
	return (1);
}
