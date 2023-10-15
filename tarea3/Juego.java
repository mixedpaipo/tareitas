import java.util.Scanner;

public class Juego {
    private int dondetamo = 5;
    private int turnos = 1;
    private int turnototales = 30;
    public static Scanner scanner = new Scanner(System.in);
    private int piezasEncontradas = 0;

    public int getpiezasEncontradas() {
        return piezasEncontradas;
    }

    public void unamas() {
        piezasEncontradas++;
    }

    public static void main(String[] args) {
        Juego start = new Juego();
        Pikinim cyan = new Cyan(10);
        Pikinim magenta = new Magenta(10);
        Pikinim amarillo = new Amarillo(10);

        Pikinim[] grupo = { cyan, magenta, amarillo };
        Zona[] mapa = new Zona[11];
        mapa[0] = new Pieza(50);
        mapa[1] = new Enemigo(130, 20, 25);
        mapa[2] = new Enemigo(50, 10, 15);
        mapa[3] = new Pildora(25);
        mapa[4] = new Muralla(50);
        mapa[5] = new Pieza(100);
        mapa[6] = new Enemigo(45, 8, 10);
        mapa[7] = new Pieza(35);
        mapa[8] = new Pildora(15);
        mapa[9] = new Enemigo(75, 15, 20);
        mapa[10] = new Muralla(150);

        while (start.turnos <= start.turnototales) {
            if (start.turnos == 1) {
                System.out.println("Hemos empezado nuestra aventura para recuperar las 3 piezas de la nave. Mucha suerte aventurerx\n");
            }

            System.out.println(" \n \n Turno número " + start.turnos + " (Pikinims-> Cyan: " + cyan.getCantidad()
                    + " - Magenta: " + magenta.getCantidad() + " - Amarillo: " + amarillo.getCantidad() + ")");

            Zona izquierda = start.dondetamo > 0 ? mapa[start.dondetamo - 1] : mapa[mapa.length - 1];
            Zona centro = mapa[start.dondetamo];
            Zona derecha = start.dondetamo < mapa.length - 1 ? mapa[start.dondetamo + 1] : mapa[0];

            System.out.println("¿Qué decides hacer?\n \n");

            if (izquierda.getCompletar()) {
                System.out.println("1. Moverse a la izquierda (Ya no hay nada más que hacer aquí)");
            } else {
                if (izquierda instanceof Pildora) {
                    System.out.println("1. Moverse a la izquierda (Pildora - Recoge una píldora - Cantidad a multiplicar: "
                            + ((Pildora) izquierda).getCantidad() + ")");
                } else if (izquierda instanceof Pieza) {
                    System.out.println("1. Moverse a la izquierda (Pieza - Recoge una pieza - Peso de la Pieza: "
                            + ((Pieza) izquierda).getPeso() + ")");
                } else if (izquierda instanceof Muralla) {
                    System.out.println(
                            "1. Moverse a la izquierda (Muralla - No puedes moverte debido a una muralla con "
                                    + ((Muralla) izquierda).getVida() + " de vida)");
                } else if (izquierda instanceof Enemigo) {
                    System.out.println("1. Moverse a la izquierda (Enemigo - Vida del Enemigo: "
                            + ((Enemigo) izquierda).getVida() + ")");
                }
            }

            if (centro.getCompletar()) {
                System.out.println("2. Quedarse aquí (No queda nada que hacer)");
            } else {
                if (centro instanceof Pildora) {
                    System.out.println("2. Quedarse aquí (Pildora - Recoge una píldora - Cantidad a multiplicar: "
                            + ((Pildora) centro).getCantidad() + ")");
                } else if (centro instanceof Pieza) {
                    System.out.println("2. Quedarse aquí (Pieza - Recoge una pieza - Peso de la Pieza: "
                            + ((Pieza) centro).getPeso() + ")");
                } else if (centro instanceof Muralla) {
                    System.out.println(
                            "2. Quedarse aquí (Muralla - No puedes moverte debido a una muralla con "
                                    + ((Muralla) centro).getVida() + " de vida)");
                } else if (centro instanceof Enemigo) {
                    System.out.println("2. Quedarse aquí (Enemigo - Enfrenta al enemigo - Vida del Enemigo: "
                            + ((Enemigo) centro).getVida() + ")");
                }
            }

            if (derecha.getCompletar()) {
                System.out.println("3. Moverse a la derecha (Se completó)");
            } else {
                if (derecha instanceof Pildora) {
                    System.out.println("3. Moverse a la derecha (Pildora - Recoge una píldora - Cantidad a multiplicar: "
                            + ((Pildora) derecha).getCantidad() + ")");
                } else if (derecha instanceof Pieza) {
                    System.out.println("3. Moverse a la derecha (Pieza - Recoge una pieza - Peso de la Pieza: "
                            + ((Pieza) derecha).getPeso() + ")");
                } else if (derecha instanceof Muralla) {
                    System.out.println(
                            "3. Moverse a la derecha (Muralla - No puedes moverte debido a una muralla con "
                                    + ((Muralla) derecha).getVida() + " de vida)");
                } else if (derecha instanceof Enemigo) {
                    System.out.println("3. Moverse a la derecha (Enemigo - Vida del Enemigo: "
                            + ((Enemigo) derecha).getVida() + ")");
                }
            }

            int decision = scanner.nextInt();

            if (decision == 1) {
                System.out.println("A la izquierda que nos vamos");
                if (start.dondetamo > 0) {
                    start.dondetamo = start.dondetamo - 1;
                } else {
                    start.dondetamo = mapa.length - 1;
                }
                if (!izquierda.getCompletar()) {
                    if (izquierda instanceof Pildora) {
                        System.out.println("¿Qué Pikinim desea multiplicar? \n 1. Cyan: " + cyan.getCantidad()
                                + "  2. Magenta:" + magenta.getCantidad() + "  3. Amarillo: " + amarillo.getCantidad());
                        int numero = scanner.nextInt() - 1;
                        int cantidad = ((Pildora) izquierda).getCantidad();
                        grupo[numero].multiplicar(cantidad);
                        ((Pildora) izquierda).setCompletar(true);
                    } else if (izquierda instanceof Muralla) {
                        Muralla muralla = (Muralla) izquierda;
                        if (muralla.getVida() > 0) {
                            System.out.println("No puedes atravesar la Muralla. ¡Su vida es demasiado alta!");
                            muralla.Interactuar(grupo);
                        }
                    } else if (izquierda instanceof Enemigo) {
                        ((Enemigo) izquierda).Interactuar(grupo);
                    } else if (centro instanceof Pieza) {
                        ((Pieza) izquierda).Interactuar(grupo);
                    }
                } else {
                    System.out.println("Esta zona ya ha sido completada.");
                }
            } else if (decision == 2) {
                if (!centro.getCompletar()) {
                    if (centro instanceof Pildora) {
                        System.out.println("¿Qué Pikinim desea multiplicar? \n 1. Cyan: " + cyan.getCantidad()
                                + "  2. Magenta:" + magenta.getCantidad() + "  3. Amarillo: " + amarillo.getCantidad());
                        int numero = scanner.nextInt() - 1;
                        int cantidad = ((Pildora) centro).getCantidad();
                        grupo[numero].multiplicar(cantidad);
                        ((Pildora) centro).setCompletar(true);
                    } else if (centro instanceof Muralla) {
                        Muralla muralla = (Muralla) centro;
                        if (muralla.getVida() > 0) {
                            System.out.println("No puedes atravesar la Muralla. ¡Su vida es demasiado alta!");
                            muralla.Interactuar(grupo);
                        }
                    } else if (centro instanceof Enemigo) {
                        ((Enemigo) centro).Interactuar(grupo);
                    } else if (centro instanceof Pieza) {
                        ((Pieza) centro).Interactuar(grupo);
                        if (((Pieza)centro).getCompletar()){
                            start.unamas();
                            System.out.println(start.getpiezasEncontradas());
                            if (start.getpiezasEncontradas() == 3) {
                                System.out.println("¡Encontraste las 3 piezas de la nave! ¡Has ganado!");
                                break;
                            }
                        }
                    }
                } else {
                    System.out.println("Esta zona ya ha sido completada.");
                }
            } else if (decision == 3) {
                System.out.println("A la derecha que nos vamos");
                if (start.dondetamo < mapa.length - 1) {
                    start.dondetamo = start.dondetamo + 1;
                } else {
                    start.dondetamo = 0;
                }
                if (!derecha.getCompletar()) {
                    if (derecha instanceof Pildora) {
                        System.out.println("¿Qué Pikinim desea multiplicar? \n 1. Cyan: " + cyan.getCantidad()
                                + "  2. Magenta:" + magenta.getCantidad() + "  3. Amarillo: " + amarillo.getCantidad());
                        int numero = scanner.nextInt() - 1;
                        int cantidad = ((Pildora) derecha).getCantidad();
                        grupo[numero].multiplicar(cantidad);
                        ((Pildora) derecha).setCompletar(true);
                    } else if (derecha instanceof Muralla) {
                        Muralla muralla = (Muralla) derecha;
                        if (muralla.getVida() > 0) {
                            System.out.println("No puedes atravesar la Muralla. ¡Su vida es demasiado alta!");
                            muralla.Interactuar(grupo);
                        }
                    } else if (derecha instanceof Enemigo) {
                        ((Enemigo) derecha).Interactuar(grupo);
                    } else if (derecha instanceof Pieza) {
                        ((Pieza) derecha).Interactuar(grupo);
                    }
                } else {
                    System.out.println("Esta zona ya ha sido completada.");
                }
            } else if (decision == 4) {
                System.out.println("¡Has decidido salir del juego! Gracias por jugar.");
                break;
            } else {
                System.out.println("Opción inválida");
                start.turnos--;
            }

            start.turnos++;
        }

        if (start.getpiezasEncontradas() < 3) {
            System.out.println("No pudiste encontrar las 3 piezas de la nave, lo lamento aventurerx :(");
        }
        scanner.close();
    }
}
//Comentar Juego se me iba a hacer muy largo, pero funciona y espero que sea entendible