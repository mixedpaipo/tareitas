
public class Pieza extends Zona implements ILevantar{
    private int peso;
    Pieza(int peso){
        this.peso = peso;
    }

    public void Interactuar(Pikinim[] pikinims){
        Levantar(pikinims);
    }

    public void Levantar(Pikinim[] pikinims){
        int suma = 0;
        for (Pikinim pikinim : pikinims){
            suma += (pikinim.getCantidad() * pikinim.getCapacidad());
        }
        if (suma >= peso){
            System.out.println("Se ha recuperado un tesoro.");
            setCantidadPiezas(getCantidadPiezas-1);
            }
        setCompletar(true);
    }
}