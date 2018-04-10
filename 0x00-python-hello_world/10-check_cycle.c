#include "lists.h"

/**
 * check_cycle - checks if list has a cycle
 * @list: takes list
 * Return: 0 if no cycle, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *var1 = list, *var2 = list;

	while (var1 && var2 && var2->next)
	{
		var1 = var1->next;
		var2 = var2->next->next;

		if (var1 == var2)
			return (1);
	}
	return (0);
}
