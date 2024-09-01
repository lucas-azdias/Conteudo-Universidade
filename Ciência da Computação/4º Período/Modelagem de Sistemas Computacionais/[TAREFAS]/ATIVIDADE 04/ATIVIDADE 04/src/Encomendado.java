
public class Encomendado extends Estado {

	public Estado entrega() {
//		System.out.println("Classe Encomendado");
		return new Faturado();
	}
	
	public Estado cancela() {
//		System.out.println("Classe Encomendado");
		return new Cancelado();
	}
}
