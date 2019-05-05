import Data.List

alphabet = ["a", "b", "c"]
states = [0, 1, 2, 3, 4]
initial = 0
final = [4]
transitions = [[1, 2, 3], [1, 4, 4], [4, 1, 4], [4, 4, 1], [4, 4, 4]]

checkIfSublist [] _ = False
checkIfSublist _ [] = True
checkIfSublist [] [] = True
checkIfSublist list sublist =
    let h1 = head list
        t1 = tail list
        h2 = head sublist
        t2 = tail sublist
    in if h1 == h2
        then checkIfSublist t1 t2
        else False

accumDoWork word w1 w2 x y z currentState =
    if (elemIndices currentState final)!!0 /= -1
        then False
        else if word == w1
            then
                if word == w2
                    then True
                    else
                        if (checkIfSublist word w2)
                            then
                                let l = last w2
                                in
                                    let character = word!!((elemIndices l word)!!0 + 1)
                                    in
                                        let nextState = (elemIndices character (transitions!!currentState))!!0
                                            _w2 = w2 ++ [character]
                                        in accumDoWork word w1 _w2 x y z nextState
                            else
                                let _y = y ++ w2
                                    _w2 = []
                                in accumDoWork word w1 _w2 x _y z currentState
            else
                if (checkIfSublist word w1)
                    then
                        let l = last w1
                        in
                            let character = word!!(elemIndices l word)!!0 + 1)
                            in
                                let nextState = (elemIndices character (transitions!!currentState))!!0
                                    _w1 = w1 ++ [character]
                                in accumDoWork word _w1 w2 x y z nextState
                    else
                        let _x = x ++ w1
                            _w1 = []
                        in accumDoWork word _w1 w2 _x y z currentState


doWork word =
    accumDoWork word [] [] [] [] [] initial

main = do
    print(doWork ["a", "a"])
