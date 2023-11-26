sigue(p1, p2).
sigue(p2, p3).
sigue(p3, p4).
sigue(p4, p5).
sigue(p5, p6).
sigue(p6, p7).
sigue(p7, p8).
sigue(p8, p1).
sigue(p1, p9).
sigue(p1, p15).
sigue(p15, p16).
sigue(p16, p20).
sigue(p21, p22).
sigue(p9, p10).
sigue(p11, p12).
sigue(p12, p13).
sigue(p13, p14).
sigue(p7, p17).
sigue(p17, p18).
sigue(p18, p19).

% construir _lista_precedentes construye una lista de nodos
% precedentes
construir_lista_precedentes(Nodo, Lista) :-
    construir_lista_precedentes_rec(Nodo, [], Lista).

construir_lista_precedentes_rec(Nodo, ListaActual, ListaFinal) :-
    % cuenta cuántas veces el nodo actual está en la lista
    count_occurrences(ListaActual, Nodo, Count),
    % verifica si el nodo actual puede agregarse una vez más
    (Count < 2 ->
        % agrega el nodo actual a la lista de visitados
        append(ListaActual, [Nodo], ListaNueva),
        % encuentra el nodo anterior según las reglasde conexión
        sigue(NodoAnterior, Nodo),
        % llama recursivamente con el nodo anterior y la lista actualizada
        construir_lista_precedentes_rec(NodoAnterior, ListaNueva, ListaFinal)
    ;
        % si el nodo actual ya está dos veces en la lista, no se vuelve a agregar
        ListaFinal = ListaActual
    ).

% predicado principal que verifica si un nodo está en la lista final
principal(Nodo, R) :-
    construir_lista_precedentes(Nodo, Lista),
    % verifica si el nodo de entrada aparece exactamente dos veces en la lista
    % si no aparece dos veces, se retorna "no se encuentra en la ruta"
    (count_occurrences(Lista, Nodo, 2) ->
        R = "Se encuentra en la ruta"
    ;
        R = "No se encuentra en la ruta"
    ).

%contador de cuantas veces aparece un nodo
count_occurrences([], _, 0).
count_occurrences([H|T], E, N) :-
    (H = E -> count_occurrences(T, E, N1), N is N1 + 1 ;
     count_occurrences(T, E, N)).
