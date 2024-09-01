
package modelo.gaucho;

import iinterface.PizzaDeQueijo;


// Concrete Products para Pizza Gaúcha
public class PizzaDeQueijoGaucho implements PizzaDeQueijo {
    
    @Override
    public String preparar() {
        return "Pizza Gaúcha de Quatro Queijos";
    }
}
