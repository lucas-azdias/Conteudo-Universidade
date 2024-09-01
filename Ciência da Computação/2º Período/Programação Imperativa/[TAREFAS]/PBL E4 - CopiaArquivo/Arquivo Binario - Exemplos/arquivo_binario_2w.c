#include <stdio.h>

#define MAX 10

int main()
{
    char palavra[MAX];
    for (int i = 0; i < MAX; i++)
        palavra[i] = i + 'a';

    FILE* arq = fopen("teste.bin", "wb");
    fwrite(palavra, 1, MAX, arq);
    fclose(arq);

    return 0;
}