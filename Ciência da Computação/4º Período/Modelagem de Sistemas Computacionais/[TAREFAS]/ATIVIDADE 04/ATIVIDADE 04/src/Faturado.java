
public class Faturado extends Estado {

	public Faturado() {
		super();
	}
	
	public Estado paga() {
//		System.out.println("Classe Faturado");
		return new Pago();
	}
}
