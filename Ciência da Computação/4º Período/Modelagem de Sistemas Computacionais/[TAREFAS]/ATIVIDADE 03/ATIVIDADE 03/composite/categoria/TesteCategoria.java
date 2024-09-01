package categoria;

import modelo.Elemento;
import modelo.MyException;

public class TesteCategoria {
    
    private static Elemento criarInstancias(){
        
        Elemento craiz = new CategoriaRaiz("craiz");

        Elemento comestivel = new Categoria("comestivel");
        Elemento diversos = new Categoria("diversos");
        Elemento proteinaAnimal = new Categoria("proteinaAnimal");

        Elemento limpeza = new CategoriaFolha("limpeza");
        Elemento cereal = new CategoriaFolha("cereal");
        Elemento bebida = new CategoriaFolha("bebida");
        Elemento defumado = new CategoriaFolha("defumado");
        Elemento carne = new CategoriaFolha("carne");

        Elemento p1 = new Cereal("p1");
        Elemento p2 = new Cereal("p2");
        Elemento p3 = new Cereal("p3");

        Elemento p4 = new Bebida("p4");
        Elemento p5 = new Bebida("p5");
        Elemento p6 = new Bebida("p6");

        Elemento p7 = new Defumado("p7");
        Elemento p8 = new Defumado("p8");
        Elemento p9 = new Defumado("p9");

        Elemento p10 = new Carne("p10");
        Elemento p11 = new Carne("p11");
        Elemento p12 = new Carne("p12");
        
        Elemento l1 = new Limpeza("l1");
        Elemento l2 = new Limpeza("l2");
        Elemento l3 = new Limpeza("l3");

        try {
        cereal.adicionar(p1);
        cereal.adicionar(p2);
        cereal.adicionar(p3);

        bebida.adicionar(p4);
        bebida.adicionar(p5);
        bebida.adicionar(p6);
        
        defumado.adicionar(p7);
        defumado.adicionar(p8);
        defumado.adicionar(p9);
        
        carne.adicionar(p10);
        carne.adicionar(p11);
        carne.adicionar(p12);
        
        limpeza.adicionar(l1);
        limpeza.adicionar(l2);
        limpeza.adicionar(l3);
        
        diversos.adicionar(cereal);
        diversos.adicionar(bebida);
        
        proteinaAnimal.adicionar(defumado);
        proteinaAnimal.adicionar(carne);

        comestivel.adicionar(diversos);
        comestivel.adicionar(proteinaAnimal);

        craiz.adicionar(limpeza);
        craiz.adicionar(comestivel);   
        
        } catch(MyException e){
            System.out.println( e.getMessage() );
        }
        
        return craiz;
    }
    public static void main(String[] args) {
        try{
            Elemento craiz = criarInstancias(); 
            craiz.listar(0);
        
            System.out.println("\n");    

            Elemento t4 = new Limpeza("t4");
            Elemento filho = craiz.consultar("proteinaAnimal");
        
            filho.adicionar(t4);
            filho.listar(0);
            
            
            //craiz.excluir("proteinaAnimal");
            
            filho = craiz.consultar("craiz");
            filho.listar(0);
            filho = craiz.excluir("proteinaAnimal");
            //filho = craiz.consultar("proteinaAnimal");
            filho = craiz.excluir("diversos");
            craiz.listar(0);
            
           
        } catch(MyException e){
            System.out.println( e.getMessage() );
        }
    }
}
