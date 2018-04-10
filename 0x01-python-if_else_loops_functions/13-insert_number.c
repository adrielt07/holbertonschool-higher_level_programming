#include "lists.h"

/**
 * insert_node - insert a new node in sorted order
 * @head: takes address of new node
 * @number: value of new node
 * Return: NULL if malloc failed or head is null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *prev, *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	while (current->n < number)
	{
		prev = current;
		current = current->next;
	}
	new->n = number;
	new->next = prev->next;
	prev->next = new;
}
