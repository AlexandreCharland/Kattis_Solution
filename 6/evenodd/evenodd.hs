solve :: [Integer] -> [Integer]
solve [] = []
solve (a:b:rs) = (g b - g (a-1)) `mod` (10^9+7) : solve rs

b :: Integer -> [Integer]
b 1 = []
b n = n `mod` 2 : b (n `div` 2)

len :: [Integer] -> Integer
len = foldr (\ x -> (+) 1) 0

f :: Integer -> Integer
f 1 = 0
f n = if even n then f (n `div` 2)+1 else f ((n `div` 2)+1)+2

g :: Integer -> Integer
g 0 = 0
g 1 = 0
g n = let m = reverse (b n) in g' m (len m)

g' :: [Integer] -> Integer -> Integer
g' m l = g2 l + h m (l-2) 1

h :: [Integer] -> Integer -> Integer -> Integer
h [] _ _ = 0
h (x:xs) r a = let b = 2*a+x in (h xs (r-1) b) + if x==1 then (gdif b r) + f(b*2^(r+1)) else 0

g2 :: Integer -> Integer
g2 0 = 0
g2 r = 2 + (3*r-4)*(2^(r-1))

gdif :: Integer -> Integer -> Integer
gdif a r = if r<0 then 0 else (r + 2 + f a)*(2^(r+1)-1)+(r-1)*(2^r)+1

readInput = map read . words
writeOutput = unlines . map show
main = interact (writeOutput . solve . readInput)