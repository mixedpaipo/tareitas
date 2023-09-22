
public interface ILevantar{
    private int cantidadpiezas;
    abstract public void Levantar(Pikinim[] pikinims);


    public void setCantidadPiezas(int cantidadpiezas){
        this.cantidadpiezas = cantidadpiezas
    }
    public void getCantidadPiezas(){
        return cantidadpiezas;

    }
}