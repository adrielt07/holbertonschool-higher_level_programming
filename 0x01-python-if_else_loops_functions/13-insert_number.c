#include "lists.h"

/**
 * insert_node - insert a new node in sorted order
 * @head: takes address of new node
 * @number: value of new node
 * Return: NULL if malloc failed or head is null
 * else return new linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *prev, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (head == NULL)
	{
		*head = new;
		return (new);
	}

	if (current->n > number)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current->next != NULL)
	{
		if (current->n > number)
			break;
		prev = current;
		current = current->next;
	}
	if (current->n > number)
	{
		new->next = prev->next;
		prev->next = new;
		return (new);
	}
	else if (current->next == NULL)
	{
		new->next = NULL;
		current->next = new;
		return (new);
	}
	return (new);
}
