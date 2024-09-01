#include <stdio.h>

#define QUANTIDADE 10

int main()
{
    int numeros[QUANTIDADE];
    for (int i = 0; i < QUANTIDADE; i++) numeros[i] = i * 2;

    const int ESPACO_UNITARIO = sizeof(int);
    FILE* arq = fopen("teste.bin", "wb");
    fwrite(numeros, ESPACO_UNITARIO, QUANTIDADE, arq);
    fclose(arq);

    return 0;
}