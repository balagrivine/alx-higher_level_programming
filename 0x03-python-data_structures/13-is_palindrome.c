#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int *arr, j, i, count;

	temp = *head;
	count = 0;
	while (temp != NULL)
	{
		count++;
		temp = temp->next;
	}
	arr = (int*)malloc(sizeof(int) * count);
	if (arr == NULL)
	{
		free(arr);
	}
	temp = *head;
	for (i = 0; i < count; i++)
	{
		arr[i] = temp->n;
		temp = temp->next;
	}
	for (i = 0, j = count - 1; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return 0;
		}
	}
	free(arr);
	return 1;
}
