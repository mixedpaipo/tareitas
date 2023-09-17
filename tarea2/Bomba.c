#include "Tierra.h"
#include "Bomba.h"
#include "Tablero.h"
#include <stdio.h>
#include <stdlib.h>

extern void*** tablero;
extern int** bombas;

void TryExplotar(int fila, int columna){
    Bomba* bomb = ((Bomba*)tablero[fila][columna]);
    bomb->contador_turnos--;
    if (bomb->contador_turnos == 0){
        bomb->explotar(fila, columna);
    }
    return;
}

void BorrarBomba(int fila, int columna){
    Bomba* bomb = ((Bomba*)tablero[fila][columna]);
    tablero[fila][columna] = bomb->tierra_debajo; 
    bombas[fila][columna] = 0;
    free(bomb); 
    return;
}

void ExplosionPunto(int fila, int columna){
    Bomba* bomb = ((Bomba*)tablero[fila][columna]);
    bomb->tierra_debajo->vida-=3;
    if(bomb->tierra_debajo->vida <= 0){
        bomb->tierra_debajo->vida = 0;
    };
    BorrarBomba(fila,columna);
    return;
}

void ExplosionX(int fila, int columna){
    int f[]= {-1, 1, -1, 1};
    int c[] = {-1, 1, 1, -1};
    Bomba* bomb = ((Bomba*)tablero[fila][columna]);
    bomb->tierra_debajo->vida-=1;
    BorrarBomba(fila,columna);
    for(int i = 0; i < 4; i++){
        int nueva_fila = fila + f[i];
        int nueva_columna = columna + c[i];
        printf("%d", nueva_fila);
        if (nueva_fila >= 0 && nueva_fila < dimension && nueva_columna >= 0 && nueva_columna < dimension){
            if (tablero[nueva_fila][nueva_columna] != NULL) {
                Tierra *tierra = (Tierra *)tablero[nueva_fila][nueva_columna];
                if (tierra->vida <= 0){
                    tierra->vida = 0;}

                else{
                tierra->vida--;}
            }
        }
        else {
            int nueva_f = -f[i];
            int nueva_c = -c[i];
            nueva_fila = fila + nueva_f;
            nueva_columna = columna + nueva_c;
            if (nueva_fila >= 0 && nueva_fila < dimension && nueva_columna >= 0 && nueva_columna < dimension) {
                Tierra *tierra = (Tierra *)tablero[nueva_fila][nueva_columna];
                if (tierra->vida <= 0){
                    tierra->vida = 0;
                }
                else{
                tierra->vida--;}
            }
        }
    }
}