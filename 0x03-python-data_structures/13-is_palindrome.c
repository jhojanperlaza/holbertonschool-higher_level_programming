#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * palindrome- checks if a singly linked list is a palindrome.
 * @head: pointer to head of list
 * @string_left: pointer to tail of list
 * Return: 1 if is palindrome, 0 otherwise
 */
int palindrome(listint_t **string_left, listint_t **head)
{
	listint_t *move = NULL;
	listint_t *string_right = NULL;

	if (!head)
		return (1);
	if (!*head)
		return (0);

	string_right = *head;

	if (!string_left)
		move = string_right, string_left = &move;

	if (palindrome(string_left, &(string_right->next)) == 0
		&& string_right->next != NULL)
		return (0);

	if ((*string_left)->n != string_right->n)
		return (0);

	if ((*string_left)->n == string_right->n)
		*string_left = (*string_left)->next;

	return (1);
}
