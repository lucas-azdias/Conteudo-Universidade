
package fabrica;

import iinterface.PizzaDeCostela;
import iinterface.PizzaDeMignon;
import iinterface.PizzaDeQueijo;
import iinterface.PizzaVegetariana;
import modelo.gaucho.PizzaDeCostelaGaucho;
import modelo.gaucho.PizzaDeMignonGaucho;
import modelo.gaucho.PizzaDeQueijoGaucho;
import modelo.gaucho.PizzaVegetarianaGaucho;


// Concrete Factory para Pizza Gaúcha

public class FabricaDePizzaGaucho implements FabricaDePizza {

    @Override
    public PizzaDeQueijo criarPizzaDeQueijo() {
        return new PizzaDeQueijoGaucho();
    }

    @Override
    public PizzaVegetariana criarPizzaVegetariana() {
        return new PizzaVegetarianaGaucho();
    }

    @Override
    public PizzaDeCostela criarPizzaDeCostela() {
        return new PizzaDeCostelaGaucho();
    }

    @Override
    public PizzaDeMignon criarPizzaDeMignon() {
        return new PizzaDeMignonGaucho();
    }
}
