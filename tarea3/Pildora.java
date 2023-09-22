
public class Pildora extends Zona{
    private int cantidad;
    Pildora(int cantidad){
        this.cantidad = cantidad;
    };

    public void Interactuar(Pikinim pikinim){
        pikinim.multiplicar(cantidad);
        setCompletar(true);
    }
}