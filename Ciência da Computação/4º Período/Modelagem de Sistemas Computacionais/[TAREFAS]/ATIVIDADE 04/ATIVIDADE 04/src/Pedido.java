
public class 
Pedido {

	private Estado estado;
	public String solicita() {
		this.estado = new Solicitado();
		return "Solicitado";
	}
	public String cotacao() {
		this.estado = this.estado.cotacao();
		return "Cotado";
	}
	public String encomenda() {
		this.estado = this.estado.encomenda();
		return "Encomendado";
	}
	public String entrega() {
		this.estado = this.estado.entrega();
		return "Faturado";
	}
	public String paga() {
		this.estado = this.estado.paga();
		return "Pago";
	}
	public String rejeita() {
		this.estado = this.estado.rejeita();
		return "Rejeitado";
	}
	public String cancela() {
		this.estado = this.estado.cancela();
		return "Cancelado";
	}
	public String arquiva() {
		this.estado = this.estado.arquiva();
		return "FIM";
	}
}
