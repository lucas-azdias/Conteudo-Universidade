package universidade;

import modelo.Folha;

public class Auditorio extends Folha {

	public Auditorio(String nm) {
		super(nm);
	}
	
	@Override
    public void listar(int nivel) {
        super.tabular(nivel);
        System.out.println("Auditorio: " + this.nome);
	}

}
