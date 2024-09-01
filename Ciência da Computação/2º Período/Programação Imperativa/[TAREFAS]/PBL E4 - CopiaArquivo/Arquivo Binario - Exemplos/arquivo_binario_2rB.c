#include <stdio.h>

int main()
{
    char ch;

    FILE* arq = fopen("teste.bin", "rb");
    int lido = 0;
    int total = 0;
    do
    {
        lido = fread(&ch, 1, 1, arq);
        printf("lido = %d\n", lido);
        total = total + lido;
    }
    while (lido > 0);
    fclose(arq);
    printf("total = %d\n", total);

    return 0;
}