
public class Pildora extends Zona{
    private int cantidad;
    Pildora(int cantidad){
        this.cantidad = cantidad;
    };

    public void Interactuar(Pikinim pikinim){
        setCompletar(true); 
        System.out.println(getCompletar());
        pikinim.multiplicar(cantidad);
    }

    //Interactuar consume la pildora y llama a multiplicar del pikinim escogido
    public int getCantidad(){
        return cantidad;
    }

    //retorna la cantidad

    public void setCantidad(int cantidad){
        this.cantidad = cantidad;
    }
    //setea la cantidad
}