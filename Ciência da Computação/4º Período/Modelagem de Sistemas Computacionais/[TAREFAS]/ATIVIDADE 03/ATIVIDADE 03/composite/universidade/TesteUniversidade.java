package universidade;

import modelo.Elemento;
import modelo.MyException;

public class TesteUniversidade {
    
    private static Elemento criarInstancias(){

        Elemento pucpr = new Universidade("PUCPR");

        Elemento curitiba = new Campus("curitiba");
        Elemento londrina = new Campus("londrina");
        Elemento azul = new Bloco("azul");
        Elemento verde = new Bloco("verde");

        Elemento primeiro = new Andar("primeiro");
        Elemento segundo = new Andar("segundo");
        Elemento terceiro = new Andar("terceiro");
        Elemento quarto = new Andar("quarto");
        
        Elemento P1 = new Corredor("P1");
        Elemento P2 = new Sala("P2");
        Elemento P3 = new Sala("P3");

        Elemento P4 = new Corredor("P4");
        Elemento P5 = new Sala("P5");
        Elemento P6 = new Laboratorio("P6");

        Elemento P7 = new Laboratorio("P7");
        Elemento P8 = new Auditorio("P8");
        Elemento P9 = new Cantina("P9");

        Elemento P10 = new Sala("P10");
        Elemento P11 = new Sala("P11");
        Elemento P12 = new Laboratorio("P12");

        Elemento L1 = new Auditorio("L1");
        Elemento L2 = new Sala("L2");
        Elemento L3 = new Laboratorio("L3");

        try {
            primeiro.adicionar(P1);
            primeiro.adicionar(P2);
            primeiro.adicionar(P3);

            segundo.adicionar(P4);
            segundo.adicionar(P5);
            segundo.adicionar(P6);

            terceiro.adicionar(P7);
            terceiro.adicionar(P8);
            terceiro.adicionar(P9);

            quarto.adicionar(P10);
            quarto.adicionar(P11);
            quarto.adicionar(P12);

            londrina.adicionar(L1);
            londrina.adicionar(L2);
            londrina.adicionar(L3);

            azul.adicionar(primeiro);
            azul.adicionar(primeiro);

            verde.adicionar(terceiro);
            verde.adicionar(quarto);

            curitiba.adicionar(azul);
            curitiba.adicionar(verde);

            pucpr.adicionar(curitiba);
            pucpr.adicionar(londrina);

            // deve gerar uma exceção, pois P1 não é filho de Composição
            P1.adicionar(P2);

        } catch(MyException e){
            System.out.println( e.getMessage() );
        }

        return pucpr;
    }

    public static void main(String [] args){

        try{
            Elemento praiz = TesteUniversidade.criarInstancias();
            praiz.listar(0);

            System.out.println("\n---------- praiz.listar(0) ----------\n");

            // Crfinado mais uma instância de Ceral
            Elemento P13 = new Corredor("P13");
            // Consultando se a categoria "proteinaAnimal"
            Elemento filho = praiz.consultar("verde");

            // Adicionando a instância de Ceral P13 na Caterogia "proteinaAnimal"
            filho.adicionar(P13);
            filho.listar(0);  // mostrando se na subarvore "proteinaAnimal"
            // foi adicionado P13.
            System.out.println("\n---------- filho.listar(0) ----------\n");

            // Excluindo a subarvore "proteinaAnimal"
            praiz.excluir("verde");

            // Consultando a arvore a partir da raiz.
            filho = praiz.consultar("CRaiz");
            // A subarvore "proteinaAnimal" não deve ser mostrada,
            // pois ela foi excluida.
            filho.listar(0);

            System.out.println("\n--------- filho.listar(0) -----------\n");

            // Tentando excluir a subarvore "proteinaAnimal".
            // Não deve excluir pois ela já foi excluída
            filho = praiz.excluir("verde");
            // Consultando a subarvore "proteinaAnimal"
            filho = praiz.consultar("verde");

        } catch(MyException e){
            System.out.println( e.getMessage() );
        }
    }
}
