package com.poo;

import java.util.Scanner;

public class modulo2 {

    /* 
        Exemplo: Execute o programa três vezes, 
        fornecendo como entrada os valores 200.00, 50.00 e 100.00. 
        Note que a mensagem "Obrigado" é sempre impressa.         
     */
    public static void main(String args[]) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o preço do produto: ");
        double preco = teclado.nextDouble();

        if (preco <= 100.00) {
            System.out.println("Preço bom!");
        } else {
            System.out.println("Muito caro!");
        }
        System.out.println("Obrigado");
    }

    /*
    Comando Composto (Bloco de Comandos)
    Execute o programa três vezes, 
    fornecendo como entrada os valores 200.00, 50.00 e 100.00.  
     */
    public static void main2(String args[]) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o preço do produto: ");
        double preco = teclado.nextDouble();
        if (preco <= 100.00) {
            System.out.println("Preço bom!");
            System.out.println("Compre uma unidade");
        } else {
            System.out.println("Muito caro!");
        }
        System.out.println("Obrigado");
    }

    /*
    Encadeamento de desviosExecute o programa para as 
    seguintes entradas: 80.00, 50.00, 30.00, 100.00 e 150.00. 
     */
    public static void main3(String args[]) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o preço do produto: ");
        double preco = teclado.nextDouble();

        if (preco <= 100.00) {
            System.out.println("Preço bom!");
            if (preco > 50.00) {
                System.out.println("Compre uma unidade.");
            } else {
                System.out.println("Compre duas unidades");
            }
        } else {
            System.out.println("Muito caro!");
        }
        System.out.println("Obrigado");
    }

    /*
    Comando-2 opcional: Teste o exemplo, 
    fornecendo como entrada o valor 200.00. 
    Observe que somente a mensagem "Obrigado" é impressa.
     */
    public static void main4(String args[]) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o preço do produto: ");
        double preco = teclado.nextDouble();

        if (preco <= 100.00) {
            System.out.println("Preço bom!");

            if (preco > 50.00) {
                System.out.println("Compre uma unidade.");
            } else {
                System.out.println("Compre duas unidades");
            }
        }
        System.out.println("Obrigado");
    }

    /*
    Comando de desvio: switch
    Verifica o valor fornecido para k e, dependendo do 
    valor (0, 1, 2 ou outro qualquer, isto é, default), 
    executa um bloco específico de comandos (cada bloco é encerrado 
    com o comando break). Execute o programa com os seguintes dados 
    de entrada: 0, 1, 2 e 4.
     */
    public static void main5(String args[]) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o valor de k: ");

        int k = teclado.nextInt();

        switch (k) {
            case 0:
                k = (k + 5) * 3;
                break;
            case 1:
                k = k + 5;
                k = k * k;
                break;
            case 2:
                k = k * 3;
                k = k / 2;
                break;
            default:
                k = 0;
        }
        System.out.println(k);
    }

    /*
    Comando de Repetição: while 
    No comando while, o comando-repetível será repetidamente 
    executado enquanto a expressão-lógica for verdadeira. 
 
    Teste o programa fornecendo os seguintes valores 
    para n: 5, 20, 1 e 0.    
     */
    public static void main6(String args[]) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o seu nome: ");
        String nome = teclado.next();

        System.out.print("Digite o número de vezes : ");
        int n = teclado.nextInt();

        int i = 0;
        while (i < n) {
            i = i + 1;
            System.out.println("Vez " + i + ": " + nome);
        }
        System.out.println("Fim do programa");
    }

    /*
    Exemplo: while 
    Teste o programa para os seguintes valores de n: 8, 9, 10 e 11. 
     */
    public static void main7(String args[]) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o valor máximo para k : ");
        int n = teclado.nextInt();

        int k = 2;

        while (k < n - 2) {
            k = k + 3;
        }
        System.out.println("Valor final de k: " + k);
    }

    /*
    Comando de Repetição: for 
    
    for ( expr-inicial; expr-lógica; expr-final )
           comando-repetível
    
    A expressão expr-inicial é executada somente uma vez 
    (quando começa a execução do comando for). 
    A expressão expr-condicional é usada para determinar 
    o fim da repetição, semelhantemente ao que ocorre 
    no comando while: o comando-repetível (simples ou composto) 
    é repetidamente executado enquanto expr-lógica for verdadeira. 
    A expressão expr-final é executada repetidamente, logo após 
    cada execução do comando-repetível. 
 
    Teste o programa para os seguintes valores de n: 8, 9, 10 e 11.
    Observe o valor de i impresso em cada vez e compare com a saída obtida no
    exemplo acima que faz o mesmo processando usando o comando while. 
     */
    public static void main8(String args[]) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o seu nome: ");
        String nome = teclado.next();

        System.out.print("Digite o número de vezes : ");
        int n = teclado.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.println("Vez " + i + ": " + nome);
        }
        System.out.println("Fim do programa");
    }

    /*
    Vetores e Matrizes  
    Uma sequência finita de dados de certo tipo pode ser representada 
    por uma única variável indexada, denominada vetor (ou array). 
    Por exemplo, a sequência de números primos { 1, 2, 3, 5, 7, 11, 13 } 
    pode ser armazenada em um vetor denominado primo com capacidade para 
    armazenar 7 valores do tipo int, ou seja, o comprimento (ou tamanho) 
    do vetor seria 7. Em Java, esse vetor pode declarado e iniciado da 
    seguinte forma:
    
    int[ ] primo = {1, 2, 3, 5, 7, 11, 13};
    
    O tipo da variável primo é int[ ], o que significa que a variável 
    é um vetor de valores do tipo int. A sequência { 1, 2, 3, 5, 7, 11, 13 } 
    atribuída à variável primo não apenas define o seu valor inicial, 
    mas também fixa o seu comprimento, nesse caso 7, uma vez que a sequência 
    possui 7 elementos.
     */
 /*
    Acesso aos elementos de um vetor 
    Cada um dos elementos da sequência pode ser acessado através do 
    correspondente índice, sendo o primeiro elemento indexado por 0 
    (zero) e o último pelo comprimento da sequência menos 1. 
 
    Execute o programa e confira os valores impressos. 
     */
    public static void main9(String args[]) {

        int[] primo = {1, 2, 3, 5, 7, 11, 13};

        System.out.println(primo[0]);
        System.out.println(primo[3]);
        System.out.println(primo[6]);
    }

    /*
    Impressão de um vetor 
    A impressão completa dos elementos de uma sequência pode ser feita 
    por meio de um comando de repetição: o comando repetível seria o 
    comando de impressão do i-ésimo elemento, variando-se i de 0 até o 
    tamanho da sequência menos 1. 
     */
    public static void main10(String args[]) {

        int[] primo = {1, 2, 3, 5, 7, 11, 13};

        for (int i = 0; i < primo.length; i++) {
            System.out.println(primo[i]);
        }
    }

    /*
    Modificação de um elemento de um vetor 
    Qualquer elemento de um vetor pode ter o valor modificado por meio de 
    um comando de atribuição. 
     */
    public static void main11(String args[]) {
        int[] primo = {1, 2, 3, 5, 7, 11, 13};

        primo[3] = 10; // modifica o quarto elemento do vetor

        for (int i = 0; i < primo.length; i++) {
            System.out.println(primo[i]);
        }
    }

    /*
    Expressão com elementos de um vetor 
    
    Os elementos de uma sequência podem ser indexados e, assim, 
    usados em qualquer expressão compatível com o tipo dos dados 
    na sequência. 
     */
    public static void main12(String args[]) {
        int[] primo = {1, 2, 3, 5, 7, 11, 13};
        int soma = 0;

        for (int i = 0; i < primo.length; i++) {
            if (primo[i] > 5) {
                soma = soma + primo[i];
            }
        }
        System.out.println(soma);
    }

    /*
    Criação de um vetor 
    
    Um vetor também pode ser iniciado por meio do comando new, 
    deixando os seus elementos com o valor padrão do sistema, 
    de acordo com o tipo definido. 
     */
    public static void main14(String args[]) {
        int[] primo = new int[7];

        primo[0] = 1;
        primo[1] = 2;
        primo[2] = 3;
        primo[3] = 5;

        for (int i = 0; i < primo.length; i++) {
            System.out.println(primo[i]);
        }
    }

    /*
    Criação dinâmica de um vetor 
    O comprimento de um vetor pode ser definido de forma dinâmica, 
    por meio do valor de um variável. 
     */
    public static void main15(String args[]) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite a quantidade de jogadores: ");
        int n = teclado.nextInt();

        String[] equipe = new String[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Digite o nome do jogador " + i + ": ");
            equipe[i] = teclado.next();
        }

        for (int i = 0; i < n; i++) {
            System.out.println(equipe[i]);
        }
    }

    /*
    Matriz
    Os elementos de uma sequência também podem ser sequências, 
    ou seja, o tipo de dos elementos de um vetor pode ser um 
    vetor de dados de certo tipo. Nesse caso, diz-se que a 
    variável é um vetor bidimensional ou, simplesmente, que a 
    variável é uma matriz. 
     */
    public static void main16(String args[]) {

        int[][] vendas = {{40, 32, 30}, {20, 26, 38}};

        for (int i = 0; i < 2; i++) {

            System.out.print("Vendedor " + i + ": ");

            for (int j = 0; j < 3; j++) {
                System.out.print(vendas[i][j]);
                System.out.print(" ");
            }

            System.out.println();
        }
    }

    /*
    ****** Dimensões variáveis  ********
    Como mencionado, os comprimentos das sequências em uma sequência de 
    sequências não precisam ser iguais.   
     */
    public static void main17(String args[]) {

        int[][] vendas = {{40, 32, 30}, {20, 26}, {10, 4, 18, 40}};

        for (int i = 0; i < vendas.length; i++) {

            System.out.print("Vendedor " + i + ": ");

            for (int j = 0; j < vendas[i].length; j++) {
                System.out.print(vendas[i][j]);
                System.out.print(" ");
            }

            System.out.println();
        }
    }

    /*
    Dimensões dinâmicas 
    As dimensões de uma matriz também podem ser definidas de forma 
    dinâmica. No exemplo a seguir, a matriz T de valores do tipo 
    double é criada com m linhas e n colunas, sendo que m e n são 
    variáveis do tipo int. 
     */
    public static void main18(String args[]) {

        int m = 4;
        int n = 5;
        double[][] T = new double[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                T[i][j] = 1.0;
            }
        }
        for (int i = 0; i < m; i++) {
            // System.out.println();   // remova '//' do inincio desta linha
            for (int j = 0; j < n; j++) {
                System.out.print(T[i][j]);  // acrescente +"\t" depois de [j]
            }
        }
    }

    /*
    PBL 01
     */
    public static void main19(String[] args) {

        Scanner teclado = new Scanner(System.in);

        // 01    escreva "Digite o valor do primeiro termo da PA: "
        System.out.println("Digite o valor do primeiro termo da PA: ");

        // 02    leia a_1
        double a_1 = teclado.nextDouble();

        // 03    escreva "Digite a razão da PA: "
        System.out.println("Digite a razão da PA: ");

        // 04    leia r
        double r = teclado.nextDouble();

        // 05    escreva "Digite o número de termos da PA: "
        System.out.println("Digite o número de termos da PA: ");

        // 06    leia n
        int n = teclado.nextInt();

        // 07    a_n = a_1 + (n-1) * r
        double a_n = a_1 + ((n - 1) * r);

        // 08    escreva "Último termo da PA: "
        System.out.print("Último termo da PA: ");
        // 09    escreva a_n
        System.out.println(a_n);

        // 10    S_n = (a_1 + a_n) * n / 2
        double S_n = (a_1 + a_n) * n / 2;

        // 11    escreva "Soma de todos os termos da PA: "
        System.out.print("Soma de todos os termos da PA: ");
        // 12    escreva S_n
        System.out.println(S_n);

    }

    /*
    PBL 02
     */
    public static void main20(String[] args) {
        Scanner teclado = new Scanner(System.in);
        
        // leia a
        System.out.println("Digite o limite inferior a: ");
        double a = teclado.nextDouble();
        // leia b
        
        System.out.println("Digite o limite superior b: ");
        double b = teclado.nextDouble();
        
        // se a <= b
        if (a <= b) {
        //     leia n
               System.out.println("Digite o valor de n: ");
               double n = teclado.nextInt();
               
        //     se n > 0
               if (n > 0){
        //         area_total = 0
                   double area_total =  0;
        //         x = a
                   double x = a;
        //         h = (b - a) / n
                   double h = (b - a) / n;
        //         y1 = f(x)
                   double y1 = (2 * Math.sin(x)) + (Math.cos(x) / 3);
        //         i = 0
                   int i =  0;
           
                   double y2;
                   double area_trapezio;
                   
        //         enquanto i < n
                   while (i < n){
        //             x = x + h
                       x = x + h;
                       
        //             y2 = f(x)
                       y2 = (2 * Math.sin(x)) + (Math.cos(x) / 3);
                       
        //             area_trapezio = ((y1 + y2) / 2) * h
                       area_trapezio = ((y1 + y2) / 2) * h;
                       
        //             area_total = area_total + area_trapezio
                       area_total = area_total + area_trapezio;
                       
        //             y1 = y2
                       y1 = y2;
                       
        //             i = i + 1
                       i = i + 1;       // ou i++;
                   }
        //         escreva area_total
                   System.out.println("area_total: "+area_total);
               }else{
        //     senão
        //         escreva " Erro: o valor de n deve ser maior que zero"
                   System.out.println(" Erro: o valor de n deve ser maior que zero");
               }
        // senão
        }else{
        //     escreva "Erro: valor de a deve ser menor ou igual ao valor de b"
               System.out.println("Erro: valor de a deve ser menor ou igual ao valor de b");
        }
    }
}
