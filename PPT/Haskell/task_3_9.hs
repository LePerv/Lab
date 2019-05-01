alphabet = ["a", "b", "c"]
states = [0, 1, 2, 3, 4]
initial = 0
final = [4]
transitions = [[1, 2, 3], [1, 4, 4], [4, 1, 4], [4, 4, 1], [-1, -1, -1]]

accumIndexOf [] value index = -1
accumIndexOf list value index =
    let h = head list
        t = tail list
    in if h == value
        then index
        else accumIndexOf t value (index + 1)
indexOf list value =
    accumIndexOf list value 0

accumGetListValue [] i k = undefined
accumGetListValue list i k = 
    let h = head list
        t = tail list
    in if i == k
        then h
        else accumGetListValue t i (k + 1)
getListValue list i = accumGetListValue list i 0

accumGetMatrixValue [] i j k = undefined
accumGetMatrixValue matrix i j k =
    let h = head matrix
        t = tail matrix
    in if i == k
        then getListValue h j
        else accumGetMatrixValue t i j (k + 1)
getMatrixValue matrix i j =
    accumGetMatrixValue matrix i j 0

accumDoWork [] currentState = True
accumDoWork word currentState =
    if (indexOf final currentState) /= -1
        then False
        else 
            let h = head word
                t = tail word
                nextState = getMatrixValue transitions currentState (indexOf alphabet h)
            in if nextState == -1
                then False
                else accumDoWork t nextState
doWork word = 
    accumDoWork word initial

main = do
    print(doWork ["a", "a", "a", "a", "b", "c"])