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
    strcpy(L.titulo, "Ensaio sobre a cegueira");
    strcpy(L.autor, "José Saramago");
    L.numero_paginas = 310;
    L.ano_publicacao = 1995;

    FILE* arq = fopen("teste.bin", "wb");
    fwrite(&L, sizeof(Livro), 1, arq);
    fclose(arq);

    return 0;
}