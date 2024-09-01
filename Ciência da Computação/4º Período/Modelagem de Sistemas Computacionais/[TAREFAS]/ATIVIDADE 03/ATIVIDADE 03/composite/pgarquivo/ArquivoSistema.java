
package pgarquivo;


public class ArquivoSistema extends ArquivoAplicacao {

        public ArquivoSistema(String nm){
            super(nm);
        }
        
         @Override
        public void listar(int nivel) {
               super.tabular(nivel);
               System.out.println("ArquivoSistema: " + this.nome);
	}
}