public class Amarillo extends Pikinim {
    public Amarillo(int cantidad) {
        super(1, 3, cantidad);
    }

    public void multiplicar(int cantidad) {
        int nuevaCantidad = getCantidad() + (int) Math.ceil(cantidad * 1.5);
        setCantidad(nuevaCantidad); 

    }

    // multiplicar toma la cantidad y setea la nueva cantidad
}
