#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a panlindrome
 * @head: a pointer to a pointer to the head of the list
 * Return: 0 if not a panlindrome else 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *tmp1 = *head;
	int count = 0, i = 0, j = 0, check = 0, n = 0, *list = NULL;

	while (tmp != NULL)
	{
		tmp = tmp->next;
		count++;
	}
	n = count - 1;
	list = malloc(count * sizeof(int));
	while (tmp1 != NULL && i < count)
	{
		list[i] = tmp1->n;
		i++;
		tmp1 = tmp1->next;
	}
	while (j < count && n > 0)
	{
		if (list[j] == list[n])
			check = 1;
		else
		{
			check = 0;
			break;
		}
		j++;
		n--;
	}
	free(list);
	return (check);
}
