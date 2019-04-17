import Data.Bits

isPower2 :: Integer -> Bool

isPower2 x = if x == 0
                then False
                else if (x .&. (x - 1)) == 0
                        then True
                        else False

doWork l from = if l == []
                   then l
                   else let x = head l
                            xs = tail l
                        in if isPower2 from
                              then x:doWork xs (from + 1)
                              else doWork xs (from + 1)

main = do
    let list = [0, 1, 2, 3, 4, 5, 6]
    print (doWork list 0)
