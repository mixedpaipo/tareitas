cifrado([0,0], a).
cifrado([0,1], g).
cifrado([1,0], c).
cifrado([1,1], t).
%Nuestras reglas

descifrar([_], []).

descifrar([], []).
% Las dos anteriores son para si las listas est�n vac�as, pero nu puedo
% eliminar la primera porque no me funciona sin ella pipipi

descifrar([M1,M2|Resto], [R|R2]) :-
    cifrado([M1,M2], R),
    descifrar(Resto, R2).

% Se llama a cifrado para ver si nuestros n�meros calzan con alguna de
% las reglas, para terminar haciendo una recursi�n de descifrar por si
% la secuencia es m�s larga que dos d�gitos






