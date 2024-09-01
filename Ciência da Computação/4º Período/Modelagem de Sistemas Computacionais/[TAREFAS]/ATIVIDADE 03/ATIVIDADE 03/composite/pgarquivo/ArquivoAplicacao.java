package pgarquivo;

import modelo.Folha;

public abstract class ArquivoAplicacao extends Folha {

        public ArquivoAplicacao(String nm){
            super(nm);
        }
        
        @Override
        public void listar(int nivel) {
               super.tabular(nivel);
               System.out.println("ArquivoAplicacao: " + this.nome);
	}
}
