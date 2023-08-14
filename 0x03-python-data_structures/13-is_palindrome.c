#include "lists.h"

/**
* revlist - Reverses a singly-linked listint_t list.
* @head: A pointer to the starting node of the list to reverse.
*
* Return: A pointer to the head of the reversed list.
*/

listint_t *revlist(listint_t **head)
{
	listint_t *crnt = *head, *next, *prev = NULL;

	while (crnt)
	{
		next = crnt->next;
		crnt->next = prev;
		prev = crnt;
		crnt = next;
	}
	*head = prev;
	return (*head);
}

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: A pointer to the head of the linked list.
*
* Return: If the linked list is not a palindrome - 0.
* If the linked list is a palindrome - 1.
*/

int is_palindrome(listint_t **head)
{
	size_t size = 0, i = 0;
	listint_t *tmp, *rev, *mid;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp = *head;
	while(tmp)
	{
		size++;
		tmp = tmp->next;
	}
	tmp = *head;
	for (; i < (size/2) - 1; i++)
		tmp = tmp->next;
	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);
	
	tmp = tmp->next->next;
	rev = revlist(&tmp);
	mid = rev;
	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	revlist(&mid);
	return (1);
}
