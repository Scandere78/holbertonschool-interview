#include "slide_line.h"

/**
 * merge_left - Fusionne et décale les éléments vers la gauche
 */
void merge_left(int *line, size_t size)
{
    size_t i, j;
    int last_merge_index = -1;

    for (i = 0, j = 0; i < size; i++)
    {
        if (line[i] == 0)
            continue;

        if (j > 0 && line[j - 1] == line[i] && last_merge_index != (int)(j - 1))
        {
            line[j - 1] *= 2;
            last_merge_index = j - 1;
        }
        else
        {
            line[j++] = line[i];
        }
    }

    while (j < size)
        line[j++] = 0;
}

/**
 * merge_right - Fusionne et décale les éléments vers la droite
 */
void merge_right(int *line, size_t size)
{
    int i, j;
    int last_merge_index = -1;

    for (i = (int)size - 1, j = (int)size - 1; i >= 0; i--)
    {
        if (line[i] == 0)
            continue;

        if (j < (int)size - 1 && line[j + 1] == line[i] && last_merge_index != j + 1)
        {
            line[j + 1] *= 2;
            last_merge_index = j + 1;
        }
        else
        {
            line[j--] = line[i];
        }
    }

    while (j >= 0)
        line[j--] = 0;
}

/**
 * slide_line - Applique le mouvement et la fusion selon la direction
 * Return: 1 en cas de succès, 0 sinon
 */
int slide_line(int *line, size_t size, int direction)
{
    if (!line || size == 0 || (direction != SLIDE_LEFT && direction != SLIDE_RIGHT))
        return (0);

    if (direction == SLIDE_LEFT)
        merge_left(line, size);
    else
        merge_right(line, size);

    return (1);
}

