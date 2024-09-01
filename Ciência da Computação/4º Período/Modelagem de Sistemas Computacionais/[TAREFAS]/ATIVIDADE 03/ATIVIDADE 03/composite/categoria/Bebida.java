package categoria;

import modelo.Folha;

public class Bebida extends Folha {

	public Bebida(String nm) {
		super(nm);
	}
	
    @Override
    public void listar(int nivel) {
		  super.tabular(nivel);
		  System.out.println("Bebida: " + this.nome);
    }

}
