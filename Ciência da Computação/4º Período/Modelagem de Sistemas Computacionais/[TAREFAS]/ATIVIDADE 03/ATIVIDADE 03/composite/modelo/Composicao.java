package modelo;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Stack;

public abstract class Composicao extends Elemento {

	public ArrayList<Elemento> elemento;
     
        public Composicao(String nm){
            super(nm);
            this.elemento = new ArrayList<Elemento>();
        }

        @Override
	public boolean adicionar(Elemento d) {
            this.elemento.add( d );
            d.pertenceA( this );
            return false;
	}

        @Override
	public Elemento consultar(String nm) throws MyException {

            Iterator<Elemento> itE = this.elemento.iterator();
            Stack<Elemento> pilha = new Stack<Elemento>();
            
            if (itE.hasNext()){
                pilha.add(this);
            }
                       
            Elemento ptr = null;
            while (!pilha.isEmpty()){
                ptr = pilha.pop();      
                if (ptr.nome.equals(nm)){
                    return ptr;
                }else{
                    if (ptr instanceof Composicao){
                        Iterator<Elemento> it = ((Composicao)ptr).elemento.iterator();
                        while (it.hasNext()){
                            pilha.push(it.next());                        
                        }
                    }
                }
            }
            throw new MyException("Elemento não encontrado : op->consulta");
	}

        @Override
	public Elemento excluir(String nm) throws MyException {
            
           Iterator<Elemento> itE = this.elemento.iterator();
           Stack<Elemento> pilha = new Stack<Elemento>();
            
            if (itE.hasNext()){
                pilha.add(this);
            }
                       
            //ArrayList<Elemento> ptrA = this.elemento;
            //String ptrAnome = null;
            Elemento ptr  = this;
            while (!pilha.isEmpty()){
                ptr = pilha.pop();      
                if (ptr.nome.equals(nm)){
                    if (ptr.pertenceA != null){
                        ((Composicao)ptr.pertenceA).elemento.remove(ptr);
                    }
                    return ptr;
                }else{
                    if (ptr instanceof Composicao){
                        Iterator<Elemento> it = ((Composicao)ptr).elemento.iterator();
                        while (it.hasNext()){
                            pilha.push(it.next());                        
                        }
                    }
                }
            }
            throw new MyException("Elemento não encontrado : op->excluir");
        }

        @Override
	public void listar(int nivel) {
            tabular(nivel);
            System.out.println(this.nome);
            for (Elemento e : this.elemento){
                e.listar(nivel + 1);
            }
	}
}
