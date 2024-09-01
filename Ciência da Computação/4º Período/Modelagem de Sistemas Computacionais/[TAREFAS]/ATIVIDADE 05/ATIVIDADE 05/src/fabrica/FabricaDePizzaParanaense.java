
package fabrica;

import iinterface.PizzaDeCostela;
import iinterface.PizzaDeMignon;
import iinterface.PizzaDeQueijo;
import iinterface.PizzaVegetariana;
import modelo.paranaense.PizzaDeCostelaParanaense;
import modelo.paranaense.PizzaDeMignonParanaense;
import modelo.paranaense.PizzaDeQueijoParanaense;
import modelo.paranaense.PizzaVegetarianaParanaense;


// Concrete Factory para Pizza Paranaense

public class FabricaDePizzaParanaense implements FabricaDePizza {

    @Override
    public PizzaDeQueijo criarPizzaDeQueijo() {
        return new PizzaDeQueijoParanaense();
    }

    @Override
    public PizzaVegetariana criarPizzaVegetariana() {
        return new PizzaVegetarianaParanaense();
    }

    @Override
    public PizzaDeCostela criarPizzaDeCostela() {
        return new PizzaDeCostelaParanaense();
    }

    @Override
    public PizzaDeMignon criarPizzaDeMignon() {
        return new PizzaDeMignonParanaense();
    }
}
