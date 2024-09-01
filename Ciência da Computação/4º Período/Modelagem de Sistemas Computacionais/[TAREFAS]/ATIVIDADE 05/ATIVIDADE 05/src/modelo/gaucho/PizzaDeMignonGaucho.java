
package modelo.gaucho;

import iinterface.PizzaDeMignon;


public class PizzaDeMignonGaucho implements PizzaDeMignon {

    @Override
    public String preparar() {
        return "Pizza Gaúcha de Mignon";
    }
}