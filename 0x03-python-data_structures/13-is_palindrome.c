#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
*reverse_listint - function that reverses a linked list
*@head:is a pointer the singly linked list
* Return:a pointer to the first node of the reversed list
*/
listint_t *reverse_listint(listint_t **head)
{
	listint_t *p_prev =  (*head)->next;
	listint_t *p_next =  p_prev->next;

	(*head)->next = NULL;
	while (p_prev != NULL)
	{
		p_prev->next = *head;
		*head = p_prev;
		p_prev = p_next;
		if (p_prev == NULL)
			return (*head);
		p_next = p_next->next;
	}
	return (*head);
}

/**
 * is_palindrome- checks if a singly linked list is a palindrome.
 * @head: pointer to head of list
 * Return: 1 if is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *p_aux = *head;
	int cont = 0, i = 0, *array;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (p_aux)
	{
		cont++;
		p_aux = p_aux->next;
	}
	array = malloc(cont * sizeof(int));
	p_aux = *head;
	while (p_aux)
	{
		array[i] = p_aux->n;
		p_aux = p_aux->next;
		i++;
	}
	reverse_listint(head);
	p_aux = *head;
	i = 0;
	while (p_aux)
	{
		if (p_aux->n != array[i])
		{
			free(array);
			return (0);
		}
		p_aux = p_aux->next;
		i++;
	}
	free(array);
	return (1);
}
