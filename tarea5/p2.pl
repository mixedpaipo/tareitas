cerradura(1,4,5,1,0).

deltas(X1, X2, X3, X4, X5, D1, D2, D3, D4, D5) :-
    cerradura(C1, C2, C3, C4, C5),
    D1 is abs(C1 - X1),
    D2 is abs(C2 - X2),
    D3 is abs(C3 - X3),
    D4 is abs(C4 - X4),
    D5 is abs(C5 - X5).
% Deltas es una función que calcula los deltas de Ci-Xi, para tenerlos a
% mano en verificar

verificar(X1, X2, X3, X4, X5, Mensaje) :-
    deltas(X1, X2, X3, X4, X5, D1, D2, D3, D4, D5),
    E is (D1 + D2 + D3 + D4 + D5) / 5,
    %Calculamos la fórmula dada en el pdf
    (
        E > 1 ->
            Mensaje = 'Lejos'
        ; E < 0.0001 ->
            Mensaje = 'Contraseña descubierta'
        ; true ->
            Mensaje = 'Cerca'
    ).
%Dependiendo de el resultado de E, es el mensaje que retornamos :3
