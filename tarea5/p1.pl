cifrado([0,0], a).
cifrado([0,1], g).
cifrado([1,0], c).
cifrado([1,1], t).
%Nuestras reglas

descifrar([_], []).

descifrar([], []).
% Las dos anteriores son para si las listas están vacías, pero nu puedo
% eliminar la primera porque no me funciona sin ella pipipi

descifrar([M1,M2|Resto], [R|R2]) :-
    cifrado([M1,M2], R),
    descifrar(Resto, R2).

% Se llama a cifrado para ver si nuestros números calzan con alguna de
% las reglas, para terminar haciendo una recursión de descifrar por si
% la secuencia es más larga que dos dígitos






