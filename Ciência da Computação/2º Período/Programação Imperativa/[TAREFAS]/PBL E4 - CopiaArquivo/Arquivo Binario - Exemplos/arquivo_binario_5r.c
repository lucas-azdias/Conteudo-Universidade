#include <stdio.h>
#include <string.h>

#define QUANTIDADE 3

typedef struct {
    char titulo[50];
    char autor[40];
    int numero_paginas;
    int ano_publicacao;
} Livro;

int main()
{
    Livro biblioteca[QUANTIDADE];

    FILE* arq = fopen("teste.bin", "rb");
    fread(biblioteca, sizeof(Livro), QUANTIDADE, arq);
    fclose(arq);

    for (int i = 0; i < QUANTIDADE; i++)
    {
        printf("%s\n", biblioteca[i].titulo);
        printf("%s\n", biblioteca[i].autor);
        printf("%d\n", biblioteca[i].numero_paginas);
        printf("%d\n", biblioteca[i].ano_publicacao);
        putchar('\n');
    }
    
    return 0;
}