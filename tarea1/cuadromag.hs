
nums::Int->[Int]
nums n = [1..n*n]

permutations::Eq a=>[a]->[[a]]
permutations [] = [[]]
permutations as = do a <- as
                     let l = filter (a/=) as
                     ls <- permutations l
                     return $ a : ls

type Cuadro = [[Int]]
           
cuadros::Int->[Cuadro]                                          
cuadros n = [corta n p | p<-permutations $ nums n] where
                        corta _ [] = []
                        corta n xs = (take n xs):(corta n $ drop n xs)
                        
                  
                                                    
sumaMag::Int->Cuadro->Bool
sumaMag n c = let m = (div (n*(n*n + 1)) 2) in sumaReng c m && sumaCol c n m where
                                               sumaReng [] _ = True
                                               sumaReng (r:rs) m = (sum r == m) && sumaReng rs m
                                               sumaCol c 0 m = True 
                                               sumaCol c n m = sum (map head c) == m && sumaCol (map tail c) (n-1) m
     
     
cuadrosMag :: Int -> [Cuadro]                   
cuadrosMag n = [c|c<-cuadros n,sumaMag n c]
                                                                                                

main::IO ()
main = pintaCuadros $ take 5 $ cuadrosMag 3 where
                                 pintaCuadros cs = itera cs 
                                 pintaCuadro [r1,r2,r3] = show r1 ++ "\n" ++ show r2 ++ "\n"++ show r3
                                 itera [c] = putStrLn $ pintaCuadro c   
                                 itera (c:cs) = do 
                                                 putStrLn $ pintaCuadro c ++ "\n"
                                                 itera cs



