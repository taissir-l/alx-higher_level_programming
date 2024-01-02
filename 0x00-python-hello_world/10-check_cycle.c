#include "lists.h"
/**
 * check_cycle - function to check for loop in LL
 *
 * @list: head of LL.
 *
 * Description - the loops checker in LL
 *
 * Return: 1 when cycled or 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
	{
		return (0);
	}
	slow = list;
	fast = list->next;

	while (fast && slow && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
