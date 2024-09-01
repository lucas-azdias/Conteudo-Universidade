#include <stdio.h>

int main()
{
    char ch = 'Z';

    FILE* arq = fopen("teste.bin", "wb");
    fwrite(&ch, 1, 1, arq);
    fclose(arq);

    return 0;
}
