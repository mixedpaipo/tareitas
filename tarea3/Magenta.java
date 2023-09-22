

public class Magenta extends Pikinim{
    private int cantidad;
    public Magenta(int cantidad){
        super(2,1,cantidad);
    }

    public void multiplicar(int cantidad){
        int ataque = getAtaque();
        this.cantidad += cantidad * ataque;
    }
}