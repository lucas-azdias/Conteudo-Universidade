#include <stdio.h>

int main()
{
    printf("Forma geral da equação do segundo grau: a x**2 + b x + c = 0\n");
    double coef_a = obter_coeficiente("Digite o coeficiente a: ");
    if (coef_a == 0)
    {
        printf("O coeficiente a não pode ser zero!\n");
        return 0;
    }
    double coef_b = obter_coeficiente("Digite o coeficiente b: ");
    double coef_c = obter_coeficiente("Digite o coeficiente c: ");
    double delta = calcular_delta(coef_a, coef_b, coef_c);
    if (delta < 0)
        responder_sem_raiz();
    else if (delta == 0)
        responder_uma_raiz(coef_a, coef_b);
    else
        responder_duas_raizes(coef_a, coef_b, delta);

    return 0;
}