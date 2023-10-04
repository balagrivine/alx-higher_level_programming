#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp;

	new_node = (listint_t*)malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		free(new_node);
		return NULL;
	}
	new_node->n = number;
	if ((*head) == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = (*head);
		(*head) = new_node;
		return (new_node);
	}
	temp = *head;
	while (temp->next != NULL && temp->next->n < new_node->n)
	{
		temp = temp->next;
	}
	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}
