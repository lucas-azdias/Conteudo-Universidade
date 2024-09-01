
package modelo.gaucho;

import iinterface.PizzaDeCostela;


public class PizzaDeCostelaGaucho implements PizzaDeCostela {
 
    @Override
    public String preparar() {
        return "Pizza Gaúcha de Costela";
    }
}