package categoria;

import modelo.Folha;

public class Defumado extends Folha {

	public Defumado(String nm) {
		super(nm);
	}
	
    @Override
    public void listar(int nivel) {
		  super.tabular(nivel);
		  System.out.println("Defumado: " + this.nome);
    }

}
