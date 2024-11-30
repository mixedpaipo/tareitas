#include <iostream>
#include <deque>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

// Clase página
class pagina {
    public:
        int num_pagina;
        vector<int> bit;    // bit[0]: V, bit[1]: U, bit[2]: D
        int frame;          // Frame asignado

        // Constructor
        pagina(int num_pagina) : num_pagina(num_pagina), bit(3, 0), frame(-1) {}

        // Modificar frame
        void modificar_frame(int nuevo_frame) {
            frame = nuevo_frame;
        }

        // Cargar página en memoria (bit v = 1)
        void cargar_pagina() {
            bit[0] = 1;  
        }

        // Modificar bits según la operación (R, W, F, f) Siendo R: Read, W: Write, F: Free frame, f: free page
        void modificar_bits(char operacion) {
        // Lectura
        if (operacion == 'R') {
            bit[1] = 1;  // Lectura marca el bit de uso
        } 

        // Escritura
        else if (operacion == 'W') {
            bit[1] = 1;  // Bit U = 1
            bit[2] = 1;  // Bit D = 1
        } 

        // Liberar frame
        else if (operacion == 'F') {
            bit[0] = 0;  // Bit V = 0
            frame = -1;  // El frame se libera
        } 

        // Liberar página
        else if (operacion == 'f') {
            bit[0] = 0;  // Bit V = 0, se libera la página
            bit[1] = 0;  // Bit U = 0, se libera el bit de uso
            bit[2] = 0;  // Bit D = 0, se libera el bit de modificación
            frame = -1;  // El frame se libera
        }
    }

    // Obtiene el bit V
    int get_bit_v() const {
        return bit[0];
    }

    // Obtiene el número de página
    int get_num_pagina() const {
        return num_pagina;
    }

    // Obtiene el número de frame
    int get_frame() const {
        return frame;
    }
};


// Verifica si el frame está siendo ocupado, retorna true si lo está, y false en el caso contrario
bool check_frame(const vector<pagina>& paginas_vector, int frame) {
    for (int i = 0; i < paginas_vector.size(); i++) {
        if (paginas_vector[i].get_frame() == frame) { // Si la el frame está asignado a una página
            return true;
        }
    }
    return false;
}

// Verificar si la página está cargada en memoria
bool verificar_carga(const vector<pagina>& paginas_vector, int pagina) {
    if (pagina < 0 || pagina >= paginas_vector.size()) {
        return false;                                      // Página no existe
    }
    return paginas_vector[pagina].get_bit_v() == 1;        // Bit V = 1, página cargada
}

// Liberar frame, se añade de vuelta a la cola de frames disponibles
void liberar_frame(deque<int>& frames, int frame) {
    frames.push_back(frame);                       // Se añade el frame a la cola de frames disponibles
}

// Operaciones
void operaciones(vector<pagina>& paginas_vector, char operacion, int num, deque<int>& frames, vector<int>& paginas_activas) {
    // Validación del índice de página
    if (num < 0 || num >= paginas_vector.size()) {
        cerr << "Error: Índice de página fuera de rango: " << num << "\n";   // Página no existe
        return;
    }

    if (operacion == 'R' || operacion == 'W') {
        // Si la página no está en memoria
        if (!verificar_carga(paginas_vector, num)) {
            if (!frames.empty()) {
                int frame = frames.front(); // Se obtiene el primer frame disponible
                frames.pop_front();         // Se elimina de la cola de frames disponibles

                // cout << "Asignando frame " << frame << " a página " << pagina << endl;      // Debug

                // Cargar la página en el frame
                paginas_vector[num].modificar_frame(frame);      // Asigna el frame a la página
                paginas_vector[num].cargar_pagina();             // La página se carga en la memoria, bit V = 1
                paginas_vector[num].modificar_bits(operacion);   // Se modifican los bits según la operación
            } 
            
            else {
                // Si no hay frames disponibles se reemplaza por una página activa (que está en la memoria) con FIFO
                int pagina_a_reemplazar = paginas_activas.front();
                paginas_activas.erase(paginas_activas.begin());     // Se elimina de la lista de páginas activas

                int frame = paginas_vector[pagina_a_reemplazar].get_frame();    // Se obtiene el frame de la página a reemplazar

                // Descargar la página reemplazada
                paginas_vector[pagina_a_reemplazar].modificar_bits('f');
                cout << "Reemplazando: Liberando frame " << frame << " de página " << pagina_a_reemplazar << endl;

                // Asignar el frame liberado a la nueva página
                paginas_vector[num].modificar_frame(frame);
                paginas_vector[num].cargar_pagina();
                paginas_vector[num].modificar_bits(operacion);
            }
        } else {
            // Si la página ya está en la memoria solo se realiza la operación
            paginas_vector[num].modificar_bits(operacion);
        }

        // Añadir la página a la lista de páginas activas si es que no lo está
        if (find(paginas_activas.begin(), paginas_activas.end(), num) == paginas_activas.end()) {
            paginas_activas.push_back(num);
        }
    } else if (operacion == 'F') {              // Se libera el F(i)
        // Liberar frame asociado a la página
        for (int i = 0; i < size(paginas_vector); i++){

            // Si la página está en memoria y tiene el frame a liberar
            // Liberamos el frame de la página mientras la página se queda con sus bits
            
            if (paginas_vector[i].get_bit_v() == 1 && paginas_vector[i].get_frame() == num) {    
                int frame = paginas_vector[i].get_frame();
                paginas_vector[i].modificar_bits('F');      // Liberar página
                liberar_frame(frames, frame);               // Devolver frame a la lista

                // cout << "Liberando frame " << frame << " de página " << i << endl;      // Debug

                // Eliminar la página de las activas
                paginas_activas.erase(remove(paginas_activas.begin(), paginas_activas.end(), i), paginas_activas.end());
            } 
        }
    }
}

// Mostrar la tabla de páginas
void mostrar_tabla(const vector<pagina>& paginas_vector) {
    cout << "Tabla de páginas:\n";
    cout << "Página\tV\t U\t D\tFrame\n";
    for (int i = 0; i < paginas_vector.size(); i++) {
        cout << i << "\t" << paginas_vector[i].get_bit_v() << "\t" << paginas_vector[i].bit[1] << "\t" << paginas_vector[i].bit[2] << "\t" << paginas_vector[i].get_frame() << "\n";
    }
}

// Crear páginas
vector<pagina> crear_paginas(int num_paginas) {
    vector<pagina> paginas;
    for (int i = 0; i < num_paginas; i++) {
        paginas.push_back(pagina(i));       // Inicializa las páginas con el número de página correspondiente
    }                                       // Comenzando desde el 0
    return paginas;
}

// Main (MMU)
int main(int argc, char* argv[]) {
    // Validar argumentos de entrada
    if (argc < 4) {
        cerr << "Uso: ./mmu <num_paginas> <num_frames> <archivo_entrada>\n";
        return 1;
    }

    // Parámetros de entrada
    int num_paginas = stoi(argv[1]);
    int num_frames = stoi(argv[2]);
    string archivo_entrada = argv[3];

    deque<int> frames;              // Cola de frames disponibles
    vector<int> paginas_activas;    // Lista de páginas activas

    // Inicializar frames disponibles
    for (int i = 0; i < num_frames; i++) {
        frames.push_back(i);            // Se añaden los frames a la cola
    }

    // Crear vector de páginas
    vector<pagina> paginas_vector = crear_paginas(num_paginas);

    // Abrir archivo de entrada
    ifstream archivo(archivo_entrada);
    if (!archivo.is_open()) {
        cerr << "No se pudo abrir el archivo " << archivo_entrada << ".\n";
        return 1;
    }

    cout << "Páginas virtuales: " << num_paginas << "\n";
    cout << "Frames: " << num_frames << "\n";
    cout << "Leyendo archivo: " << archivo_entrada << ".\n";

    string linea;
    while (getline(archivo, linea)) {
        stringstream ss(linea);
        char operacion;

        int num;

        ss >> operacion >> num;

        if (num < 0 || num >= num_paginas) {
            cerr << "Error: Página inválida " << num << ".\n";
            continue;
        }

        operaciones(paginas_vector, operacion, num, frames, paginas_activas);
    }
    mostrar_tabla(paginas_vector);
    archivo.close();
    return 0;
}


/*Las operaciones R, W funcinan de la siguiente manera:
1. Si la página no está en memoria, se asigna un frame disponible a la página y se carga en memoria.
2. Si la página ya está en memoria, se actualizan los bits de uso y modificación.
3. Si no hay frames disponibles, se reemplaza por una página activa (que está en la memoria) con FIFO.

La operación F:
1. Libera el frame i de su asociación con una página
2. Y pone el bit V de la página en 0

La operación f:
1. Hace el reemplazo de páginas
2. Libera los bits V, U, D de la página
3. Libera el frame asociado a la página
 */

// Pía Correa Brenni
// 202273042-0
// Sistemas Operativos
// 2024-2