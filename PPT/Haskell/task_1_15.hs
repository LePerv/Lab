isInList x l = if l == []
                  then False
                  else let y = head l
                           ys = tail l
                       in if x == y
                             then True
                             else isInList x ys

removeDuplicates l = if l == []
                        then l
                        else let x = head l
                                 xs = tail l
                             in if isInList x xs
                                   then removeDuplicates xs
                                   else x:removeDuplicates xs

main = do
    let list = [1, 1, 1, 1]

    print (removeDuplicates list)
