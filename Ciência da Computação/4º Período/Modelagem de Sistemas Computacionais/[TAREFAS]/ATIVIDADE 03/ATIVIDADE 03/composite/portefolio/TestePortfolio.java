package portefolio;

import modelo.Elemento;
import modelo.MyException;

public class TestePortfolio {
    
    private static Elemento criarInstancias() {

        Elemento CRaiz = new Portefolio("Portefolio");

        Elemento projeto1 = new Projeto("projeto1");
        Elemento projeto2 = new ProjetoSimples("projeto2");
        Elemento subprojeto1_1 = new Projeto("subprojeto1_1");
        Elemento subprojeto1_2 = new Projeto("subprojeto1_2");

        Elemento atividade1 = new Atividade("atividade1");
        Elemento atividade2 = new Atividade("atividade2");
        Elemento atividade8 = new Atividade("atividade8");
        Elemento atividade9 = new Atividade("atividade9");

        Elemento T1 = new Tarefa("T1");
        Elemento T2 = new Tarefa("T2");
        Elemento T3 = new Tarefa("T3");

        Elemento T4 = new Tarefa("T4");
        Elemento T5 = new Tarefa("T5");
        Elemento T6 = new Tarefa("T6");

        Elemento T7 = new Tarefa("T7");
        Elemento T8 = new Tarefa("T8");
        Elemento T9 = new Tarefa("T9");

        Elemento T10 = new Tarefa("T10");
        Elemento T11 = new Tarefa("T11");
        Elemento T12 = new Tarefa("T12");

        Elemento TS1 = new Tarefa("TS1");
        Elemento TS2 = new Tarefa("TS2");
        Elemento TS3 = new Tarefa("TS3");

        try {
            atividade1.adicionar(T1);
            atividade1.adicionar(T2);
            atividade1.adicionar(T3);

            atividade2.adicionar(T4);
            atividade2.adicionar(T5);
            atividade2.adicionar(T6);

            atividade8.adicionar(T7);
            atividade8.adicionar(T8);
            atividade8.adicionar(T9);

            atividade9.adicionar(T10);
            atividade9.adicionar(T11);
            atividade9.adicionar(T12);

            projeto2.adicionar(TS1);
            projeto2.adicionar(TS2);
            projeto2.adicionar(TS3);
            
            subprojeto1_1.adicionar(atividade1);
            subprojeto1_1.adicionar(atividade2);

            subprojeto1_2.adicionar(atividade8);
            subprojeto1_2.adicionar(atividade9);

            projeto1.adicionar(subprojeto1_1);
            projeto1.adicionar(subprojeto1_2);

            CRaiz.adicionar(projeto1);
            CRaiz.adicionar(projeto2);

            // deve gerar uma exceção, pois P1 não é filho de Composição
            T1.adicionar(T2);

        } catch(MyException e){
            System.out.println( e.getMessage() );
        }

        return CRaiz;
    }

    public static void main(String [] args){

        try{
            Elemento praiz = criarInstancias();
            praiz.listar(0);

            System.out.println("\n---------- praiz.listar(0) ----------\n");

            Elemento T13 = new Tarefa("T13");

            Elemento filho = praiz.consultar("subprojeto1_2");

            filho.adicionar(T13);
            filho.listar(0);

            System.out.println("\n---------- filho.listar(0) ----------\n");

            praiz.excluir("subprojeto1_2");

            filho = praiz.consultar("CRaiz");

            filho.listar(0);

            System.out.println("\n--------- filho.listar(0) -----------\n");

            filho = praiz.excluir("subprojeto1_2");

            filho = praiz.consultar("subprojeto1_2");

        } catch(MyException e){
            System.out.println( e.getMessage() );
        }
    }
}
