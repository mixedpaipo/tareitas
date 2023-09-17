#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Tierra.h"
#include "Bomba.h"
#include "Tablero.h"

int dimension;
extern int contador_tesoros;
extern int tesoros_encontrados;
int main(int argc, char const *argv[]){   
    int numero;
    int turnos = 1;
    int seleccion;
    Bomba* bomb;
    int fila, columna, explosion;
    printf("¡Bienvenido a Treasure Finder! \nIndique el tamaño de su tablero a jugar:\n1. 7x7   2.10x10    3.12x12 \nSu input: ");
    scanf("%d", &numero);
    if(numero == 1){
        dimension = 7;
    }
    else if(numero == 2){
        dimension = 10;
    }
    else if(numero == 3){
        dimension = 12;
    }
    IniciarTablero(dimension);
    printf("Iniciando juego .... listo \n\n");
    while(1){
        if (contador_tesoros == tesoros_encontrados){
            printf("FELICIDADES!!! Encontraste todos los tesoros\n\n");
            break;
        }
        printf("Tablero (Turno %d)\n\n", turnos);
        MostrarTablero();
        printf("\nSeleccione una accion: \n1.Colocar Bomba    2.Mostrar Bombas    3.Mostras Tesoros   4. Salir \nEscoja una opcion: ");
        scanf("%d", &seleccion);
        if(seleccion == 1){
            bomb = (Bomba*)malloc(sizeof(Bomba)); 
            printf("Indique coordenadas de la bomba \nFila: ");
            scanf("%d", &fila);
            printf("Columna: ");
            scanf("%d", &columna);
            printf("Indique forma en que explota la bomba: \n1.Punto    2. X: ");
            scanf("%d", &explosion);
            if(explosion == 1){
                bomb->explotar = ExplosionPunto;
                bomb->contador_turnos = 1;
            }
            else if (explosion == 2){
                bomb->explotar = ExplosionX;
                bomb->contador_turnos = 3;
            }
                ColocarBomba(bomb, fila, columna); 
                turnos++;
                PasarTurno();
        }
        else if(seleccion == 2){
            MostrarBombas();
        }
        else if(seleccion == 3){
            VerTesoros();

        }
        else if(seleccion == 4){
            break;
        }
    };




    BorrarTablero();
    return 0;
}

