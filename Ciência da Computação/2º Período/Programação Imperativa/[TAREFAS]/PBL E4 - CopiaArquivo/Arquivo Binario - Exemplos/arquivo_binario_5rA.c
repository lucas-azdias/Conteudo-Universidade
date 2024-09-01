#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 2

typedef struct {
    char titulo[50];
    char autor[40];
    int numero_paginas;
    int ano_publicacao;
} Livro;

int main()
{
    Livro buffer[BUFFER_SIZE];

    FILE* arq = fopen("teste.bin", "rb");
    size_t lido = 0;
    size_t total = 0;
    do
    {
        lido = fread(buffer, sizeof(Livro), BUFFER_SIZE, arq);
        printf("lido = %zu\n", lido);
        total = total + lido;
    }
    while (lido == BUFFER_SIZE);
    
    fclose(arq);
    printf("total = %zu\n", total);

    return 0;
}