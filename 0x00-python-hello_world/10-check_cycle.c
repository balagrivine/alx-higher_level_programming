#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list;
	while (list  && slow != fast)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast == slow)
	{
		return (1);
	}
	else
		return (0);

	return (0);
}
