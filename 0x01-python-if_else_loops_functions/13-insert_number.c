#include "lists.h"
/**
 * insert_node - function to Inserts a numb into a sorted singly linked list.
 *
 * @head: the pointer to the head of the linked list.
 *
 * @number: The numb  to insert.
 *
 * Return: 0 If it  fails or pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;
	return (new);
}

