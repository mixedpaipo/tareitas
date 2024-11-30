## Tarea 2 - Sistemas Operativos
**Pía Correa Brenni - 202273042-0**\
**2024-2**

### Compulación simulador
- Para compilar el simulador, 

```
g++ -o mmu mmu.cpp
```

- El cual retornará el archivo de ejucución ```mmu```

### Para la ejecución del simulador MMU
- Recibe como parametros, la cantidad de páginas virtuales, frames y el archivo de operaciones a utilizar, de la siguiente forma

```
 ./mmu <num_paginas> <num_frames> <archivo_entrada>
```

El programa fue probado con la versión de _Ubuntu 22.04.5_

> [IMPORTANTE]
>
> Los archivos de prueba tienen que estar al mismo nivel que mmu.cpp o añadirlos a la carpeta ``Ejemplos`` y ejecutar
> ```
> ./mmu <num_paginas> <num_frames> Ejemplos/<archivo_entrada>
> ```