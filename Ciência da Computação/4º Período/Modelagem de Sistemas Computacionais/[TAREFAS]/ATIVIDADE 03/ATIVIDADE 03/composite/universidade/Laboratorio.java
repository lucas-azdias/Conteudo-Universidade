package universidade;

import modelo.Folha;

public class Laboratorio extends Folha {

	public Laboratorio(String nm) {
		super(nm);
	}
	
	@Override
    public void listar(int nivel) {
        super.tabular(nivel);
        System.out.println("Laboratorio: " + this.nome);
	}

}
