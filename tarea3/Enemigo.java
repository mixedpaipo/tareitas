import java.util.Scanner;
import java.util.Random;

public class Enemigo extends Zona implements ILevantar {
    private int vida;
    private int ataque;
    private int peso;

    Enemigo(int vida, int peso, int ataque) {
        this.vida = vida;
        this.ataque = ataque;
        this.peso = peso;
    }

    public void Interactuar(Pikinim[] pikinims) {
        if (vida > 0) {
            Pelear(pikinims);
        } 
    }
    // Interactuar llama a pelear

    public void Pelear(Pikinim[] pikinims) {
        Random random = new Random();
        int colorAleatorio = random.nextInt(3);
        int ataqueEnemigo = ataque;
        for (Pikinim pikinim : pikinims) {
            ataqueEnemigo += pikinim.getAtaque() * pikinim.getCantidad();
        }
        vida -= ataqueEnemigo;
        pikinims[colorAleatorio].disminuir(ataque);
        if (vida <= 0) {
            Levantar(pikinims);
            vida = 0;
        }
    }
    //Pelear le baja a la vida al enemigo hasta que esta sea menor o igual a 0, en donde los pikinims levantan al enemigo

   public void Levantar(Pikinim[] pikinims) {
    int suma = 0;
    for (Pikinim pikinim : pikinims){
        suma += pikinim.getCapacidad() * pikinim.getCantidad();
    }
    if (suma >= peso) {
        int numero = 0;
        setCompletar(true);
        System.out.println("Has derrotado al Enemigo\n");
        System.out.println("¿Qué Pikinim desea multiplicar? \n 1. Cyan: "+ pikinims[0].getCantidad()+"  2. Magenta: "+ pikinims[1].getCantidad()+"  3. Amarillo: "+ pikinims[2].getCantidad());
        numero = Juego.scanner.nextInt() - 1;
        pikinims[numero].multiplicar(peso);
}
    }
   // Los pikinims levantan al enemigo si y solo si su capacidad por cantidad es mayor al peso

    public int getAtaque() {
        return ataque;
    }

    public int getVida() {
        return vida;
    }

    public int getPeso() {
        return peso;
    }

    // Los getters retornan los atributos

    public void setAtaque(int ataque) {
        this.ataque = ataque;
    }

    public void setVida(int vida) {
        this.vida = vida;
    }

    public void setPeso(int peso) {
        this.peso = peso;
    }
    // Los setters setean los atributos
}
