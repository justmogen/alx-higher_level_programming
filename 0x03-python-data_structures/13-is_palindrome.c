#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to first node of a singly-linked list
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int n = 0;
	size_t arr[15];

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		arr[n] =current->n;
		current = current->next;
		n++;
	}
	current = *head;
	n--;
	while (current != NULL)
	{
		if (current->n != arr[n])
			return (0);
		n--;
		current = current->next;
	}
	return (1);
}
