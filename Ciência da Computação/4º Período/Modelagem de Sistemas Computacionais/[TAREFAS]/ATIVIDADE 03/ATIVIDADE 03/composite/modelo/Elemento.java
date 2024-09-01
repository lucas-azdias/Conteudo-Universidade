package modelo;

public abstract class Elemento {

	protected String nome;
	protected Elemento pertenceA;
        
        public Elemento(String nm){
            this.nome = nm;
            this.pertenceA = null;
        }

        public String getNome(){
            return nome;
        }
        
        public void pertenceA(Elemento pertenceA){
             this.pertenceA = pertenceA;           
        }
 
        public Elemento pertenceA(){
             return this.pertenceA;           
        }
                
        protected void tabular(int k) {
            for (int i = 0; i < k; i++) {
                System.out.print("    ");
            }
        }  
        
	abstract public Elemento consultar(String nome) throws MyException;
        abstract public boolean adicionar(Elemento d) throws MyException;
	abstract public Elemento excluir(String nm) throws MyException; 
	public abstract void listar(int nivel);

}
