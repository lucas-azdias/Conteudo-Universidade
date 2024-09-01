
package modelo.docorador;

import iinterface.EstrategiaDePreparo;
import iinterface.PizzaDeQueijo;


public class DecoradorDeQueijoExtra extends DecoradorDePizza {

    public DecoradorDeQueijoExtra(PizzaDeQueijo pizza, 
            EstrategiaDePreparo estrategiaDePreparo) 
    {
        super(estrategiaDePreparo);
        
        System.out.println(pizza.preparar());
        System.out.println("Queijo Extra");
    }
}
