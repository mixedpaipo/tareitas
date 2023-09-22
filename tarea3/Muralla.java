public class Muralla extends Zona{
    private int vida;

    Muralla(int vida){
        this.vida = vida;
    }
    public void Interactuar(Pikinim[] pikinims){
        if (TryRomper(pikinims)){
            setCompletar(true)
        }
    }
    public boolean TryRomper(Pikinim[] pikinims){
        int suma = 0;
        for(Pikinim pikinim : pikinims){
            suma = pikinim.getCantidad()*pikinim.getAtaque();
        }
        if (suma >= vida){
            return true;
        }
        else{
            return false;
        }
    }

    public void getVida(){
        return vida;
    }

    public void setVida(int vida){
        this.vida = vida;
    }
}