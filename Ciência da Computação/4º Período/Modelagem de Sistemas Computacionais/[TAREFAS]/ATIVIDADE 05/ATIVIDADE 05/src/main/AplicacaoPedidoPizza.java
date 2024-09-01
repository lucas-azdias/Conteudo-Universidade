package main;

import fabrica.FabricaDePizza;
import fabrica.FabricaDePizzaCatarinense;
import fabrica.FabricaDePizzaGaucho;
import fabrica.FabricaDePizzaParanaense;
import fabrica.FabricaDePizzaPaulista;
import iinterface.EstrategiaDePreparo;
import iinterface.PizzaDeCostela;
import iinterface.PizzaDeMignon;
import iinterface.PizzaDeQueijo;
import iinterface.PizzaVegetariana;
import modelo.docorador.DecoradorDeCostelasExtra;
import modelo.docorador.DecoradorDeMignonExtra;
import modelo.docorador.DecoradorDeQueijoExtra;
import modelo.docorador.DecoradorDeVegetaisExtra;
import modelo.preparo.PreparoPremium;
import modelo.preparo.PreparoTradicional;



// Cliente: Exemplo de Uso
public class AplicacaoPedidoPizza {
    
    private static void print(String str){
        System.out.println(str);
    }
    
    public static void main(String[] args) {
    	
        // Abstract Factory: Criando uma fábrica para pizza gaúcha
        FabricaDePizza fabricaDePizzaGaucho = new FabricaDePizzaGaucho();

        // Produtos concretos Products para pizza gaúcha
        PizzaDeQueijo pizzaDeQueijoGaucho = fabricaDePizzaGaucho.criarPizzaDeQueijo();
        PizzaVegetariana pizzaVegetarianaGaucho = fabricaDePizzaGaucho.criarPizzaVegetariana();
        PizzaDeCostela pizzaDeCostelaGaucho = fabricaDePizzaGaucho.criarPizzaDeCostela();
        PizzaDeMignon pizzaDeMignonGaucho = fabricaDePizzaGaucho.criarPizzaDeMignon();

        // Exibindo os sabores de pizza gaúcha
        System.out.println("\nPizza Gaúcha:");
        print(pizzaDeQueijoGaucho.preparar());
        print(pizzaVegetarianaGaucho.preparar());
        print(pizzaDeCostelaGaucho.preparar());
        print(pizzaDeMignonGaucho.preparar());

        // Strategy: Aplicando uma estratégia específica
        EstrategiaDePreparo preparoTradicional = new PreparoTradicional();
        EstrategiaDePreparo preparoPremium     = new PreparoPremium();

        // Decorator: Personalizando as pizzas
        System.out.println("\nPersonalizando Pizzas:");

        // Decorando pizza gaúcha de quatro queijos com preparo tradicional
        PizzaDeQueijo extraQueijoPizzaDeQueijoGaucho = new DecoradorDeQueijoExtra(pizzaDeQueijoGaucho, preparoTradicional);
        print(extraQueijoPizzaDeQueijoGaucho.preparar());

        // Decorando pizza gaúcha vegetariana com vegetais extras e preparo premium
        PizzaVegetariana extraVegetaisPizzaVegetarianaGaucho = new DecoradorDeVegetaisExtra(pizzaVegetarianaGaucho, preparoPremium);
        print(extraVegetaisPizzaVegetarianaGaucho.preparar());

        // Decorando pizza gaúcha de costela com costelas extras
        PizzaDeCostela extraCostelasPizzaDeCostelaGaucho = new DecoradorDeCostelasExtra(pizzaDeCostelaGaucho, preparoTradicional);
        print(extraCostelasPizzaDeCostelaGaucho.preparar());

        // Decorando pizza gaúcha de mignon com mignon extra e preparo premium
        PizzaDeMignon extraMignonPizzaDeMignonGaucho = new DecoradorDeMignonExtra(pizzaDeMignonGaucho, preparoPremium);
        print(extraMignonPizzaDeMignonGaucho.preparar());

        // Abstract Factory: Criando uma fábrica para pizza catarinense
        FabricaDePizza fabricaDePizzaCatarinense = new FabricaDePizzaCatarinense();

        // Concrete Products para pizza catarinense
        PizzaDeQueijo pizzaDeQueijoCatarinense = fabricaDePizzaCatarinense.criarPizzaDeQueijo();
        PizzaVegetariana pizzaVegetarianaCatarinense = fabricaDePizzaCatarinense.criarPizzaVegetariana();
        PizzaDeCostela pizzaDeCostelaCatarinense = fabricaDePizzaCatarinense.criarPizzaDeCostela();
        PizzaDeMignon pizzaDeMignonCatarinense = fabricaDePizzaCatarinense.criarPizzaDeMignon();

        // Exibindo os sabores de pizza catarinense
        System.out.println("\nPizza Catarinense:");
        print(pizzaDeQueijoCatarinense.preparar());
        print(pizzaVegetarianaCatarinense.preparar());
        print(pizzaDeCostelaCatarinense.preparar());
        print(pizzaDeMignonCatarinense.preparar());
        
        // acrescente aqui as chamadas para testar o que foi feito
        
        // PARANAENSE
        FabricaDePizza fabricaDePizzaParanaense = new FabricaDePizzaParanaense();

        // Concrete Products para pizza Paranaense
        PizzaDeQueijo pizzaDeQueijoParanaense = fabricaDePizzaParanaense.criarPizzaDeQueijo();
        PizzaVegetariana pizzaVegetarianaParanaense = fabricaDePizzaParanaense.criarPizzaVegetariana();
        PizzaDeCostela pizzaDeCostelaParanaense = fabricaDePizzaParanaense.criarPizzaDeCostela();
        PizzaDeMignon pizzaDeMignonParanaense = fabricaDePizzaParanaense.criarPizzaDeMignon();
        
        // Exibindo os sabores de pizza Paranaense
        System.out.println("\nPizza Paranaense:");
        print(pizzaDeQueijoParanaense.preparar());
        print(pizzaVegetarianaParanaense.preparar());
        new DecoradorDeCostelasExtra(pizzaDeCostelaParanaense, preparoTradicional);
        print(pizzaDeMignonParanaense.preparar());
        
        
        // PAULISTA
    	FabricaDePizza fabricaDePizzaPaulista = new FabricaDePizzaPaulista();

        // Concrete Products para pizza Paulista
        PizzaDeQueijo pizzaDeQueijoPaulista = fabricaDePizzaPaulista.criarPizzaDeQueijo();
        PizzaVegetariana pizzaVegetarianaPaulista = fabricaDePizzaPaulista.criarPizzaVegetariana();
        PizzaDeCostela pizzaDeCostelaPaulista = fabricaDePizzaPaulista.criarPizzaDeCostela();
        PizzaDeMignon pizzaDeMignonPaulista = fabricaDePizzaPaulista.criarPizzaDeMignon();

        // Exibindo os sabores de pizza Paulista
        System.out.println("\nPizza Paulista:");
        new DecoradorDeQueijoExtra(pizzaDeQueijoPaulista, preparoPremium);
        print(pizzaVegetarianaPaulista.preparar());
        print(pizzaDeCostelaPaulista.preparar());
        print(pizzaDeMignonPaulista.preparar());
        
        PizzaDeQueijo pizza1 = fabricaDePizzaPaulista.criarPizzaDeQueijo();
        new DecoradorDeQueijoExtra(pizza1, preparoPremium);
        
    }
}
