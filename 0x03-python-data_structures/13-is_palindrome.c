#include "lists.h"

/**
 * len_list - gets the len of linked list
 * @head: pointer to the list
 * Return: length of list
 */
int len_list(listint_t *head)
{
	int i = 0;

	while (head)
	{
		head = head->next;
		i++;
	}
	return (i);
}

/**
 * is_palindrome - checks if the list is palindrome
 * @head: pointer to address of list
 * Return: 1 if palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	unsigned int *list;
	int i = 0, len = len_list(*head) - 1, j = 0;
	listint_t *current = *head;

	list = malloc(sizeof(unsigned int *) * len);

	while (current)
	{
		list[i] = current->n;
		current = current->next;
		i++;
	}

	while (len >= 0)
	{
		if (list[len] != list[j])
		{
			free(list);
			return (0);
		}
		len--;
		j++;
	}
	free(list);
	return (1);
}
