#include <stdio.h>
#include "sandpiles.h"

/**
 * sandpiles_sum - Computes the sum of two sandpiles
 * @grid1: Left 3x3 grid
 * @grid2: Right 3x3 grid
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3]) {
    sum_grids(grid1, grid2);
    while (!check_grids(grid1)) {
        print_grid(grid1);
        change_grids(grid1);
    }
}

/**
 * sum_grids - Computes the sum of two grids
 * @grid1: Left 3x3 grid
 * @grid2: Right 3x3 grid
 */
void sum_grids(int grid1[3][3], int grid2[3][3]) {
    int i, j;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            grid1[i][j] += grid2[i][j];
        }
    }
}

/**
 * check_grids - Checks if a grid is stable
 * @grid: 3x3 grid
 * Return: 1 if stable, 0 otherwise
 */
int check_grids(int grid[3][3]) {
    int i, j;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            if (grid[i][j] > 3) {
                return 0;
            }
        }
    }
    return 1;
}

/**
 * print_grid - Prints a 3x3 grid
 * @grid: 3x3 grid
 */
void print_grid(int grid[3][3]) {
    int i, j;
    printf("=\n");
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            if (j) printf(" ");
            printf("%d", grid[i][j]);
        }
        printf("\n");
    }
}

/**
 * change_grids - Performs a toppling operation on a grid
 * @grid: 3x3 grid
 */
void change_grids(int grid[3][3]) {
    int i, j;
    int new_grid[3][3] = {0};

    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            if (grid[i][j] > 3) {
                grid[i][j] -= 4;
                if (i > 0) new_grid[i-1][j] += 1;
                if (i < 2) new_grid[i+1][j] += 1;
                if (j > 0) new_grid[i][j-1] += 1;
                if (j < 2) new_grid[i][j+1] += 1;
            }
        }
    }

    sum_grids(grid, new_grid);
}
