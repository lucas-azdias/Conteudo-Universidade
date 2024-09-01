
package pgarquivo;


public class ArquivoBinario extends ArquivoAplicacao {

        public ArquivoBinario(String nm){
            super(nm);
        }
        
         @Override
        public void listar(int nivel) {
               super.tabular(nivel);
               System.out.println("ArquivoBinario: " + this.nome);
	}

}