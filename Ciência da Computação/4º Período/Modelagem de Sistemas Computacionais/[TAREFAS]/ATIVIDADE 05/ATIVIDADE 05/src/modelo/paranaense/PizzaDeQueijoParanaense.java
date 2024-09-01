
package modelo.paranaense;

import iinterface.PizzaDeQueijo;


// Concrete Products para Pizza Gaúcha
public class PizzaDeQueijoParanaense implements PizzaDeQueijo {
    
    @Override
    public String preparar() {
        return "Pizza Paranaense de Quatro Queijos";
    }
}
