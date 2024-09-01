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

    strcpy(biblioteca[0].titulo, "Ensaio sobre a cegueira");
    strcpy(biblioteca[0].autor, "José Saramago");
    biblioteca[0].numero_paginas = 310;
    biblioteca[0].ano_publicacao = 1995;

    strcpy(biblioteca[1].titulo, "Cem sonetos de amor");
    strcpy(biblioteca[1].autor, "Pablo Neruda");
    biblioteca[1].numero_paginas = 128;
    biblioteca[1].ano_publicacao = 1959;

    strcpy(biblioteca[2].titulo, "Sentimento do mundo");
    strcpy(biblioteca[2].autor, "Carlos Drummond de Andrade");
    biblioteca[2].numero_paginas = 101;
    biblioteca[2].ano_publicacao = 1940;

    FILE* arq = fopen("teste.bin", "wb");
    fwrite(&biblioteca, sizeof(Livro), QUANTIDADE, arq);
    fclose(arq);

    return 0;
}