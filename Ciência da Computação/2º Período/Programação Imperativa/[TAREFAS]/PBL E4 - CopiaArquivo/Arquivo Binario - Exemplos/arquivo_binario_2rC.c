#include <stdio.h>

#define BUFFER_SIZE 3

int main()
{
    char buffer[BUFFER_SIZE];

    FILE* arq = fopen("teste.bin", "rb");
    int lido = 0;
    int total = 0;
    do
    {
        lido = fread(buffer, 1, BUFFER_SIZE, arq);
        printf("lido = %d\n", lido);
        total = total + lido;
    }
    while (lido == BUFFER_SIZE);
    fclose(arq);
    printf("total = %d\n", total);

    return 0;
}