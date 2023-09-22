
abstract public class Pikinim{
    private int cantidad;
    private int ataque;
    private int capacidad;

    Pikinim(int ataque, int capacidad, int cantidad){
        this.ataque = ataque;
        this.capacidad = capacidad;
        this.cantidad = cantidad;|
    }


    public void disminuir(int cantidad){
        this.cantidad -= cantidad;
    }

    abstract public void multiplicar(int cantidad);

    public int getCapacidad(){
        return capacidad;
    }

    public int getCantidad(){
        return cantidad;
    }

    public int getAtaque(){
        return ataque;
    }
} 