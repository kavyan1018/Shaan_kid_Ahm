#include<stdio.h>
#include<conio.h>
void main()
{
    int i, j;
    char n;

    printf("Enter the Pattern type which u want to Display : ");
    scanf("%c",&n);
    for (i = 1; i < 5; i++)    // row 
    {
        for (j = 0; j < 5; j++)   // cols
        {
            printf("%c", n);
        }
        printf("\n");
    }
}