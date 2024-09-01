package categoria;

import modelo.Folha;

public class Cereal extends Folha {

	public Cereal(String nm) {
		super(nm);
	}
	
    @Override
    public void listar(int nivel) {
		  super.tabular(nivel);
		  System.out.println("Cereal: " + this.nome);
    }

}
