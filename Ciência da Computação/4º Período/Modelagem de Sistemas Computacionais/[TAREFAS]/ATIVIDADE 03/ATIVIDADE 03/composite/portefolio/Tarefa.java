package portefolio;

import modelo.Folha;

public class Tarefa extends Folha {

	public Tarefa(String nm) {
		super(nm);
	}
	
	@Override
    public void listar(int nivel) {
        super.tabular(nivel);
        System.out.println("Tarefa: " + this.nome);
	}

}
