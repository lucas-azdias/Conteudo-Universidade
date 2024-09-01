package modelo;

public abstract class Folha extends Elemento {

        public Folha(String nm){
            super(nm);
        }
        
        @Override
        public boolean adicionar(Elemento d) throws MyException {
            throw (new MyException("Operacao não valida em Folha"));
        }
        
        @Override
	public Elemento excluir(String nm) throws MyException {
            throw (new MyException("Operacao não valida em Folha"));
        }

        @Override
        	public Elemento consultar(String nome) throws MyException{
            throw (new MyException("Operacao não valida em Folha"));
        }

        @Override
        public void listar(int nivel){
                tabular(nivel);
        }
}
