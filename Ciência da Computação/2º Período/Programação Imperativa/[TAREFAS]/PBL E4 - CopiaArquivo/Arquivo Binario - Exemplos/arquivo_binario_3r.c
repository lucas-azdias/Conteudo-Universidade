#include <stdio.h>

#define QUANTIDADE 10

int main()
{
    int numeros[QUANTIDADE];

    const int ESPACO_UNITARIO = sizeof(int);
    FILE* arq = fopen("teste.bin", "rb");
    fread(numeros, ESPACO_UNITARIO, QUANTIDADE, arq);
    fclose(arq);

    for (int i = 0; i < QUANTIDADE; i++) printf("%d\n", numeros[i]);

    return 0;
}