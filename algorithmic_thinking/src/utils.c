#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utils.h"

int shortest_line_index(int lines[], int n){
    int j;
    int shortest = 0;
    for (j = 1; j < n; j++)
        if (lines[j] < lines[shortest])
            shortest = j;
    return shortest;
}

void solve(int lines[], int n, int m){
    int i, shortest;
    for (i = 0; i < m; i++){
        shortest = shortest_line_index(lines, n);
        printf("%d\n", lines[shortest]);
        lines[shortest]++;
    }
}
