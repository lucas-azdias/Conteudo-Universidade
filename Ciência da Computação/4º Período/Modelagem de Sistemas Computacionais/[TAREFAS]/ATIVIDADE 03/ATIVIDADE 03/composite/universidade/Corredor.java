package universidade;

import modelo.Folha;

public class Corredor extends Folha {

	public Corredor(String nm) {
		super(nm);
	}
	
	@Override
    public void listar(int nivel) {
        super.tabular(nivel);
        System.out.println("Corredor: " + this.nome);
	}

}
