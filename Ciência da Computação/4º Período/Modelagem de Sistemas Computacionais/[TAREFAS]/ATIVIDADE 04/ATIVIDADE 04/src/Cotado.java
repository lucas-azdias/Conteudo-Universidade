
public class Cotado extends Estado {
	
	public Estado encomenda() {
//		System.out.println("Classe Cotado");
		return new Encomendado();
	}
	
	public Estado rejeita() {
//		System.out.println("Classe Cotado");
		return new Rejeitado();
	}
}
