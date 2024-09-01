
package modelo.docorador;

import iinterface.EstrategiaDePreparo;
import iinterface.PizzaDeCostela;
import iinterface.PizzaDeMignon;
import iinterface.PizzaDeQueijo;
import iinterface.PizzaVegetariana;


// Decorator: Decoradores para Pizzas
public abstract class DecoradorDePizza 
        implements  PizzaDeQueijo, 
                    PizzaVegetariana, 
                    PizzaDeCostela, 
                    PizzaDeMignon {

    protected EstrategiaDePreparo estrategiaDePreparo;

    public DecoradorDePizza(EstrategiaDePreparo estrategiaDePreparo) {
        this.estrategiaDePreparo = estrategiaDePreparo;
    }

    @Override
    public String preparar() {
        return ("Preparando a pizza com:\n" + estrategiaDePreparo.preparar());
    }
}