
package modelo.paulista;

import iinterface.PizzaDeMignon;


public class PizzaDeMignonPaulista implements PizzaDeMignon {

    @Override
    public String preparar() {
        return "Pizza Paulista de Mignon";
    }
}