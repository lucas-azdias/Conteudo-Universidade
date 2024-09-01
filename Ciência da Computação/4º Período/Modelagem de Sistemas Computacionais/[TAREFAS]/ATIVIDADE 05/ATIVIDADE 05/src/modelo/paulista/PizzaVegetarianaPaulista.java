
package modelo.paulista;

import iinterface.PizzaVegetariana;


public class PizzaVegetarianaPaulista implements PizzaVegetariana {

    @Override
    public String preparar() {
        return "Pizza Paulista Vegetariana";
    }
}