package pgarquivo;

import modelo.MyException;
import modelo.Elemento;
import modelo.Composicao;

public class Teste {
    
    private static Elemento criarInstancias(){
        
        Elemento praiz = new PastaRaiz("praiz");
        Elemento pasta1 = new Pasta("pasta1");
        Elemento psistema = new Pasta("psistema");
        Elemento pasta1_1 = new Pasta("pasta1_1");
        Elemento pasta1_2 = new Pasta("pasta1_2");
        Elemento P_1_1_1 = new Pasta("P_1_1_1");
        Elemento P_1_1_2 = new Pasta("P_1_1_2");
        Elemento P_1_2_1 = new Pasta("P_1_2_1");
        Elemento P_1_2_2 = new Pasta("P_1_2_2");

        Elemento a1 = new ArquivoTexto("a1");
        Elemento a2 = new ArquivoTexto("a2");
        Elemento a3 = new ArquivoTexto("a3");

        Elemento b1 = new ArquivoBinario("b1");
        Elemento b2 = new ArquivoBinario("b2");
        Elemento b3 = new ArquivoBinario("b3");

        Elemento c1 = new ArquivoTexto("c1");
        Elemento c2 = new ArquivoTexto("c2");
        Elemento c3 = new ArquivoTexto("c3");

        Elemento d1 = new ArquivoImagem("d1");
        Elemento d2 = new ArquivoImagem("d2");
        Elemento d3 = new ArquivoImagem("d3");
        
        Elemento t1 = new ArquivoSistema("t1");
        Elemento t2 = new ArquivoSistema("t2");
        Elemento t3 = new ArquivoSistema("t3");

        try {
        P_1_1_1.adicionar(a1);
        P_1_1_1.adicionar(a2);
        P_1_1_1.adicionar(a3);

        P_1_1_2.adicionar(b1);
        P_1_1_2.adicionar(b2);
        P_1_1_2.adicionar(b3);
        
        P_1_2_1.adicionar(c1);
        P_1_2_1.adicionar(c2);
        P_1_2_1.adicionar(c3);
        
        P_1_2_2.adicionar(d1);
        P_1_2_2.adicionar(d2);
        P_1_2_2.adicionar(d3);
        
        psistema.adicionar(t1);
        psistema.adicionar(t2);
        psistema.adicionar(t3);
        
        pasta1_1.adicionar(P_1_1_1);
        pasta1_1.adicionar(P_1_1_2);
        
        pasta1_2.adicionar(P_1_2_1);
        pasta1_2.adicionar(P_1_2_2);

        pasta1.adicionar(pasta1_1);
        pasta1.adicionar(pasta1_2);

        praiz.adicionar(pasta1);
        praiz.adicionar(psistema);   
        
        a1.adicionar(a2);
        
        } catch(MyException e){
            System.out.println( e.getMessage() );
        }
        
        return praiz;
    }
    
    public static void main(String [] args){
        
        try{
            Elemento praiz = criarInstancias(); 
            praiz.listar(0);
        
            System.out.println("\n");    

            Elemento t4 = new ArquivoSistema("t4");
            Elemento filho = praiz.consultar("pasta1_2");
        
            filho.adicionar(t4);
            filho.listar(0);
            
            
            praiz.excluir("pasta1_2");
            
            filho = praiz.consultar("praiz");
            filho.listar(0);
            filho = praiz.excluir("pasta1_2");
            filho = praiz.consultar("pasta1_2");
           
        } catch(MyException e){
            System.out.println( e.getMessage() );
        }
  }
}
