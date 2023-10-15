
public class Pieza extends Zona implements ILevantar{
    private int peso;
    Pieza(int peso){
        this.peso = peso;
    }
    public void Interactuar(Pikinim[] pikinims){
        Levantar(pikinims);
    }
    // Interactuar llama a Levantar


    public void Levantar(Pikinim[] pikinims){
        int suma = 0;
        for (Pikinim pikinim : pikinims){
            suma += (pikinim.getCantidad() * pikinim.getCapacidad());
        }
        if (suma >= peso){
            System.out.println("Se ha recuperado un tesoro, una de nuestras queridas piezas");
            setCompletar(true);
            }
    }
    // Levantar en resumidas palabras es que si la suma de las cantidades por las capacidades de los pikinims
    // es más que el peso, se recupera un tesoro
    public int getPeso(){
        return peso;
    }
    //retorna el peso

    public void setPeso(int peso){
        this.peso = peso;
    }

    //setea el peso
}