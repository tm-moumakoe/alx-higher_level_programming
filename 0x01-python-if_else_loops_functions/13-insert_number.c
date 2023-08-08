#include "lists.h"
/**
* insert_node - Inserts a number into a sorted singly-linked list.
* @head: A pointer the head of the linked list.
* @number: The number to insert.
*
* Return: If the function fails - NULL.
* Otherwise - a pointer to the new node.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (old == NULL || old->n >= number)
	{
		new->next = old;
		*head = new;
		return (new);
	}
	
	while (old && old->next && old->next->n < number)
		old = old->next;
	new->next = old->next;
	old->next = new;

	return (new);
}
