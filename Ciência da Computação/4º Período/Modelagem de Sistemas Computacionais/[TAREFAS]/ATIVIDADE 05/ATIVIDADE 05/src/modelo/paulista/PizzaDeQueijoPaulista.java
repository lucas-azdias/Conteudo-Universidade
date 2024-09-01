
package modelo.paulista;

import iinterface.PizzaDeQueijo;


// Concrete Products para Pizza Gaúcha
public class PizzaDeQueijoPaulista implements PizzaDeQueijo {
    
    @Override
    public String preparar() {
        return "Pizza Paulista de Quatro Queijos";
    }
}
