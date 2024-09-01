#include <stdio.h>
#include <string.h>

int main()
{
  int qc = 0, qv = 0;
  char letra;
  int numero;
  char enter;
  while (1){
  puts("entre com a letra:");
  scanf("%c", &letra);
  scanf("%c", &enter);
    if (isalpha(letra)){
      if(letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u'){
        printf("Digitou Vogal\n");
        qv++;
      }
       else {
        printf("Digitou Consoante\n");
         qc++;
         }
      }
    else if(letra == '0') {
      break;
        }
    else{
      printf("erro");
      }
    }
    printf("vogais= %d \n", qv);
    printf("consoante= %d \n",qc);
    return 0;
  }