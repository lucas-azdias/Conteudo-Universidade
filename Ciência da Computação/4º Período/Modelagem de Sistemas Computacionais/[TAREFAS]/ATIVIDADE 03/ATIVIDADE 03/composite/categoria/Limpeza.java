package categoria;

import modelo.Folha;

public class Limpeza extends Folha {

	public Limpeza(String nm) {
		super(nm);
	}
	
    @Override
    public void listar(int nivel) {
		  super.tabular(nivel);
		  System.out.println("Limpeza: " + this.nome);
    }

}
