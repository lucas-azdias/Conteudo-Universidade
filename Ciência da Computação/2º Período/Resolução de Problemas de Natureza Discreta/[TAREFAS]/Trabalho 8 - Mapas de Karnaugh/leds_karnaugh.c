#include <stdio.h>
#include <stdlib.h>

const char HORIZONTAL_LINE = '='/*┅*//*L'\U00002505'*/; // Linha horizontal no dígito
const char VERTICAL_LINE = '|'/*┊*//*L'\U0000250A'*/; // Linha vertical no dígito

typedef enum { // Enum com os LEDs do dígito
      LED_A,
      LED_B,
      LED_C,
      LED_D,
      LED_E,
      LED_F,
      LED_G
} LED;
/*
      Dígito:
        a
      f   b
        g
      e   c
        d
*/

char* int_to_bits(int, size_t);
unsigned int select_bit_in_bits(int, char*);
int solveLed(unsigned int, unsigned int, unsigned int, unsigned int, LED);

int main() {

      size_t SIZE = 4;

      // Mostra uma tabela-verdade com os leds que devem ser ligados para mostrar o valor hexadecimal correspondente
      puts("\nNUM\tA\tB\tC\tD\tE\tF\tG");
      for (int i = 0; i < SIZE * SIZE; i++) {
            char* bits = int_to_bits(i, 4); // String de bits do número atual
            unsigned int a = select_bit_in_bits(0, bits); // Primeiro bit da string
            unsigned int b = select_bit_in_bits(1, bits); // Segundo bit da string
            unsigned int c = select_bit_in_bits(2, bits); // Terceiro bit da string
            unsigned int d = select_bit_in_bits(3, bits); // Quarto bit da string
            printf(
                  "%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n",
                  bits,
                  solveLed(a, b, c, d, LED_A),
                  solveLed(a, b, c, d, LED_B),
                  solveLed(a, b, c, d, LED_C),
                  solveLed(a, b, c, d, LED_D),
                  solveLed(a, b, c, d, LED_E),
                  solveLed(a, b, c, d, LED_F),
                  solveLed(a, b, c, d, LED_G)
            );
      }

      // Mostra cada dígito formado a partir da tabela-verdade anterior
      puts("\n\nDígitos:\033[1m");
      for (int i = 0; i < SIZE * SIZE; i++) {
            char* bits = int_to_bits(i, 4); // String de bits do número atual
            unsigned int a = select_bit_in_bits(0, bits); // Primeiro bit da string
            unsigned int b = select_bit_in_bits(1, bits); // Segundo bit da string
            unsigned int c = select_bit_in_bits(2, bits); // Terceiro bit da string
            unsigned int d = select_bit_in_bits(3, bits); // Quarto bit da string
            
            printf(
                  "\n  %c\n%c   %c\n  %c\n%c   %c\n  %c\n",
                  solveLed(a, b, c, d, LED_A) ? HORIZONTAL_LINE : ' ',
                  solveLed(a, b, c, d, LED_F) ? VERTICAL_LINE : ' ',
                  solveLed(a, b, c, d, LED_B) ? VERTICAL_LINE : ' ',
                  solveLed(a, b, c, d, LED_G) ? HORIZONTAL_LINE : ' ',
                  solveLed(a, b, c, d, LED_E) ? VERTICAL_LINE : ' ',
                  solveLed(a, b, c, d, LED_C) ? VERTICAL_LINE : ' ',
                  solveLed(a, b, c, d, LED_D) ? HORIZONTAL_LINE : ' '
                  /*
                        Dígito:
                          a
                        f   b
                          g
                        e   c
                          d
                  */
            );
      }
      puts("\033[m");

      return 0;
}

char* int_to_bits(int num, size_t size_bits) {
      // Transforma o número passado em uma string de bits (com o tamanho selecionado)
      char* bits = malloc(sizeof(char) * size_bits + 1);

      for (int i = 0; i < (int) size_bits; i++) {
            *(bits + i) = num & (1u << (size_bits - 1 - i)) ? '1' : '0';
      }
      *(bits + sizeof(char) * size_bits) = '\0';

      return bits;
}

unsigned int select_bit_in_bits(int index, char* bits) {
      // Seleciona um bit dentro da string de bits  e o retorna como um unsigned int
      unsigned int b;

      if (*(bits + index) == '0') {
            b = 0u;
      } else if (*(bits + index) == '1') {
            b = 1u;
      } else {
            b = NULL;
      }

      return b;
}

int solveLed(unsigned int a, unsigned int b, unsigned int c, unsigned int d, LED led) {
      // Resolve para um LED de acordo com os bits se ele deve ficar ligado ou não
      switch (led) {
            case LED_A:
                  return (
                        (!a && (
                              (!b && !d) ||
                              (c) ||
                              (b && d)
                        )) ||
                        (b && c) ||
                        (a && !d) ||
                        (a && !b && !c)
                  );
            
            case LED_B:
                  return (
                        (a && !c && d) ||
                        (!a && (
                              (!c && !d) ||
                              (c && d)
                        )) ||
                        (!b && (
                              (!a && c) ||
                              (a && !d)
                        )) ||
                        (!b && !c)
                  );
            
            case LED_C:
                  return (
                        (!a && (
                              (!c) ||
                              (d) ||
                              (b && c)
                        )) ||
                        (!b && (
                              (!c) ||
                              (a && c)
                        )) ||
                        (b && !c && d)
                  );
            
            case LED_D:
                  return (
                        (a && !c) ||
                        (!d && (
                              (!a && !b) ||
                              (b && c)
                        )) ||
                        (d && (
                              (b && !c) ||
                              (!b && c)
                        ))
                  );
            
            case LED_E:
                  return (
                        (a && (
                              (c) ||
                              (b && !c)
                        )) ||
                        (!d && (
                              (!a && c) ||
                              (!b && !c)
                        ))
                  );
            
            case LED_F:
                  return (
                        (a && (
                              (c) ||
                              (!b && !c)
                        )) ||
                        (!c && !d && (
                              (!a) ||
                              (b)
                        )) ||
                        (!a && b && (
                              (!c) ||
                              (!d)
                        ))
                  );
            
            case LED_G:
                  return (
                        (a && (
                              (c) ||
                              (d) ||
                              (!b && !c)
                        )) ||
                        (!a && (
                              (!b && c) ||
                              (b && !d)
                        )) ||
                        (b && !c && (
                              (!a) ||
                              (d)
                        ))
                  );
            
            default:
                  return NULL;
      }
}
