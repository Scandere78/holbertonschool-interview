#include "binary_trees.h"
#include <stdlib.h>

/**
 * binary_tree_size - Compte les nœuds dans un arbre binaire
 */
size_t binary_tree_size(const binary_tree_t *tree)
{
	if (!tree)
		return (0);
	return (1 + binary_tree_size(tree->left) + binary_tree_size(tree->right));
}

/**
 * get_parent_node - Trouve le parent où insérer le nouveau nœud
 */
heap_t *get_parent_node(heap_t *root, size_t index)
{
	if (index == 1)
		return (NULL);
	heap_t *parent = root;
	size_t path[64], depth = 0;

	/* Décoder le chemin vers le parent en binaire sauf le bit le plus haut */
	while (index > 1)
	{
		path[depth++] = index % 2;
		index /= 2;
	}
	for (int i = depth - 1; i > 0; i--)
		parent = path[i] ? parent->right : parent->left;

	return (parent);
}

/**
 * swap_up - Remonte le nœud si la valeur est plus grande que le parent
 */
void swap_up(heap_t *node)
{
	int tmp;
	while (node->parent && node->n > node->parent->n)
	{
		tmp = node->n;
		node->n = node->parent->n;
		node->parent->n = tmp;
		node = node->parent;
	}
}

/**
 * heap_insert - Insère une valeur dans le Max Binary Heap
 */
heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *new_node, *parent;
	size_t size;

	if (!root)
		return (NULL);

	new_node = binary_tree_node(NULL, value);
	if (!new_node)
		return (NULL);

	if (!*root)
	{
		*root = new_node;
		return (new_node);
	}

	size = binary_tree_size(*root) + 1;
	parent = get_parent_node(*root, size);

	new_node->parent = parent;
	if (!parent->left)
		parent->left = new_node;
	else
		parent->right = new_node;

	swap_up(new_node);

	return (new_node);
}
