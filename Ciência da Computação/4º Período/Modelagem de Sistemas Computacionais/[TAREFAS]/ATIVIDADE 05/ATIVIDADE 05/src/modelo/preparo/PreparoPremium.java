

package modelo.preparo;

import iinterface.EstrategiaDePreparo;


public class PreparoPremium implements EstrategiaDePreparo {

    @Override
    public String preparar() {
        return "Preparo Premium";
    }
}