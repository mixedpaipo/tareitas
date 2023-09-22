
public class Cyan extends Pikinim{
    private int cantidad;
    public Cyan(int cantidad){
        super(1,1,cantidad);
    }

    public void multiplicar(int cantidad){
        this.cantidad += cantidad * 3;

    }
}