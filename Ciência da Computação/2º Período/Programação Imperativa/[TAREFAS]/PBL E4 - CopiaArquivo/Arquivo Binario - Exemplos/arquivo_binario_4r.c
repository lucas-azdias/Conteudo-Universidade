#include <stdio.h>
#include <string.h>

typedef struct {
    char titulo[50];
    char autor[40];
    int numero_paginas;
    int ano_publicacao;
} Livro;

int main()
{
    Livro L;

    FILE* arq = fopen("teste.bin", "rb");
    fread(&L, sizeof(Livro), 1, arq);
    fclose(arq);

    printf("%s\n", L.titulo);
    printf("%s\n", L.autor);
    printf("%d\n", L.numero_paginas);
    printf("%d\n", L.ano_publicacao);
    
    return 0;
}