power2 :: Int -> Int
power2 0 = 1
power2 x = 2 * power2 (x - 1)

extractNFirstFrom :: [a] -> Int -> [a]
extractNFirstFrom [] n = []
extractNFirstFrom l 0 = l
extractNFirstFrom l n
    | n > 0 = extractNFirstFrom (tail l) (n - 1)
    | otherwise = l

extractNFirstTo :: [a] -> [a] -> Int -> [a]
extractNFirstTo to [] n = to
extractNFirstTo to from 0 = to
extractNFirstTo to from n
    | (length to) >= n = to
    | otherwise = let x = head from
                      xs = tail from
                  in extractNFirstTo (to ++ [x]) xs n

accumSplitList :: [[a]] -> [a] -> [[a]]
accumSplitList dest [] = dest
accumSplitList dest list
    | length list == 0 = dest
    | otherwise = let n = power2 (length dest)
                  in let e = extractNFirstTo [] list n
                         l = extractNFirstFrom list n
                     in accumSplitList (dest ++ [e]) l

splitList :: [a] -> [[a]]
splitList l = accumSplitList [] l

main = do
  let l = [1, 2, 3, 4, 0, 5, 4, 2, 1, 5, 4, 2, 5, 4, 2, 3, 4]
  print (splitList l)
