
package fabrica;

import iinterface.PizzaDeCostela;
import iinterface.PizzaDeMignon;
import iinterface.PizzaDeQueijo;
import iinterface.PizzaVegetariana;
import modelo.paulista.PizzaDeCostelaPaulista;
import modelo.paulista.PizzaDeMignonPaulista;
import modelo.paulista.PizzaDeQueijoPaulista;
import modelo.paulista.PizzaVegetarianaPaulista;


// Concrete Factory para Pizza Paulista

public class FabricaDePizzaPaulista implements FabricaDePizza {

    @Override
    public PizzaDeQueijo criarPizzaDeQueijo() {
        return new PizzaDeQueijoPaulista();
    }

    @Override
    public PizzaVegetariana criarPizzaVegetariana() {
        return new PizzaVegetarianaPaulista();
    }

    @Override
    public PizzaDeCostela criarPizzaDeCostela() {
        return new PizzaDeCostelaPaulista();
    }

    @Override
    public PizzaDeMignon criarPizzaDeMignon() {
        return new PizzaDeMignonPaulista();
    }
}
