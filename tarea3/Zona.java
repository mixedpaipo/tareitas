
public class Zona{
    private boolean completado;

    Zona(){
        completado = false;
    }
    public void Interactuar(Pikinim[] pikinim){}

    
    public boolean getCompletar(){
        return completado;
    }

    public void setCompletar(boolean completado){
        this.completado = completado;
    }

    //Setters y Getters e interactuar se implementa en las diferentes zonas
}