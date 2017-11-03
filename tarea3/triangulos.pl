/*
 * EJERCICIO 2
 */

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


/*
 * EJERCICIO 3
 */
%Filtrado de elementos repetidos
filtra([], []) :- !.
filtra([X|Xs], Ys) :-
   member(X, Xs),
   !,
   filtra(Xs, Ys).
filtra([X|Xs], [Y|Ys]) :-
   Y is X,
   filtra(Xs, Ys).




/*
 * EJERCICIO 4
 */
suma([], [], []) :- !.
suma([A|As], [B|Bs], [A_plus_B | ABs]) :-
    A_plus_B is A + B
    , suma(As, Bs, ABs), !.


sumamatriz([[M1]], [[M2]], S) :-
   forall(member(m1,M1), member(m2, M2), suma(m1, m2, S)).



/*
 * EJERCICIO 5
 */
ackermann(0,N,X) :- X is N+1.
ackermann(M, 0, X) :- M>0, M1 is M-1, ackermann(M1, 1, X).
ackermann(M, N, X) :- M>0, N>0, M1 is M-1, N1 is N-1,
ackermann(M, N1, X1), ackermann(M1, X1, X).

