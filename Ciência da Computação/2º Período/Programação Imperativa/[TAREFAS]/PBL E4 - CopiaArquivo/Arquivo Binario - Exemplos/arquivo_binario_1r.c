#include <stdio.h>

int main()
{
    int k;

    FILE* arq = fopen("teste.bin", "rb");
    fread(&k, 4, 1, arq);
    fclose(arq);

    printf("k = %d\n", k);

    return 0;
}