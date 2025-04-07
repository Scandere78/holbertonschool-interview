#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insère un nombre dans une liste triée
 * @head: pointeur vers le début de la liste
 * @number: valeur à insérer
 *
 * Return: adresse du nouveau nœud, ou NULL en cas d'échec
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || number < (*head)->n) /* insertion en tête */
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    current = *head;
    while (current->next && current->next->n < number)
        current = current->next;

    new_node->next = current->next;
    current->next = new_node;

    return (new_node);
}
