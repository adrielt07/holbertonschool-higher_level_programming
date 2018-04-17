#include "lists.h"
#define buffer 1024
#include <stdio.h>

/**
 * len_list - gets the len of linked list
 * @head: pointer to the list
 * Return: length of list
 */
int len_list(listint_t *head)
{
	int i = 0;
	while(head)
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
	int list[buffer];
	int i = 0, len = len_list(*head), j = 0;
	listint_t *current = *head;

/*	if (current == NULL)
		return (0);
	if (current->next)
		return (1);
*/
	while(current)
	{
		list[i] = current->n;
		printf("value of list[%d]: is [%d]\n", i, current->n);
		current = current->next;
		i++;
	}
	len--;
	while (len >= 0)
	{
		if (list[len] != list[j])
			return (0);
		len--;
		j++;
	}
	return (1);
}
