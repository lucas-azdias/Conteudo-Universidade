#include <stdio.h>

#define MAX 10

int main()
{
    char palavra[MAX];

    FILE* arq = fopen("teste.bin", "rb");
    fread(palavra, 1, MAX, arq);
    fclose(arq);

    for (int i = 0; i < MAX; i++)
    printf("%c", palavra[i]);
    putchar('\n');

    return 0;
}