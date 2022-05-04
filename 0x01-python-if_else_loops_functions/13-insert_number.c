#include "lists.h"
/**
 * insert_node - inser node in the order of number
 * @head: pointer to head of list
 * @number: is the value to insert
 * Return: new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p_aux = *head;
	listint_t *new_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (!head || !*head)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (p_aux)
	{
		if (number > p_aux->n && number < p_aux->next->n)
		{
			new_node->next = p_aux->next;
			p_aux->next = new_node;
		}
		else if (number < p_aux->n)
		{
			p_aux = p_aux->next;
			new_node->next = *head;
			*head = new_node;
			return (p_aux);
		}
		p_aux = p_aux->next;
	}
	return (p_aux);
}
