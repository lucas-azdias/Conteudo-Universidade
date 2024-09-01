
package modelo;


public class MyException extends Exception{
    
    private static final long serialVersionUID = 1L;
	//private String msg;
    
    public MyException(String msg){
        super(msg);
    }
}
