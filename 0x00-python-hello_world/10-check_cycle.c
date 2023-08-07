#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *list1 = list;
	listint_t *check = list;

	if (!list)
		return (0);

	while (list1 && check && check->next)
	{
		list1 = list1->next;
		check = check->next->next;
		if (list1 == check)
			return (1);
	}
	return (0);
}
