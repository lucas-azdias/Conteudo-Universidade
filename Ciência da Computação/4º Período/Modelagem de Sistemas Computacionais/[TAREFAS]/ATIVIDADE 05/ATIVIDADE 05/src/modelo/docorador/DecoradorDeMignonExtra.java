
package modelo.docorador;

import iinterface.EstrategiaDePreparo;
import iinterface.PizzaDeMignon;


public class DecoradorDeMignonExtra extends DecoradorDePizza {
    
    public DecoradorDeMignonExtra(PizzaDeMignon pizza, 
            EstrategiaDePreparo estrategiaDePreparo) {
        
        super(estrategiaDePreparo);
        
        System.out.println(pizza.preparar());
        System.out.println("Mignon Extra");
    }
}