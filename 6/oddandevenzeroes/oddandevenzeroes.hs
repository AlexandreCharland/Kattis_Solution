solve [] = []
solve [-1] = []
solve (n:rest) = f n:(solve rest)

lo :: Integer -> Integer
lo 0 = -1
lo x = lo (x `div` 5) + 1

f :: Integer -> Integer
f n = i n (lo n)

i :: Integer -> Integer -> Integer
i n k = if k == -1 then 1 else j n k (n `div` 5^k)

j :: Integer -> Integer -> Integer -> Integer
j n k a = let b
                | a == 0 = 0
                | a == 1 = f1 k
                | a == 2 = f2 k
                | a == 3 = f3 k
                | otherwise = 2 * f2 k
            in b + l (n - a * 5^k) (k * a)

l :: Integer -> Integer -> Integer
l n k = if even k then f n else n + 1 - f n

f1 :: Integer -> Integer
f1 0 = 1
f1 k = if odd k then f1 (k-1)*5 else (f1 (k-1) - 2*5^((k-2)`div`2))*5

f2 :: Integer -> Integer
f2 k = if odd k then 5^k else 5^k + 5^(k `div` 2)

f3 :: Integer -> Integer
f3 k = if even k then (g k -1)*5^(k `div` 2) else (g k - 1)*2*5^((k+1)`div`2)

g :: Integer -> Integer
g 0 = 4
g k = if odd k then g (k-1) `div` 2 else g (k-2)*5-10

readInput = map read . words
writeOutput = unlines . map show
main = interact (writeOutput . solve . readInput)