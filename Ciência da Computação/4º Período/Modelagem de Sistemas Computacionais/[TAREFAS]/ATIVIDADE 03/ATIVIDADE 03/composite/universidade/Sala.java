package universidade;

import modelo.Folha;

public class Sala extends Folha {

	public Sala(String nm) {
		super(nm);
	}
	
	@Override
    public void listar(int nivel) {
        super.tabular(nivel);
        System.out.println("Sala: " + this.nome);
	}

}
