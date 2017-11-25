{-|
Module: tarea4.hs
Description: Tarea del curso de programación avanzada en el posgrado
de Ciencias e Ingeniería en Computación, UNAM.

Mantainer: <miguel_pinia@ciencias.unam.mx, cinthia.rodriguez@ciencias.unam.mx>
-}

--------------------------
-- Funciones auxiliares --
--------------------------

{- Función de plegado por la izquierda-}
plegadol :: (a -> b -> a) -> a -> [b] -> a
plegadol fn val [] = val
plegadol fn val (x:xs) = plegadol fn (fn val x) xs

{- Función de plegado por la derecha -}
plegador :: (a -> b -> b) -> b -> [a] -> b
plegador fn val [] = val
plegador fn val (x:xs) = fn x (plegador fn val xs)

{- Obtiene la cabeza de una lista -}
cabeza :: [a] -> a
cabeza [] = error "Error! La lista está vacía"
cabeza (x:_) = x

{- Obtiene la cola de una lista-}
cola :: [a] -> [a]
cola [] = error "Error! La lista está vacía"
cola (_:xs) = xs

{- Calcula la suma de los elementos de una lista de números enteros -}
suma :: [Int] -> Int
suma [] = 0
suma lista = plegadol (+) 0 lista

{- Obtiene la longitud de una lista de elementos -}
longitud :: [a] -> Int
longitud lista = suma [1 | _ <- lista]

{- Obtiene los elementos filtrados por un predicado. -}
filtro :: (a -> Bool) -> [a] -> [a]
filtro p [] = []
filtro p (x:xs) =
  if p x
    then x : (filtro p xs)
    else filtro p xs

{- Realiza la implementación de map -}
miMap fn [] = []
miMap fn (x:xs) = fn x:miMap fn xs
{- Implementa la función zip. -}
miZip :: [a] -> [b] -> [(a, b)]
miZip xs [] = []
miZip [] ys = []
miZip (a:as) (b:bs) = (a, b):miZip as bs

{- Verifica si un elemento es miembro de una lista -}
miembro :: Eq a => a -> [a] -> Bool
miembro x ys = plegadol (\z y -> z || y == x) False ys


---------------------------------------------------------------------------------------------------------------
-- Ejercicio 1: Función para sumar matrices. Las matrices pueden ser representadas como una lista de listas. --
---------------------------------------------------------------------------------------------------------------
{- Define el tipo para un renglon -}
type Renglon = [Int]

{- Define la suma de vectores -}
sumaVector :: Renglon -> Renglon -> Renglon
sumaVector a b =
  if longitud a == longitud b
    then miMap (\((a,b)) -> a + b) (miZip a b)
    else error "Los vectores no tienen la misma longitud"
{- Define la suma de matrices. -}
sumaMatriz :: [Renglon] -> [Renglon] -> [Renglon]
sumaMatriz a b =
  if longitud a == longitud b
    then miMap (\((r1, r2)) -> sumaVector r1 r2) (miZip a b)
    else error "Las matrices no tienen la misma longitud"

---------------------------------------------------------------------
-- Ejercicio 2: Una función que indique que dos listas son iguales --
--   aunque los elementos aparezcan en distinto orden.             --
---------------------------------------------------------------------

{- Verifica si dos listas son iguales por elementos -}
iguales :: Eq a => [a] -> [a] -> Bool
iguales xs ys =
  longitud xs == longitud ys &&
  plegadol (\z x -> z && (filtro (== x) xs) == (filtro (== x) ys)) True xs

{- Verifica si dos listas son iguales si contienen los mismos
elementos cuando se comparan en forma de conjuntos. -}
igualesSet xs ys =
  plegadol (\z x -> z && (miembro x ys)) True xs &&
  plegadol (\z y -> z && (miembro y xs)) True ys

------------------------------------------------------------------------------------
-- Ejercicio 3: Define la función invertir una lista usando la función de plegado --
--   ṕor la derecha y define otra usando plegado por la izquierda.                --
------------------------------------------------------------------------------------

{- Dada una lista, calcula su inversa usando pleglado por la izquierda. -}
inversal :: [a] -> [a]
inversal xs = plegadol (\z x -> [x] ++ z) [] xs
{- Dada una lista, calcula su inversa usando plegado por la derecha. 1-}
inversar :: [a] -> [a]
inversar xs = plegador (\z x -> x ++ [z]) [] xs


-----------------------------------------------------------------
-- Ejercicio 4: Define una función para ordenar dos listas que --
--   recibe como parámetros.                                   --
-----------------------------------------------------------------

{- Implementación de quicksort -}
qs :: (Ord a) => [a] -> [a]
qs [] = []
qs (x:xs) = (qs menor_que_x) ++ [x] ++ (qs mayor_que_x)
  where menor_que_x = [y | y <- xs, y <= x]
        mayor_que_x = [y | y <- xs, y > x]

{- Implemntación de ordenamiento de dos listas -}
ordena :: (Ord a) => [a] -> [a] -> [a]
ordena xs ys = qs (xs ++ ys)
