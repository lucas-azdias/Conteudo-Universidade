
package modelo.preparo;

import iinterface.EstrategiaDePreparo;


public class PreparoTradicional implements EstrategiaDePreparo {

    @Override
    public String preparar() {
        return "Preparo Tradicional";
    }
}