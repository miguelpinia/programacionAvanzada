{-#
  OPTIONS_GHC -fno-warn-unused-binds
#-}

{-|
Module: tarea4.hs
Description: Tarea del curso de programación avanzada en el posgrado
de Ciencias e Ingeniería en Computación, UNAM.

Mantainer: <miguel_pinia@ciencias.unam.mx, cinthia.rodriguez@ciencias.unam.mx>
-}

-- Para evitar que siga lanzando warnings.
main :: IO ()
main = print ""
--------------------------
-- Funciones auxiliares --
--------------------------

miUncurry :: (b -> c -> a) -> (b, c) -> a
miUncurry f (a, b)= f a b

miFlip :: (b -> c -> a) -> c -> b -> a
miFlip f a b = f b a

{- Obtiene la cabeza de una lista -}
cabeza :: [a] -> a
cabeza [] = error "Error! La lista está vacía"
cabeza (x:_) = x

{- Obtiene la cola de una lista-}
cola :: [a] -> [a]
cola [] = error "Error! La lista está vacía"
cola (_:xs) = xs

{- Función de plegado por la izquierda-}
-- plegadol fn val list
--   | esVacia list = val
--   | otherwise = plegadol fn (fn val (cabeza list)) (cola list)

plegadol :: (a -> b -> a) -> a -> [b] -> a
plegadol _ val [] = val
plegadol fn val (x:xs) = plegadol fn (fn val x) xs

{- Función de plegado por la derecha -}
plegador :: (a -> b -> b) -> b -> [a] -> b
plegador _ val [] = val
plegador fn val (x:xs) = fn x (plegador fn val xs)




{- Calcula la suma de los elementos de una lista de números enteros -}
suma :: [Int] -> Int
suma [] = 0
suma lista = plegadol (+) 0 lista

{- Obtiene la longitud de una lista de elementos -}
longitud :: [a] -> Int
longitud = plegadol (\x _ -> x + 1) 0
-- longitud' lista = suma [1 | _ <- lista] -- menos eficiente?

{- Obtiene los elementos filtrados por un predicado. -}
filtro :: (a -> Bool) -> [a] -> [a]
filtro _ [] = []
filtro p (x:xs)
  | p x = x : filtro p xs
  | otherwise = filtro p xs

{- Realiza la implementación de map -}
miMap :: (a -> b) -> [a] -> [b]
miMap _ [] = []
miMap fn (x:xs) = fn x:miMap fn xs
{- Implementa la función zip. -}
miZip :: [a] -> [b] -> [(a, b)]
miZip _ [] = []
miZip [] _ = []
miZip (a:as) (b:bs) = (a, b):miZip as bs

{- Verifica si un elemento es miembro de una lista -}
miembro :: Eq a => a -> [a] -> Bool
miembro x = plegadol (\z y -> z || y == x) False


---------------------------------------------------------------------------------------------------------------
-- Ejercicio 1: Función para sumar matrices. Las matrices pueden ser representadas como una lista de listas. --
---------------------------------------------------------------------------------------------------------------
{- Define el tipo para un renglon -}
type Renglon = [Int]
type Matriz = [Renglon]

mismaLongitud :: [a] -> [b] -> Bool
mismaLongitud a b = longitud a == longitud b

{- Define la suma de vectores -}
sumaVector :: Renglon -> Renglon -> Renglon
sumaVector a b
  | mismaLongitud a b = miMap (miUncurry (+)) (miZip a b)
  | otherwise = error "Los vectores no tienen la misma longitud"

{- Define la suma de matrices. -}
sumaMatriz :: Matriz -> Matriz -> Matriz
sumaMatriz a b
  | mismaLongitud a b = miMap (miUncurry sumaVector) (miZip a b)
  | otherwise = error "Las matrices no tienen la misma longitud"


---------------------------------------------------------------------
-- Ejercicio 2: Una función que indique que dos listas son iguales --
--   aunque los elementos aparezcan en distinto orden.             --
---------------------------------------------------------------------

extrae :: Eq a => a -> [a] -> [a]
extrae x = filtro (== x)

{- Verifica si dos listas son iguales por elementos -}
iguales :: Eq a => [a] -> [a] -> Bool
iguales xs ys =
  mismaLongitud xs ys &&
  plegadol (\z x -> z && extrae x xs == extrae x ys) True xs

{- Verifica si dos listas son iguales si contienen los mismos
elementos cuando se comparan en forma de conjuntos. -}
igualesSet :: Eq a => [a] -> [a] -> Bool
igualesSet xs ys =
  plegadol (\z x -> z && miembro x ys) True xs &&
  plegadol (\z y -> z && miembro y xs) True ys

------------------------------------------------------------------------------------
-- Ejercicio 3: Define la función invertir una lista usando la función de plegado --
--   ṕor la derecha y define otra usando plegado por la izquierda.                --
------------------------------------------------------------------------------------

{- Dada una lista, calcula su inversa usando pleglado por la izquierda. -}
inversal :: [a] -> [a]
inversal = plegadol (miFlip (:)) []
{- Dada una lista, calcula su inversa usando plegado por la derecha. 1-}
inversar :: [a] -> [a]
inversar = plegador (\z x -> x ++ [z]) []


-----------------------------------------------------------------
-- Ejercicio 4: Define una función para ordenar dos listas que --
--   recibe como parámetros.                                   --
-----------------------------------------------------------------

{- Implementación de quicksort -}
qs :: (Ord a) => [a] -> [a]
qs [] = []
qs (x:xs) = qs menor_que_x ++ [x] ++ qs mayor_que_x
  where menor_que_x = [y | y <- xs, y <= x]
        mayor_que_x = [y | y <- xs, y > x]

{- Implemntación de ordenamiento de dos listas -}
ordena :: (Ord a) => [a] -> [a] -> [a]
ordena xs ys = qs (xs ++ ys)
