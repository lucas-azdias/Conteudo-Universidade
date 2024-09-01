package pgarquivo;

public class ArquivoImagem extends ArquivoAplicacao {

        public ArquivoImagem(String nm){
            super(nm);
        }
        
         @Override
        public void listar(int nivel) {
               super.tabular(nivel);
               System.out.println("ArquivoImagem: " + this.nome);
	}

}
