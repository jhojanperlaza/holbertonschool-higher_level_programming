#include "lists.h"
/**
 * check_cycle - prints all elements of a listint_t list
 * @list: is the list
 * Return: number of nodes
 */

int check_cycle(listint_t *list)
{
	listint_t *p_aux = list;
	listint_t *p_aux2 = list;

	while (p_aux2 != NULL)
	{
		p_aux2 = p_aux2->next->next;
		if (p_aux == p_aux2)
			return (1);
		p_aux = p_aux->next;
	}
	return (0);
}
