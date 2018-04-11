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

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (current->n > number)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current->n < number && current->next != NULL)
	{
		prev = current;
		current = current->next;
	}
	if (current->next == NULL)
	{
		new->next = NULL;
		current->next = new;
	}
	else
	{
		new->next = prev->next;
		prev->next = new;
	}
	return (new);
}
