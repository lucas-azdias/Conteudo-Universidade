
package modelo.catarinense;

import iinterface.PizzaDeQueijo;


// Concrete Products para Pizza Catarinense
public class PizzaDeQueijoCatarinense implements PizzaDeQueijo {

    @Override
    public String preparar() {
        return "Pizza Catarinense de Quatro Queijos";
    }
}
