#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utils.h"
#define MAX_LINES 100

int main(void){
    int lines[MAX_LINES];
    int n, m, i;
    scanf("%d%d", &n, &m);
    for (i = 0; i < n; i++)
        scanf("%d", &lines[i]);
    solve(lines, n , m);
    return 0;
}
