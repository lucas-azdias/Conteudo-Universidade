#include <stdio.h>

int main()
{
    char ch;

    FILE* arq = fopen("teste.bin", "rb");
    fread(&ch, 1, 1, arq);
    fclose(arq);

    printf("ch = %c\n", ch);

    return 0;
}
