#include <stdio.h>

int main()
{
    int k = 999;

    FILE* arq = fopen("teste.bin", "wb");
    fwrite(&k, 4, 1, arq);
    fclose(arq);

    return 0;
}