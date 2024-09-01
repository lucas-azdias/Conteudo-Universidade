
package fabrica;

import iinterface.PizzaDeCostela;
import iinterface.PizzaDeMignon;
import iinterface.PizzaDeQueijo;
import iinterface.PizzaVegetariana;
import modelo.catarinense.PizzaDeCostelaCatarinense;
import modelo.catarinense.PizzaDeMignonCatarinense;
import modelo.catarinense.PizzaDeQueijoCatarinense;
import modelo.catarinense.PizzaVegetarianaCatarinense;


// Concrete Factory para Pizza Catarinense
public class FabricaDePizzaCatarinense implements FabricaDePizza {
    @Override
    public PizzaDeQueijo criarPizzaDeQueijo() {
        return new PizzaDeQueijoCatarinense();
    }

    @Override
    public PizzaVegetariana criarPizzaVegetariana() {
        return new PizzaVegetarianaCatarinense();
    }

    @Override
    public PizzaDeCostela criarPizzaDeCostela() {
        return new PizzaDeCostelaCatarinense();
    }

    @Override
    public PizzaDeMignon criarPizzaDeMignon() {
        return new PizzaDeMignonCatarinense();
    }
}