#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 100
#define LENGTH 5

int main()
{
    time_t t;
    /* Inicializa o gerador de números aleatórios */
    srand((unsigned) time(&t));

    FILE* arq = fopen("teste.bin", "w");

    for (int i = 0; i < MAX; i++)
    {
        fwrite(&i, sizeof(int), 1, arq);
        for (int j = 0; j < LENGTH; j++)
        {
            int k = rand() % 26;
            char ch = 'a' + k;
            fwrite(&ch, sizeof(char), 1, arq);
        }
    }

    fclose(arq);

    return 0;
}