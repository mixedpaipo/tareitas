cerradura(1, 4, 5, 1, 0).
%Cerradura de ejemplo

contar_si_iguales([], [], Contador, Contador).

% Si las lista y la cerradura están vacías en la última recursión, se
% retorna el contador
%
contar_si_iguales([X | Resto1], [Y | Resto2], ContadorActual, Contador) :-
    (X =:= Y ->
        NuevoContador is ContadorActual + 1
    ;
        NuevoContador is ContadorActual
    ),
    contar_si_iguales(Resto1, Resto2, NuevoContador, Contador).

% Va contando la cantidad de números iguales en la lista dada y nuestra
% cerradura
%
verificar(X1, X2, X3, X4, X5, R) :-
    cerradura(C1, C2, C3, C4, C5),
    Lista = [X1, X2, X3, X4, X5],
    %Lista de los dígitos entregados

    contar_si_iguales(Lista, [C1, C2, C3, C4, C5], 0, Cantidad),
    %llama a contar_si_iguales para verificar cuantos dígitos son iguales

    (Cantidad =:= 5 ->
        R = 'Contraseña descubierta'
    ;
        Cantidad < 5 ->
        R = Cantidad
    ).
%Retorna Contraseña descubierta en el caso de que se haya descubierto
%y la cantidad en el caso de que aún falten dígitos iguales


