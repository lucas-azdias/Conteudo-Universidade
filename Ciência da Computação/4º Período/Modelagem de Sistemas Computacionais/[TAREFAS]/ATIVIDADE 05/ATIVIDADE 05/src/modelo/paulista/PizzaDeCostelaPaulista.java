
package modelo.paulista;

import iinterface.PizzaDeCostela;


public class PizzaDeCostelaPaulista implements PizzaDeCostela {
 
    @Override
    public String preparar() {
        return "Pizza Paulista de Costela";
    }
}