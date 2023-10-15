public class Cyan extends Pikinim {
    public Cyan(int cantidad) {
        super(1, 1, cantidad);
    }

    public void multiplicar(int cantidad) {
        int nuevaCantidad = getCantidad() + cantidad * 3;
        setCantidad(nuevaCantidad);
    }

    // multiplicar toma la cantidad y setea la nueva cantidad
}
