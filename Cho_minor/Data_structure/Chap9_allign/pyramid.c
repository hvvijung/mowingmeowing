#include <stdio.h>

void main()
{
    int i, j;
    
    for(j = 5 ; j >= 1 ; j --)
    {
        for(i = 0 ; i < j ; i ++)
        printf("*");
    printf("\n");
    }
}