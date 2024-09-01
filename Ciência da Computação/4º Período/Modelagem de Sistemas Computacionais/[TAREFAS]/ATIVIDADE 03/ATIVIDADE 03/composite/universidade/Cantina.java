package universidade;

import modelo.Folha;

public class Cantina extends Folha {

	public Cantina(String nm) {
		super(nm);
	}
	
	@Override
    public void listar(int nivel) {
        super.tabular(nivel);
        System.out.println("Cantina: " + this.nome);
	}

}
