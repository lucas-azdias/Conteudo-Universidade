
public class Solicitado extends Estado{

	public Estado cotacao() {
//		System.out.println("Classe Solicitado");
		return new Cotado();
	}
}
