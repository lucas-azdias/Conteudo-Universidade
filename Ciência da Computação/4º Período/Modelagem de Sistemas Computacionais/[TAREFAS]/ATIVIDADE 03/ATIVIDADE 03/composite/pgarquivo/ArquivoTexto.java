package pgarquivo;

public class ArquivoTexto extends ArquivoAplicacao {

        public ArquivoTexto(String nm){
            super(nm);
        }
        
         @Override
        public void listar(int nivel) {
               super.tabular(nivel);
               System.out.println("ArquivoTexto: " + this.nome);
	}

}
