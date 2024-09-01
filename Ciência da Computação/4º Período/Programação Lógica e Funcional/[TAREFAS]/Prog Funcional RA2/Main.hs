-- Daniela Lima e Lucas Azevedo Dias

module Main where
import Data.List as DList

-- 1. Escreva uma função que devolva a soma de todos os números menores que 10.000 que sejam múltiplos de 3 ou 5 e não sejam múltiplos de 2.
multiplesLowerThan :: Int -> Int -> Int -> [Int]
multiplesLowerThan mustMult notMult lowerThan =
  [x | x <- [1 .. lowerThan], mod x mustMult == 0, mod x notMult /= 0]

-- 2. Escreva uma função que devolva a diferença entre a soma de todos os números de Fibonacci ímpares menores que 100.000 e a soma de todos os números de Fibonacci pares também menores que 100.000.
fibonacci :: [Integer]
fibonacci = 0 : 1 : zipWith (+) fibonacci (tail fibonacci)

somaFibonacci :: Integer -> Integer
somaFibonacci limite = somaImpares - somaPares
  where
    fibMenorQueLimite = takeWhile (<limite) fibonacci
    somaImpares = sum [x | x <- fibMenorQueLimite, odd x]
    somaPares = sum [x | x <- fibMenorQueLimite, even x]

-- 3. Fatorar um número em seus divisores primos é uma tarefa importante para a segurança de dados. Escreva uma função que devolva os fatores primos de qualquer inteiro dado maior que 100.000.000 e menor que 1.000.000.000.
tryFactoring :: Int -> Int -> [Int]
tryFactoring n divisor
  | n == 1 = []
  | mod n divisor == 0 = divisor : tryFactoring (div n divisor) divisor
  | otherwise = tryFactoring n (divisor + 1)

factorNumber :: Int -> [Int]
factorNumber n = tryFactoring n 2

factorNumberInInterval :: Int -> Int -> Int -> [Int]
factorNumberInInterval number higherThan lowerThan
  | number < higherThan = []
  | number > lowerThan = []
  | otherwise = factorNumber number

-- 4. Escreva uma função que, recebendo uma lista de inteiros, apresente a diferença entre a soma dos quadrados e o quadrado da soma destes inteiros.
somaQuadrados :: [Integer] -> Integer
somaQuadrados xs = sum (map (^ 2) xs)

quadradoSoma :: [Integer] -> Integer
quadradoSoma xs = (^ 2) (sum xs)

diferenca :: [Integer] -> Integer
diferenca xs = quadradoSoma xs - somaQuadrados xs

-- 5. O Crivo de Eratóstenes não é o melhor algoritmo para encontrar números primos. Crie uma função que implemente o Crivo de Euler (Euler’s Sieve) para encontrar todos os números primos menores que um determinado inteiro dado.
eulerSieve :: Int -> [Int]
eulerSieve n = sieve n (n - 2) [2 .. n]
  where
    sieve n counter list
      | counter < 0 = list
      | otherwise = let mult = ([2 .. n] !! counter) in sieve n (counter - 1) [y | y <- list, y `notElem` [mult * x | x <- list]]

-- 6. Escreva uma função, usando iterate que devolva uma lista infinita de inteiros de tal forma que o inteiro 𝑛 será o dobro do inteiro 𝑛 − 1. Esta função deve receber o valor inicial da lista.
gerarListaDobro :: Integer -> Int -> [Integer]
gerarListaDobro valorInicial quantidade = take quantidade (iterate (*2) valorInicial)

-- 7. Escreva uma função que receba uma string e devolva outra string com as vogais trocadas. De tal forma que: 𝑎 será transformado em 𝑢; 𝑒 será transformado em 𝑜; 𝑖 não será transformado; 𝑜 será transformado em 𝑒 e 𝑢 será transformado em 𝑎.
changeVowels :: String -> String
changeVowels "" = ""
changeVowels (c:cs) =
  case DList.elemIndex c "AEIOUaeiou" of
    Just index -> ("UOIEAuoiea" !! index) : changeVowels cs
    Nothing -> c : changeVowels cs

-- 8. Nem só de Fibonacci vivem os exemplos de recursão. Escreva uma função que devolva todos os números de uma sequência de Lucas (2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123) menores que um inteiro dado como argumento.
lucas :: [Integer]
lucas = 2 : 1 : zipWith (+) lucas (tail lucas)

sequenciaLucas :: Integer -> [Integer]
sequenciaLucas limite = takeWhile (<= limite) lucas

-- 9. Escreva uma função análoga a função map, disponível no prelude, na qual um predicado, função, seja aplicado a duas listas e não a apenas uma. Por exemplo 𝑚𝑎𝑝2 (+) [1,2,3] [10,11,12] deve retornar [11,13,15].
myMap :: (a -> b -> c) -> [a] -> [b] -> [c]
myMap _ _ [] = []
myMap _ [] _ = []
myMap f (x:xs) (y:ys) =
  f x y : myMap f xs ys

-- Main
main :: IO()
main = do
  putStrLn "AVALIAÇÃO EM GRUPO RA2"

  -- EXERCISE 1
  putStrLn "\n1. Escreva uma função que devolva a soma de todos os números menores que 10.000 que sejam múltiplos de 3 ou 5 e não sejam múltiplos de 2."
  print $ multiplesLowerThan (3 * 5) 2 10000
  -- Obs.: para ser múltiplo de 3 e 5, então precisa ser de 15, ou seja, (3 * 5)

  -- EXERCISE 2
  putStrLn "\n2. Escreva uma função que devolva a diferença entre a soma de todos os números de Fibonacci ímpares menores que 100.000 e a soma de todos os números de Fibonacci pares também menores que 100.000."
  print $ somaFibonacci 100000

  -- EXERCISE 3
  putStrLn "\n3. Fatorar um número em seus divisores primos é uma tarefa importante para a segurança de dados. Escreva uma função que devolva os fatores primos de qualquer inteiro dado maior que 100.000.000 e menor que 1.000.000.000."
  print $ factorNumberInInterval 100000004 100000000 1000000000

  -- EXERCISE 4
  putStrLn "\n4. Escreva uma função que, recebendo uma lista de inteiros, apresente a diferença entre a soma dos quadrados e o quadrado da soma destes inteiros."
  print $ diferenca [1 .. 10]

  -- EXERCISE 5
  putStrLn "\n5. O Crivo de Eratóstenes não é o melhor algoritmo para encontrar números primos. Crie uma função que implemente o Crivo de Euler (Euler’s Sieve) para encontrar todos os números primos menores que um determinado inteiro dado."
  print $ eulerSieve 100

  -- EXERCISE 6
  putStrLn "\n6. Escreva uma função, usando iterate que devolva uma lista infinita de inteiros de tal forma que o inteiro 𝑛 será o dobro do inteiro 𝑛 − 1. Esta função deve receber o valor inicial da lista."
  print $ gerarListaDobro 1 10

  -- EXERCISE 7
  putStrLn "\n7. Escreva uma função que receba uma string e devolva outra string com as vogais trocadas. De tal forma que: 𝑎 será transformado em 𝑢; 𝑒 será transformado em 𝑜; 𝑖 não será transformado; 𝑜 será transformado em 𝑒 e 𝑢 será transformado em 𝑎."
  print $ changeVowels "ola pessoas, bom dia, atumalaca!"

  -- EXERCISE 8
  putStrLn "\n8. Nem só de Fibonacci vivem os exemplos de recursão. Escreva uma função que devolva todos os números de uma sequência de Lucas (2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123) menores que um inteiro dado como argumento."
  print $ sequenciaLucas 100

  -- EXERCISE 9
  putStrLn "\n9. Escreva uma função análoga a função map, disponível no prelude, na qual um predicado, função, seja aplicado a duas listas e não a apenas uma. Por exemplo 𝑚𝑎𝑝2 (+) [1,2,3] [10,11,12] deve retornar [11,13,15]."
  print $ myMap (+) [1,2,3] [10,11,12]
