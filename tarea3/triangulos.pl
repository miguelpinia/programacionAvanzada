/*
 * Identifica si tres números cumplen con la desigualdad del triángulo.
 */
desigualdad_del_triangulo(X, Y, Z) :-
    X + Y > Z,
    Y + Z > X,
    Z + X > Y.

/*
 * Predicado auxiliar para determinar que triángulo se forma con tres
 * números dados. Sólo podemos tener un triángulo isóceles cuando dos
 * lados son iguales, un triángulo equilátero cuando tres lados son
 * iguales y un triángulo escaleno cuando tres números son distintos y
 * satisfacen la desigualdad del triángulo.
 */
t_(X, Y, Z, 'No se puede formar un triángulo') :- not(desigualdad_del_triangulo(X, Y, Z)).
t_(X, Y, Z, 'Triangulo isóceles') :-
    desigualdad_del_triangulo(X, Y, Z),
    ((X = Y, X \= Z); (Y = Z, Y \= X); (Z = X, Z \= Y)), !.
t_(X, Y, Z, 'Triángulo equilatero') :-
    desigualdad_del_triangulo(X, Y, Z),
    (X = Y, Y = Z), !.
t_(X, Y, Z, 'Triángulo escaleno') :-
    desigualdad_del_triangulo(X, Y, Z),
    X \= Y, Y \= Z, !.

/*
 * Imprime que triángulo forman tres números si es que se forma alguno.
 */
triangulo(X, Y, Z) :-
    t_(X, Y, Z, Resultado),
    write(Resultado), !.