
public class Amarillo extends Pikinim{
    private int cantidad;
    public Amarillo(int cantidad){
        super(1,3,cantidad);
    }

    public void multiplicar(int cantidad){
        this.cantidad += (int) Math.ceil(cantidad * 1.5);
    }
}