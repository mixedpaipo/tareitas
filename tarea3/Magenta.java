public class Magenta extends Pikinim {
    public Magenta(int cantidad) {
        super(2, 1, cantidad);
    }

    public void multiplicar(int cantidad) {
        int ataque = getAtaque();
        int nuevaCantidad = getCantidad() + cantidad * ataque;
        setCantidad(nuevaCantidad); 
    }
    // multiplicar toma la cantidad y setea la nueva cantidad
}
