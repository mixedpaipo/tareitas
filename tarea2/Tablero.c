#include "Tierra.h"
#include "Bomba.h"
#include "Tablero.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h> 

void*** tablero;
int** bombas;
extern int dimension;
int contador_tesoros;
int tesoros_encontrados;
void IniciarTablero(int n){
    srand(time(NULL));
    tablero = (void***)malloc(n*sizeof(void**));
    bombas = (int**)malloc(n*sizeof(int*));
    for (int i = 0; i < n; i++){
        tablero[i] = (void**)malloc(n * sizeof(void*));
        bombas[i] =(int*)malloc(n * sizeof(int));
        for(int j = 0; j < n; j++){
            bombas[i][j] = 0;
            tablero[i][j] = (struct Tierra*)malloc(sizeof(struct Tierra));
            ((Tierra*)tablero[i][j])->vida = rand() % 3 +1;
            double probabilidad = 0.05;
            double numeroaleatorio = (double)rand() / RAND_MAX;
            if(numeroaleatorio < probabilidad){
                ((Tierra*)tablero[i][j])->es_tesoro = 1;
                contador_tesoros++;
                }
            else {
                ((Tierra*)tablero[i][j])->es_tesoro = 0;
            };
        };
    };
    return;
}

void PasarTurno(){
    for (int i = 0; i < dimension; i++){
        for(int j = 0; j < dimension; j++){
            if(bombas[i][j]){
            TryExplotar(i, j);}
        };
    };

    return;
}


void ColocarBomba(Bomba* b, int fila, int columna){
    Tierra* tierra_abajo = tablero[fila-1][columna-1];
    b->tierra_debajo = tierra_abajo;
    bombas[fila-1][columna-1] = 1;
    tablero[fila-1][columna-1] = b;
}

void MostrarTablero(){
    for (int i = 0; i < dimension; i++) {
        for (int j = 0; j < dimension; j++) {
            if (bombas[i][j]){
                printf("o");
            }
            else if(((Tierra*)tablero[i][j])->vida == 0 && ((Tierra*)tablero[i][j])->es_tesoro){
                printf("*");
                tesoros_encontrados++;
                ;
            }
            else{
            printf("%d", ((Tierra*)tablero[i][j])->vida);
            }

            if (j < dimension - 1) {
                printf(" | ");
            }
        }
        if (i < dimension - 1) {
            printf("\n");
        }
    }
    printf("\n");
    return;
}



void MostrarBombas(){
    for (int fila = 0; fila < dimension; fila++) {
        for (int columna = 0; columna < dimension; columna++) {
            Bomba* bomb = tablero[fila][columna];

            if (bombas[fila][columna]) {
                printf("Turnos para explotar: %d\n", bomb->contador_turnos);
                printf("Coordenada: %d %d\n", fila+1, columna+1);
                
                if (bomb->explotar == ExplosionPunto) {
                    printf("Forma Explosión: ExplosionPunto\n");
                } else if (bomb->explotar == ExplosionX) {
                    printf("Forma Explosión: ExplosionX\n");
                }
                
                if (bomb->tierra_debajo != NULL) {
                    printf("Vida de Tierra Debajo: %d\n\n", bomb->tierra_debajo->vida);
                } else {
                }
            }
        }
    }

return;
}


void VerTesoros(){
    for (int i = 0; i < dimension; i++) {
        for (int j = 0; j < dimension; j++) {
            if (((Tierra*)tablero[i][j])->es_tesoro){
                printf("*");
            }
            else if(bombas[i][j]){
                printf("o");
            }
            else{
            printf("%d", ((Tierra*)tablero[i][j])->vida);
            }

            if (j < dimension - 1) {
                printf(" | ");
            }
        }
        if (i < dimension - 1) {
            printf("\n");
        }
    }
    printf("\n");
    return;
}


void BorrarTablero(){
    if (tablero != NULL) {
        for (int i = 0; i < dimension; i++) {
            if (tablero[i] != NULL) {
                for (int j = 0; j < dimension; j++) {
                    free(tablero[i][j]);
                }
                free(tablero[i]);
                free(bombas[i]);
            }
        }
        free(tablero);
        free(bombas);
    }
}
