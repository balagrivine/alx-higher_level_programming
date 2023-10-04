#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp, *prev;

	new_node = (listint_t*)malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		free(new_node);
		return NULL;
	}
	new_node->n = number;
	new_node->next = NULL;
	if ((*head) == NULL)
	{
		(*head) = new_node;
		return (0);
	}
	temp = *head;
	while (temp != NULL && temp->n < new_node->n)
	{
		prev = temp;
		temp = temp->next;
	}
	if (prev == NULL)
	{
		new_node->next = (*head);
		(*head) = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = temp->next;
	}
	/*(*new_node)->next = (*temp)->next;*/
	/*(*temp)->next = (*new_node);*/

	return (new_node);
}
