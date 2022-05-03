#include "lists.h"
/**
 * check_cycle - prints all elements of a listint_t list
 * @list: is the list
 * Return: 0 is list has a cycle or 1 is no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *p_aux = list;
	listint_t *p_aux2 = list;

	while (p_aux2 && p_aux && p_aux2->next)
	{
		/*if p_aux2->next is null no shouldenter loop */
		p_aux2 = p_aux2->next->next;
		p_aux = p_aux->next;
		if (p_aux == p_aux2)
			return (1);
	}
	return (0);
}
