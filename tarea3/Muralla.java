public class Muralla extends Zona {
    private int vida;

    Muralla(int vida) {
        this.vida = vida;
    }
    public void Interactuar(Pikinim[] pikinims) {
        if (TryRomper(pikinims)) {
            setCompletar(true);
            System.out.println("La muralla ha sido rota, puedes avanzar");
        } else {
            System.out.println("La muralla sigue en pie.");
        }
    }
    //Interactuar llama a Try Romper y si fue true, manda ese mensajito

    public boolean TryRomper(Pikinim[] pikinims) {
        int suma = 0;
        for (Pikinim pikinim : pikinims) {
            suma += pikinim.getCantidad() * pikinim.getAtaque();
        }
        vida -= suma;
        if (vida < 0){
            vida = 0;
        }
        return vida == 0;
    }

    // Los pikinims rompen la muralla si la vida de la muralla es menor o igual a 0
    public int getVida() {
        return vida;
    }

    public void setVida(int vida) {
        this.vida = vida;
    }

    // Los getters y setters
}
