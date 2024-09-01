
package fabrica;


import iinterface.PizzaDeCostela;
import iinterface.PizzaDeMignon;
import iinterface.PizzaDeQueijo;
import iinterface.PizzaVegetariana;

// Abstract Factory

public interface FabricaDePizza {
    PizzaDeQueijo criarPizzaDeQueijo();
    PizzaVegetariana criarPizzaVegetariana();
    PizzaDeCostela criarPizzaDeCostela();
    PizzaDeMignon criarPizzaDeMignon();
}
