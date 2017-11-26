ordena :: (Ord a) => [a] -> [a] -> [a]
ordena xs ys = ordenaLista(xs ++ ys)

ordenaLista :: Ord a => [a] -> [a]
ordenaLista [] = []
ordenaLista (x:xs) = aux xs x []
    where aux [] m r = m : ordenaLista r
          aux (x:xs) m r | x < m     = aux xs x (m:r)
                         | otherwise = aux xs m (x:r)