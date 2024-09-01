#include <stdio.h>

#define MAX 10

int main()
{
    char palavra[MAX];

    FILE* arq = fopen("teste.bin", "rb");
    for (int i = 0; i < MAX; i++)
    {
        int lido = fread(&palavra[i], 1, 1, arq);
        printf("lido = %d\n", lido);
    }
    
    fclose(arq);

    for (int i = 0; i < MAX; i++)
    printf("%c", palavra[i]);
    putchar('\n');

    return 0;
}